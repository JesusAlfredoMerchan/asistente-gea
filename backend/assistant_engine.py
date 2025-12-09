import re
import json
import uuid
import os
import time
import hashlib
from typing import Dict, List, Optional, Tuple
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Cargar variables de entorno
load_dotenv()

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  google-generativeai no está instalado. Ejecuta: pip install google-generativeai")

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  openai no está instalado. Ejecuta: pip install openai")

class GEAAssistant:
    """
    Motor principal del asistente inteligente para GEA
    Procesa preguntas y genera respuestas usando Gemini AI con la base de conocimiento
    """
    
    def __init__(self, knowledge_base_path: str = "../Base_Conocimiento_GEA.md"):
        self.knowledge_base_path = Path(knowledge_base_path)
        self.knowledge_base = self._load_knowledge_base()
        self.conversations: Dict[str, List[Dict]] = {}
        self.model = None
        self.current_model_name: Optional[str] = None
        self._ready = False
        
        # Modelos disponibles y gestión
        self.available_models: List[str] = []
        self.model_instances: Dict[str, any] = {}  # Cache de instancias de modelos
        self.preferred_models = [
            "gemini-2.0-flash-exp",
            "gemini-2.0-flash-thinking-exp",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
            "gemini-pro"
        ]  # Orden de preferencia
        
        # Control de cuotas por modelo
        self.model_quota_status: Dict[str, Dict] = {}  # {model_name: {"exceeded": bool, "reset_time": datetime, "request_count": int}}
        self.quota_tracking: Dict[str, int] = {}  # Contador simple de requests por modelo
        
        # Modelos alternativos (OpenAI)
        self.openai_client = None
        self.openai_models = ["gpt-3.5-turbo"]  # Modelos OpenAI disponibles
        
        # Cache de respuestas para evitar llamadas repetidas a Gemini
        self.response_cache: Dict[str, Dict] = {}
        self.cache_ttl = 3600  # TTL de 1 hora para el cache
        
        # Control de rate limiting
        self.last_request_time = 0
        self.min_request_interval = 1.0  # Mínimo 1 segundo entre requests
        self.quota_exceeded = False
        self.quota_reset_time = None
        
        # Inicializar Gemini
        self._initialize_gemini()
        
    def _initialize_gemini(self):
        """Inicializar el modelo Gemini y detectar modelos disponibles"""
        if not GEMINI_AVAILABLE:
            print("❌ Gemini no está disponible. Instala google-generativeai")
            self._ready = False
            return
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("⚠️  GEMINI_API_KEY no encontrada en variables de entorno")
            print("   Crea un archivo .env en la carpeta backend con: GEMINI_API_KEY=tu_api_key")
            self._ready = False
            return
        
        try:
            print("Inicializando modelos Gemini...")
            genai.configure(api_key=api_key)
            
            print("Buscando modelos disponibles...")
            models = genai.list_models()
            all_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
            
            # Filtrar y ordenar modelos por preferencia
            self.available_models = []
            for preferred in self.preferred_models:
                # Buscar variantes del modelo preferido
                matching = [m for m in all_models if preferred in m or m in preferred]
                if matching:
                    self.available_models.extend(matching)
            
            # Agregar cualquier otro modelo que no esté en la lista preferida
            for model in all_models:
                if model not in self.available_models:
                    self.available_models.append(model)
            
            print(f"✓ Modelos encontrados ({len(self.available_models)})")
            print("🔍 Verificando disponibilidad de modelos...")
            
            # Probar cada modelo para ver cuáles están disponibles
            self._test_models_availability()
            
            # Filtrar solo los modelos disponibles
            working_models = [m for m in self.available_models 
                            if self.model_quota_status.get(m, {}).get("available", False)]
            
            print(f"✓ Modelos disponibles y funcionales: {len(working_models)}")
            
            # Inicializar OpenAI si está disponible (ANTES de seleccionar modelo inicial)
            self._initialize_openai()
            
            # Recalcular modelos disponibles después de agregar OpenAI
            working_models = [m for m in self.available_models 
                            if self.model_quota_status.get(m, {}).get("available", False)]
            
            if len(working_models) > len([m for m in working_models if not m.startswith("openai:")]):
                print(f"✓ Total modelos disponibles (incluyendo OpenAI): {len(working_models)}")
            
            # Seleccionar modelo inicial
            initial_model = self._select_best_available_model()
            
            if initial_model:
                self._switch_model(initial_model)
                print(f"✓ Modelo activo: {self.current_model_name}")
                self._ready = True
            else:
                print("❌ No se encontraron modelos disponibles")
                self._ready = False
                
        except Exception as e:
            print(f"❌ Error al inicializar Gemini: {e}")
            self._ready = False
    
    def _test_models_availability(self):
        """Probar cada modelo para verificar si está disponible y funciona"""
        print("🔍 Probando disponibilidad de modelos...")
        test_prompt = "test"
        
        for model_name in self.available_models:
            if model_name not in self.model_quota_status:
                self.model_quota_status[model_name] = {
                    "exceeded": False,
                    "reset_time": None,
                    "request_count": 0,
                    "available": False
                }
            
            # Si ya está marcado como excedido recientemente, no probar
            quota_status = self.model_quota_status[model_name]
            if quota_status.get("exceeded", False):
                reset_time = quota_status.get("reset_time")
                if reset_time and datetime.now() < reset_time:
                    print(f"  ⏭️  {model_name}: Excedido (skip)")
                    quota_status["available"] = False
                    continue
            
            try:
                # Probar con una llamada pequeña
                test_model = genai.GenerativeModel(model_name)
                response = test_model.generate_content(
                    test_prompt,
                    generation_config={"max_output_tokens": 10}
                )
                if response and response.text:
                    quota_status["available"] = True
                    print(f"  ✅ {model_name}: Disponible")
                else:
                    quota_status["available"] = False
                    print(f"  ❌ {model_name}: No responde")
            except Exception as e:
                error_str = str(e)
                # Detectar si es error de cuota
                if "429" in error_str or "quota" in error_str.lower() or "Quota exceeded" in error_str:
                    quota_status["exceeded"] = True
                    quota_status["reset_time"] = datetime.now() + timedelta(hours=24)
                    quota_status["available"] = False
                    print(f"  ⚠️  {model_name}: Cuota excedida")
                else:
                    quota_status["available"] = False
                    print(f"  ❌ {model_name}: Error ({error_str[:50]})")
            
            # Pequeña pausa entre pruebas
            time.sleep(0.5)
    
    def _initialize_openai(self):
        """Inicializar cliente de OpenAI si está disponible"""
        if not OPENAI_AVAILABLE:
            print("⚠️  OpenAI no está disponible. Instala: pip install openai")
            return
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("⚠️  OPENAI_API_KEY no encontrada. Modelos OpenAI no estarán disponibles.")
            return
        
        try:
            # Guardar variables de entorno problemáticas temporalmente
            problematic_vars = {}
            for var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
                if var in os.environ:
                    problematic_vars[var] = os.environ.pop(var)
            
            # Configurar API key
            os.environ["OPENAI_API_KEY"] = api_key
            
            try:
                # Intentar inicialización simple
                import inspect
                # Verificar qué parámetros acepta OpenAI.__init__
                init_signature = inspect.signature(OpenAI.__init__)
                
                # Si tiene parámetro api_key, usarlo directamente
                if 'api_key' in init_signature.parameters:
                    self.openai_client = OpenAI(api_key=api_key)
                else:
                    # Si no, usar variable de entorno
                    self.openai_client = OpenAI()
                
                # Agregar modelos OpenAI a la lista disponible
                for model_name in self.openai_models:
                    openai_model_key = f"openai:{model_name}"
                    if openai_model_key not in self.available_models:
                        self.available_models.append(openai_model_key)
                    self.model_quota_status[openai_model_key] = {
                        "exceeded": False,
                        "reset_time": None,
                        "request_count": 0,
                        "available": True,
                        "provider": "openai"
                    }
                
                print(f"✓ OpenAI inicializado. Modelos disponibles: {', '.join(self.openai_models)}")
                # Verificar que se agregaron correctamente
                for model_name in self.openai_models:
                    openai_model_key = f"openai:{model_name}"
                    status_check = self.model_quota_status.get(openai_model_key, {})
                    print(f"   ✓ {openai_model_key}: available={status_check.get('available', False)}")
            except (TypeError, AttributeError) as e:
                error_msg = str(e)
                if "proxies" in error_msg or "unexpected keyword argument" in error_msg:
                    print(f"⚠️  Error de compatibilidad con OpenAI (versión antigua): {error_msg}")
                    print("   Sugerencia: Actualiza OpenAI con: pip install --upgrade openai")
                    print("   Por ahora, OpenAI estará deshabilitado. El sistema funcionará solo con Gemini.")
                    self.openai_client = None
                else:
                    raise
            finally:
                # Restaurar variables de entorno
                for var, value in problematic_vars.items():
                    os.environ[var] = value
                    
        except Exception as e:
            error_msg = str(e)
            if "proxies" in error_msg:
                print(f"⚠️  Error de compatibilidad: OpenAI requiere actualización.")
                print("   Ejecuta: pip install --upgrade openai")
            else:
                print(f"⚠️  Error al inicializar OpenAI: {e}")
            self.openai_client = None
            print("   El sistema continuará funcionando con los modelos de Gemini disponibles.")
    
    def _select_best_available_model(self) -> Optional[str]:
        """Seleccionar el mejor modelo disponible que funcione"""
        # Primero intentar modelos disponibles y no excedidos
        for model_name in self.available_models:
            quota_status = self.model_quota_status.get(model_name, {})
            
            # Verificar si está disponible
            if not quota_status.get("available", False):
                continue
            
            # Verificar si tiene cuota excedida
            if quota_status.get("exceeded", False):
                reset_time = quota_status.get("reset_time")
                if reset_time and datetime.now() < reset_time:
                    continue  # Este modelo está excedido, intentar el siguiente
                else:
                    # Resetear status si ya pasó el tiempo
                    quota_status["exceeded"] = False
                    quota_status["reset_time"] = None
                    quota_status["available"] = True  # Marcar como disponible de nuevo
            
            return model_name
        
        # Si todos están excedidos, intentar con el primero disponible de todos modos
        for model_name in self.available_models:
            quota_status = self.model_quota_status.get(model_name, {})
            if quota_status.get("available", False):
                return model_name
        
        return None
    
    def _switch_model(self, model_name: str) -> bool:
        """Cambiar al modelo especificado"""
        if model_name not in self.available_models:
            print(f"❌ Modelo {model_name} no está disponible")
            return False
        
        # Verificar si es un modelo OpenAI
        if model_name.startswith("openai:"):
            if not self.openai_client:
                print(f"❌ Cliente OpenAI no está inicializado")
                return False
            self.model = None  # Para OpenAI usamos el cliente directamente
            self.current_model_name = model_name
            # Inicializar tracking de cuota si no existe
            if model_name not in self.model_quota_status:
                self.model_quota_status[model_name] = {
                    "exceeded": False,
                    "reset_time": None,
                    "request_count": 0,
                    "available": True,
                    "provider": "openai"
                }
            return True
        
        # Modelo Gemini
        try:
            # Obtener o crear instancia del modelo
            if model_name not in self.model_instances:
                self.model_instances[model_name] = genai.GenerativeModel(model_name)
                print(f"✓ Instancia creada para modelo: {model_name}")
            
            self.model = self.model_instances[model_name]
            self.current_model_name = model_name
            
            # Inicializar tracking de cuota si no existe
            if model_name not in self.model_quota_status:
                self.model_quota_status[model_name] = {
                    "exceeded": False,
                    "reset_time": None,
                    "request_count": 0,
                    "available": True,
                    "provider": "gemini"
                }
            
            return True
        except Exception as e:
            print(f"❌ Error al cambiar a modelo {model_name}: {e}")
            return False
    
    def _load_knowledge_base(self) -> str:
        """Cargar la base de conocimiento desde el archivo markdown"""
        # Lista de posibles rutas donde puede estar el archivo
        possible_paths = [
            self.knowledge_base_path,  # Ruta original
            Path(__file__).parent.parent / "Base_Conocimiento_GEA.md",  # Desde backend/ hacia raíz
            Path(__file__).parent / "Base_Conocimiento_GEA.md",  # En backend/
            Path.cwd() / "Base_Conocimiento_GEA.md",  # Directorio de trabajo actual
            Path.cwd().parent / "Base_Conocimiento_GEA.md",  # Un nivel arriba del cwd
        ]
        
        # Si estamos en backend/, también buscar en la raíz
        if Path.cwd().name == "backend":
            possible_paths.append(Path.cwd().parent / "Base_Conocimiento_GEA.md")
        else:
            # Si estamos en la raíz, buscar directamente
            possible_paths.append(Path.cwd() / "Base_Conocimiento_GEA.md")
        
        try:
            for path in possible_paths:
                if path.exists():
                    print(f"✅ Base de conocimiento encontrada en: {path}")
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if content:
                            return content
            
            # Si no se encontró en ninguna ruta
            print("⚠️  Advertencia: No se encontró Base_Conocimiento_GEA.md en ninguna ubicación esperada")
            print(f"   Directorio actual: {Path.cwd()}")
            print(f"   Archivo actual: {__file__}")
            print(f"   Rutas buscadas:")
            for path in possible_paths:
                print(f"     - {path}")
            return ""
        except Exception as e:
            print(f"❌ Error cargando base de conocimiento: {e}")
            import traceback
            traceback.print_exc()
            return ""
    
    def is_ready(self) -> bool:
        """Verificar si el asistente está listo"""
        return self._ready and len(self.knowledge_base) > 0
    
    def process_message(self, message: str, conversation_id: Optional[str] = None) -> Dict:
        """
        Procesar un mensaje del usuario y generar una respuesta usando Gemini
        Incluye el historial de conversación para mantener el contexto
        Implementa cache y rate limiting para evitar exceder cuotas
        """
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        
        # Obtener el historial de conversación existente (antes de agregar el nuevo mensaje)
        conversation_history = self.conversations.get(conversation_id, [])
        
        # Verificar cache primero (solo para preguntas sin historial para mantener contexto)
        cache_key = self._generate_cache_key(message, conversation_history)
        cached_response = self._get_cached_response(cache_key)
        if cached_response:
            print("✅ Respuesta obtenida del cache (evitando llamada a Gemini)")
            response = cached_response
        else:
            response = None  # Inicializar response
            
            # Verificar si la cuota del modelo actual está excedida PRIMERO
            current_model_quota = self.model_quota_status.get(self.current_model_name or "", {})
            if current_model_quota.get("exceeded", False):
                reset_time = current_model_quota.get("reset_time")
                if reset_time and datetime.now() < reset_time:
                    # Intentar cambiar a otro modelo disponible
                    print(f"⚠️  Cuota del modelo {self.current_model_name} excedida. Intentando cambiar de modelo...")
                    next_model = self._select_best_available_model()
                    
                    if next_model and next_model != self.current_model_name:
                        print(f"🔄 Cambiando automáticamente a modelo: {next_model}")
                        self._switch_model(next_model)
                        # Continuar con el flujo normal usando el nuevo modelo
                    else:
                        # No hay otros modelos disponibles, mostrar mensaje
                        remaining = (reset_time - datetime.now()).total_seconds()
                        remaining_hours = int(remaining // 3600)
                        remaining_minutes = int((remaining % 3600) // 60)
                        print(f"⚠️  Todos los modelos tienen cuota excedida. Informando al usuario. Reintentar en {remaining_hours}h {remaining_minutes}m")
                        response = self._get_quota_exceeded_message(remaining_hours, remaining_minutes)
                else:
                    # Resetear el flag del modelo después del tiempo de espera
                    current_model_quota["exceeded"] = False
                    current_model_quota["reset_time"] = None
                    print(f"✅ Cuota del modelo {self.current_model_name} reseteada, intentando nuevamente")
                    # Continuar con el flujo normal después de resetear (response sigue siendo None)
            
            # Verificar si la cuota está excedida (compatibilidad con código anterior)
            if self.quota_exceeded:
                if self.quota_reset_time and datetime.now() < self.quota_reset_time:
                    # Intentar cambiar de modelo primero
                    next_model = self._select_best_available_model()
                    if next_model and next_model != self.current_model_name:
                        print(f"🔄 Cambiando automáticamente a modelo: {next_model}")
                        self._switch_model(next_model)
                        self.quota_exceeded = False  # Resetear flag global
                    else:
                        # No hay otros modelos, mostrar mensaje
                        remaining = (self.quota_reset_time - datetime.now()).total_seconds()
                        remaining_hours = int(remaining // 3600)
                        remaining_minutes = int((remaining % 3600) // 60)
                        response = self._get_quota_exceeded_message(remaining_hours, remaining_minutes)
                else:
                    # Resetear el flag después del tiempo de espera
                    self.quota_exceeded = False
                    self.quota_reset_time = None
                    print("✅ Cuota de Gemini reseteada, intentando nuevamente")
            
            # Si después de verificar cuota, aún está excedida, ya tenemos response
            if response is not None:
                pass  # Ya se asignó response arriba
            # Si Gemini no está disponible (pero no por cuota), usar método de fallback
            elif not self._ready or not self.model:
                print("⚠️  Gemini no disponible, usando método de fallback")
                response = self._find_answer_fallback(message)
            else:
                # Rate limiting: esperar mínimo 1 segundo entre requests
                current_time = time.time()
                time_since_last = current_time - self.last_request_time
                if time_since_last < self.min_request_interval:
                    wait_time = self.min_request_interval - time_since_last
                    print(f"⏳ Rate limiting: esperando {wait_time:.2f}s antes de la siguiente request")
                    time.sleep(wait_time)
                
                # Usar Gemini para generar respuesta con el historial
                try:
                    self.last_request_time = time.time()
                    
                    # Incrementar contador de requests del modelo actual
                    if self.current_model_name:
                        if self.current_model_name not in self.model_quota_status:
                            self.model_quota_status[self.current_model_name] = {
                                "exceeded": False,
                                "reset_time": None,
                                "request_count": 0
                            }
                        self.model_quota_status[self.current_model_name]["request_count"] += 1
                    
                    response = self._generate_with_gemini(message, conversation_id, conversation_history)
                    # Guardar en cache si fue exitoso
                    self._cache_response(cache_key, response)
                except Exception as e:
                    error_str = str(e)
                    # Detectar error 429 (quota exceeded)
                    if "429" in error_str or "quota" in error_str.lower() or "Quota exceeded" in error_str:
                        print(f"❌ Cuota del modelo {self.current_model_name} excedida: {error_str[:200]}")
                        
                        # Marcar el modelo actual como excedido
                        if self.current_model_name:
                            self.model_quota_status[self.current_model_name] = {
                                "exceeded": True,
                                "reset_time": datetime.now() + timedelta(hours=24),
                                "request_count": self.model_quota_status.get(self.current_model_name, {}).get("request_count", 0)
                            }
                        
                        # Intentar cambiar automáticamente a otro modelo
                        print(f"🔄 Intentando cambiar automáticamente de modelo...")
                        next_model = self._select_best_available_model()
                        
                        if next_model and next_model != self.current_model_name:
                            print(f"✅ Cambiado automáticamente a: {next_model}")
                            self._switch_model(next_model)
                            # Intentar de nuevo con el nuevo modelo
                            try:
                                response = self._generate_with_gemini(message, conversation_id, conversation_history)
                                self._cache_response(cache_key, response)
                                print(f"✅ Respuesta generada exitosamente con modelo: {self.current_model_name}")
                            except Exception as e2:
                                # Si el nuevo modelo también falla, mostrar mensaje
                                print(f"❌ El modelo alternativo también falló: {e2}")
                                remaining_hours = 24
                                remaining_minutes = 0
                                response = self._get_quota_exceeded_message(remaining_hours, remaining_minutes)
                        else:
                            # No hay otros modelos disponibles
                            self.quota_exceeded = True
                            self.quota_reset_time = datetime.now() + timedelta(hours=24)
                            print("⚠️  Todos los modelos tienen cuota excedida.")
                            remaining_hours = 24
                            remaining_minutes = 0
                            response = self._get_quota_exceeded_message(remaining_hours, remaining_minutes)
                    # Detectar errores relacionados con tokens
                    elif "token" in error_str.lower() or "too many tokens" in error_str.lower() or "context length" in error_str.lower():
                        print(f"❌ Error de tokens con Gemini: {error_str[:200]}")
                        response = self._get_token_error_message()
                    else:
                        print(f"⚠️  Error con Gemini: {error_str[:200]}, usando método de fallback")
                        response = self._find_answer_fallback(message)
        
        # Generar sugerencias relacionadas
        suggestions = self._generate_suggestions(message.lower())
        
        # Guardar en el historial de conversación
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        
        self.conversations[conversation_id].append({
            "user": message,
            "assistant": response
        })
        
        return {
            "response": response,
            "conversation_id": conversation_id,
            "suggestions": suggestions
        }
    
    def _generate_with_openai(self, question: str, conversation_id: str, conversation_history: List[Dict]) -> str:
        """
        Generar respuesta usando OpenAI con la base de conocimiento y el historial de conversación como contexto
        """
        if not self.openai_client:
            return self._find_answer_fallback(question)
        
        try:
            # Extraer nombre del modelo (sin prefijo "openai:")
            model_name = self.current_model_name.replace("openai:", "")
            
            # Construir el historial de conversación
            history_text = self._build_conversation_history(conversation_history)
            
            # Limitar base de conocimiento (OpenAI tiene límite de ~4k tokens para 3.5-turbo)
            max_context_chars = 12000  # Aproximadamente 3000 tokens
            prompt_base_chars = 1000
            history_chars = len(history_text)
            question_chars = len(question)
            reserved_chars = prompt_base_chars + history_chars + question_chars + 500
            available_kb_chars = max(4000, max_context_chars - reserved_chars)
            kb_snippet = self.knowledge_base[:int(available_kb_chars)]
            
            # Construir mensajes para OpenAI
            messages = [
                {
                    "role": "system",
                    "content": f"""Eres un asistente experto del sistema GEA (Sistema de Gestión de IMPROTECSA).

Tienes acceso a la siguiente base de conocimiento sobre GEA:

{kb_snippet}

INSTRUCCIONES IMPORTANTES:
1. Responde ÚNICAMENTE basándote en la información proporcionada en la base de conocimiento.
2. Si la pregunta del usuario NO está relacionada con GEA o NO encuentras información específica en la base de conocimiento, DEBES responder honestamente diciendo que no tienes esa información en tu conocimiento actual.
3. NO inventes información que no esté en la base de conocimiento.
4. NO asumas o supongas detalles que no están explícitamente mencionados.
5. Si la pregunta es sobre un procedimiento que SÍ está en la base de conocimiento, proporciona los pasos de manera ordenada y clara.
6. Si no tienes la información, puedes ofrecer ayuda sobre temas relacionados que SÍ conozcas de la base de conocimiento.
7. Ten en cuenta el contexto de la conversación anterior para responder de forma coherente y mantener la continuidad.

Responde en español, de forma amigable y honesta. Mantén la coherencia con el contexto de la conversación anterior. Si no tienes la información, dilo claramente."""
                }
            ]
            
            # Agregar historial
            for turn in conversation_history[-5:]:  # Últimos 5 turnos
                messages.append({"role": "user", "content": turn.get("user", "")})
                messages.append({"role": "assistant", "content": turn.get("assistant", "")})
            
            # Agregar pregunta actual
            messages.append({"role": "user", "content": question})
            
            # Generar respuesta
            response = self.openai_client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.3,
                max_tokens=1000
            )
            
            if response and response.choices and len(response.choices) > 0:
                answer = response.choices[0].message.content.strip()
                answer = self._validate_response(answer, question)
                return answer
            else:
                return self._get_unknown_response(question)
                
        except Exception as e:
            error_str = str(e)
            print(f"Error al generar respuesta con OpenAI: {error_str[:150]}")
            # Detectar error de cuota
            if "429" in error_str or "quota" in error_str.lower() or "rate limit" in error_str.lower():
                raise e  # Re-lanzar para que se maneje en process_message
            else:
                return self._find_answer_fallback(question)
    
    def _generate_with_gemini(self, question: str, conversation_id: str, conversation_history: List[Dict]) -> str:
        """
        Generar respuesta usando Gemini u OpenAI con la base de conocimiento y el historial de conversación como contexto
        """
        # Si es modelo OpenAI, usar método diferente
        if self.current_model_name and self.current_model_name.startswith("openai:"):
            return self._generate_with_openai(question, conversation_id, conversation_history)
        
        try:
            # Construir el historial de conversación en formato de texto
            history_text = self._build_conversation_history(conversation_history)
            
            # Calcular espacio disponible para la base de conocimiento
            # Estimación: ~4 caracteres por token, límite de contexto ~30k tokens para gemini-2.5-flash
            # Reservamos espacio para el prompt base, historial y pregunta
            max_context_chars = 30000 * 4  # Aproximadamente 120k caracteres
            prompt_base_chars = 1000  # Instrucciones y estructura del prompt
            history_chars = len(history_text)
            question_chars = len(question)
            reserved_chars = prompt_base_chars + history_chars + question_chars + 2000  # Buffer de seguridad
            
            # Limitar base de conocimiento según espacio disponible
            available_kb_chars = max(8000, max_context_chars - reserved_chars)
            kb_snippet = self.knowledge_base[:int(available_kb_chars)]
            
            # Construir el prompt con historial y base de conocimiento
            if history_text:
                prompt = f"""Eres un asistente experto del sistema GEA (Sistema de Gestión de IMPROTECSA).

Tienes acceso a la siguiente base de conocimiento sobre GEA:

{kb_snippet}

INSTRUCCIONES IMPORTANTES:
1. Responde ÚNICAMENTE basándote en la información proporcionada en la base de conocimiento.
2. Si la pregunta del usuario NO está relacionada con GEA o NO encuentras información específica en la base de conocimiento, DEBES responder honestamente diciendo que no tienes esa información en tu conocimiento actual.
3. NO inventes información que no esté en la base de conocimiento.
4. NO asumas o supongas detalles que no están explícitamente mencionados.
5. Si la pregunta es sobre un procedimiento que SÍ está en la base de conocimiento, proporciona los pasos de manera ordenada y clara.
6. Si no tienes la información, puedes ofrecer ayuda sobre temas relacionados que SÍ conozcas de la base de conocimiento.
7. Ten en cuenta el contexto de la conversación anterior para responder de forma coherente y mantener la continuidad.

HISTORIAL DE LA CONVERSACIÓN:
{history_text}

Pregunta actual del usuario: {question}

Responde en español, de forma amigable y honesta. Mantén la coherencia con el contexto de la conversación anterior. Si no tienes la información, dilo claramente:"""
            else:
                # Primera pregunta de la conversación (sin historial)
                prompt = f"""Eres un asistente experto del sistema GEA (Sistema de Gestión de IMPROTECSA).

Tienes acceso a la siguiente base de conocimiento sobre GEA:

{kb_snippet}

INSTRUCCIONES IMPORTANTES:
1. Responde ÚNICAMENTE basándote en la información proporcionada en la base de conocimiento.
2. Si la pregunta del usuario NO está relacionada con GEA o NO encuentras información específica en la base de conocimiento, DEBES responder honestamente diciendo que no tienes esa información en tu conocimiento actual.
3. NO inventes información que no esté en la base de conocimiento.
4. NO asumas o supongas detalles que no están explícitamente mencionados.
5. Si la pregunta es sobre un procedimiento que SÍ está en la base de conocimiento, proporciona los pasos de manera ordenada y clara.
6. Si no tienes la información, puedes ofrecer ayuda sobre temas relacionados que SÍ conozcas de la base de conocimiento.

Pregunta del usuario: {question}

Responde en español, de forma amigable y honesta. Si no tienes la información, dilo claramente:"""
            
            # Generar respuesta con Gemini
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.3,  # Baja temperatura para respuestas más precisas
                    "top_p": 0.8,
                    "top_k": 40,
                }
            )
            
            if response and response.text:
                answer = response.text.strip()
                # Validar que la respuesta no sea demasiado genérica o inventada
                answer = self._validate_response(answer, question)
                return answer
            else:
                return self._get_unknown_response(question)
                
        except Exception as e:
            error_str = str(e)
            # Detectar error 429 (quota exceeded) específicamente
            if "429" in error_str or "quota" in error_str.lower() or "Quota exceeded" in error_str:
                print(f"❌ Error 429 - Cuota excedida: {error_str[:150]}")
                # Re-lanzar para que se maneje en process_message
                raise e
            else:
                print(f"Error al generar respuesta con Gemini: {error_str[:150]}")
                # Fallback al método anterior
                return self._find_answer_fallback(question)
    
    def _build_conversation_history(self, conversation_history: List[Dict], max_turns: int = 10) -> str:
        """
        Construir el texto del historial de conversación para incluir en el prompt
        Limita el número de turnos para no exceder límites de contexto
        """
        if not conversation_history:
            return ""
        
        # Tomar solo los últimos N turnos para mantener el contexto relevante
        recent_history = conversation_history[-max_turns:] if len(conversation_history) > max_turns else conversation_history
        
        history_lines = []
        for turn in recent_history:
            user_msg = turn.get("user", "")
            assistant_msg = turn.get("assistant", "")
            
            if user_msg:
                history_lines.append(f"Usuario: {user_msg}")
            if assistant_msg:
                # Truncar respuestas muy largas del asistente para ahorrar tokens
                max_assistant_length = 500
                if len(assistant_msg) > max_assistant_length:
                    assistant_msg = assistant_msg[:max_assistant_length] + "..."
                history_lines.append(f"Asistente: {assistant_msg}")
            history_lines.append("")  # Línea en blanco entre turnos
        
        return "\n".join(history_lines)
    
    def _validate_response(self, response: str, question: str) -> str:
        """Validar que la respuesta sea apropiada y no inventada"""
        response_lower = response.lower()
        question_lower = question.lower()
        
        # Palabras que indican que la respuesta es honesta sobre no saber
        honest_indicators = [
            "no tengo", "no encuentro", "no está en", "no dispongo",
            "no tengo información", "no conozco", "no sé", "no está disponible",
            "no puedo ayudarte con eso", "no tengo datos", "no está en mi conocimiento"
        ]
        
        # Si la respuesta ya indica honestamente que no sabe, está bien
        if any(indicator in response_lower for indicator in honest_indicators):
            return response
        
        # Verificar si hay palabras clave de la pregunta en la respuesta
        # Si no hay relación, probablemente la respuesta no es relevante
        question_keywords = self._extract_keywords(question_lower)
        response_keywords = self._extract_keywords(response_lower)
        
        # Si hay muy pocas palabras clave en común, la respuesta podría no ser relevante
        common_keywords = set(question_keywords) & set(response_keywords)
        
        # Si la respuesta es muy corta o genérica, podría no ser útil
        if len(response) < 50:
            # Respuestas muy cortas podrían ser evasivas
            if not any(indicator in response_lower for indicator in honest_indicators):
                return self._get_unknown_response(question)
        
        # Si no hay palabras clave en común y la respuesta no menciona que no sabe
        if len(common_keywords) == 0 and len(question_keywords) > 0:
            # Verificar si la respuesta parece inventada (no menciona GEA o términos relacionados)
            gea_terms = ['gea', 'sistema', 'módulo', 'proceso', 'tarea', 'usuario', 'perfil']
            if not any(term in response_lower for term in gea_terms):
                return self._get_unknown_response(question)
        
        return response
    
    def _get_unknown_response(self, question: str) -> str:
        """Generar respuesta cuando no se tiene información sobre la pregunta"""
        # Intentar buscar información relacionada
        keywords = self._extract_keywords(question.lower())
        related_sections = self._search_sections(keywords)
        
        response = f"""Lo siento, no tengo información específica sobre "{question}" en mi base de conocimiento actual sobre GEA.

"""
        
        if related_sections:
            response += "Sin embargo, puedo ayudarte con temas relacionados:\n\n"
            for section_title, _, _ in related_sections[:3]:
                response += f"- {section_title}\n"
            response += "\n"
        
        response += """¿Te gustaría que te ayude con alguno de estos temas, o tienes otra pregunta sobre GEA?

Puedes preguntarme sobre:
- Módulos del sistema (Tareas, Procesos, Informes, Seguridad, etc.)
- Procedimientos paso a paso
- Configuración y parametrización
- Gestión de usuarios y permisos"""
        
        return response
    
    def _find_answer_fallback(self, question: str) -> str:
        """
        Método de fallback: buscar respuesta en la base de conocimiento sin Gemini
        """
        normalized_message = question.lower().strip()
        keywords = self._extract_keywords(normalized_message)
        relevant_sections = self._search_sections(keywords)
        
        if not relevant_sections:
            return self._get_default_response()
        
        response = self._build_response(relevant_sections, normalized_message)
        return response
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extraer palabras clave del texto"""
        stop_words = {
            'como', 'que', 'cual', 'donde', 'cuando', 'por', 'para', 'con', 'de', 'la', 'el', 'los', 'las',
            'un', 'una', 'unos', 'unas', 'es', 'son', 'está', 'están', 'tengo', 'tiene', 'hacer', 'hacerlo',
            'puedo', 'puede', 'quiero', 'necesito', 'ayuda', 'ayudar', 'me', 'te', 'se', 'nos', 'os'
        }
        
        words = re.findall(r'\b\w+\b', text.lower())
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        
        return keywords
    
    def _search_sections(self, keywords: List[str]) -> List[Tuple[str, str, int]]:
        """Buscar secciones relevantes en la base de conocimiento"""
        sections = []
        lines = self.knowledge_base.split('\n')
        
        current_section = ""
        current_content = []
        in_section = False
        
        for line in lines:
            if line.startswith('##'):
                if in_section and current_content:
                    relevance = self._calculate_relevance(' '.join(current_content), keywords)
                    if relevance > 0:
                        sections.append((current_section, '\n'.join(current_content), relevance))
                
                current_section = line.strip('#').strip()
                current_content = [line]
                in_section = True
            elif in_section:
                current_content.append(line)
        
        if in_section and current_content:
            relevance = self._calculate_relevance(' '.join(current_content), keywords)
            if relevance > 0:
                sections.append((current_section, '\n'.join(current_content), relevance))
        
        sections.sort(key=lambda x: x[2], reverse=True)
        return sections[:3]
    
    def _calculate_relevance(self, text: str, keywords: List[str]) -> int:
        """Calcular relevancia de un texto basado en keywords"""
        text_lower = text.lower()
        relevance = 0
        
        for keyword in keywords:
            count = text_lower.count(keyword)
            relevance += count * (3 if len(keyword) > 4 else 2)
        
        return relevance
    
    def _build_response(self, sections: List[Tuple[str, str, int]], question: str) -> str:
        """Construir una respuesta basada en las secciones relevantes"""
        response_parts = []
        
        if any(word in question for word in ['como', 'pasos', 'procedimiento', 'tarea']):
            response_parts.append("Te guío paso a paso:\n\n")
            for section_title, content, _ in sections:
                steps = re.findall(r'(\d+\.\s+[^\n]+)', content)
                if steps:
                    response_parts.append(f"**{section_title}**\n\n")
                    for step in steps[:10]:
                        response_parts.append(f"{step}\n")
                    response_parts.append("\n")
        else:
            for section_title, content, _ in sections:
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.strip().startswith('#')]
                
                if paragraphs:
                    response_parts.append(f"**{section_title}**\n\n")
                    for para in paragraphs[:3]:
                        if len(para) > 50:
                            response_parts.append(f"{para}\n\n")
        
        if not response_parts:
            if sections:
                _, content, _ = sections[0]
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and len(p.strip()) > 50]
                if paragraphs:
                    response_parts.append(paragraphs[0])
        
        response = ''.join(response_parts)
        
        if len(response) > 2000:
            response = response[:2000] + "\n\n... (respuesta truncada, puedes preguntar más detalles)"
        
        return response.strip() if response.strip() else self._get_default_response()
    
    def _get_default_response(self) -> str:
        """Respuesta por defecto cuando no se encuentra información específica"""
        return """No tengo información específica sobre tu pregunta en mi base de conocimiento actual sobre GEA.

Sin embargo, puedo ayudarte con los siguientes temas que sí están en mi conocimiento:

- **Módulos de GEA**: Tareas, Procesos, Informes, Mapas, Parámetros, Tableros
- **Procedimientos**: Crear usuarios, asignar permisos, gestionar tareas
- **Funcionalidades**: Configuración, seguridad, parametrización

¿Sobre qué aspecto de GEA te gustaría saber más? Puedes preguntarme cosas como:
- "¿Cómo creo un nuevo usuario?"
- "¿Qué son las tareas pendientes?"
- "¿Cómo asigno permisos a un perfil?"
"""
    
    def _get_quota_exceeded_message(self, hours: int = 24, minutes: int = 0) -> str:
        """
        Generar mensaje claro cuando la cuota de Gemini está excedida
        """
        time_str = ""
        if hours > 0:
            time_str = f"{hours} hora{'s' if hours > 1 else ''}"
        if minutes > 0:
            if time_str:
                time_str += f" y {minutes} minuto{'s' if minutes > 1 else ''}"
            else:
                time_str = f"{minutes} minuto{'s' if minutes > 1 else ''}"
        
        if not time_str:
            time_str = "aproximadamente 24 horas"
        
        return f"""⚠️ **Cuota de API Excedida**

Lo siento, he alcanzado el límite diario de solicitudes de la API de Gemini (plan gratuito: 20 requests/día).

**¿Qué significa esto?**
- He usado todas las solicitudes disponibles para hoy
- El límite se resetea automáticamente cada 24 horas
- Podrás usar el asistente nuevamente en: **{time_str}**

**Opciones disponibles:**
1. **Esperar**: El límite se resetea automáticamente mañana
2. **Revisar uso**: Visita https://ai.dev/usage?tab=rate-limit para ver tu uso actual
3. **Considerar upgrade**: Si necesitas más requests, considera un plan de pago en https://ai.google.dev/pricing

**Nota**: El sistema usa un cache inteligente para minimizar el uso de la API. Las preguntas repetidas no consumen requests adicionales.

¿Necesitas ayuda con algo más mientras tanto?"""
    
    def _get_token_error_message(self) -> str:
        """
        Generar mensaje cuando hay un error relacionado con tokens/contexto
        """
        return """⚠️ **Error de Límite de Tokens**

Lo siento, la consulta es demasiado extensa o compleja para procesarla con el modelo actual.

**¿Qué significa esto?**
- El historial de conversación o la consulta exceden el límite de tokens permitidos
- Esto puede suceder con conversaciones muy largas o preguntas muy complejas

**Soluciones:**
1. **Simplificar la pregunta**: Haz preguntas más específicas y cortas
2. **Iniciar nueva conversación**: Comienza una nueva conversación para limpiar el historial
3. **Dividir la consulta**: Si necesitas información amplia, haz varias preguntas específicas

**Tip**: Puedes limpiar la conversación usando el botón "Limpiar conversación" en la interfaz.

¿Puedo ayudarte con alguna pregunta más específica sobre GEA?"""
    
    def _generate_suggestions(self, question: str) -> List[str]:
        """Generar sugerencias de preguntas relacionadas"""
        suggestions = []
        
        if any(word in question for word in ['usuario', 'user', 'crear usuario']):
            suggestions = [
                "¿Cómo asigno un perfil a un usuario?",
                "¿Cómo gestiono los permisos de usuario?",
                "¿Qué es un perfil en GEA?"
            ]
        elif any(word in question for word in ['tarea', 'task', 'pendiente']):
            suggestions = [
                "¿Cómo veo mis tareas pendientes?",
                "¿Qué son las tareas en proceso?",
                "¿Cómo inicio un nuevo proceso?"
            ]
        elif any(word in question for word in ['proceso', 'process', 'flujo']):
            suggestions = [
                "¿Cómo asigno procesos a un usuario?",
                "¿Qué es un flujo de trabajo?",
                "¿Cómo diseño un proceso?"
            ]
        elif any(word in question for word in ['permiso', 'perfil', 'seguridad']):
            suggestions = [
                "¿Cómo creo un nuevo perfil?",
                "¿Cómo asigno permisos a un perfil?",
                "¿Qué módulos tiene el sistema de seguridad?"
            ]
        else:
            suggestions = [
                "¿Cómo inicio sesión en GEA?",
                "¿Qué módulos tiene GEA?",
                "¿Cómo creo un nuevo usuario?",
                "¿Cómo veo mis tareas pendientes?"
            ]
        
        return suggestions[:3]
    
    def get_suggestions(self) -> List[str]:
        """Obtener sugerencias de preguntas comunes"""
        return [
            "¿Cómo creo un nuevo usuario?",
            "¿Cómo asigno permisos a un perfil?",
            "¿Qué son las tareas pendientes?",
            "¿Cómo inicio un nuevo proceso?",
            "¿Qué módulos tiene GEA?",
            "¿Cómo gestiono las tareas en proceso?",
            "¿Cómo creo un informe personalizado?",
            "¿Qué es un flujo de trabajo?"
        ]
    
    def _generate_cache_key(self, question: str, conversation_history: List[Dict]) -> str:
        """
        Generar una clave única para el cache basada en la pregunta
        Solo usa la pregunta actual (no el historial completo) para cache más efectivo
        """
        # Normalizar la pregunta
        normalized = question.lower().strip()
        # Crear hash de la pregunta
        cache_key = hashlib.md5(normalized.encode('utf-8')).hexdigest()
        return f"cache_{cache_key}"
    
    def _get_cached_response(self, cache_key: str) -> Optional[str]:
        """
        Obtener respuesta del cache si existe y no ha expirado
        """
        if cache_key in self.response_cache:
            cached_data = self.response_cache[cache_key]
            # Verificar si el cache no ha expirado
            if datetime.now() < cached_data['expires_at']:
                print(f"✅ Cache hit para: {cache_key[:20]}...")
                return cached_data['response']
            else:
                # Eliminar cache expirado
                del self.response_cache[cache_key]
        return None
    
    def _cache_response(self, cache_key: str, response: str):
        """
        Guardar respuesta en el cache con TTL
        """
        expires_at = datetime.now() + timedelta(seconds=self.cache_ttl)
        self.response_cache[cache_key] = {
            'response': response,
            'expires_at': expires_at,
            'created_at': datetime.now()
        }
        print(f"💾 Respuesta guardada en cache: {cache_key[:20]}...")
        
        # Limpiar cache expirado periódicamente (cada 100 entradas)
        if len(self.response_cache) > 100:
            self._clean_expired_cache()
    
    def _clean_expired_cache(self):
        """Limpiar entradas expiradas del cache"""
        now = datetime.now()
        expired_keys = [
            key for key, data in self.response_cache.items()
            if now >= data['expires_at']
        ]
        for key in expired_keys:
            del self.response_cache[key]
        if expired_keys:
            print(f"🧹 Limpiadas {len(expired_keys)} entradas expiradas del cache")
    
    def get_available_models(self) -> List[str]:
        """Obtener lista de modelos disponibles"""
        return self.available_models.copy()
    
    def get_current_model(self) -> Optional[str]:
        """Obtener el modelo actualmente en uso"""
        return self.current_model_name
    
    def get_model_status(self) -> Dict:
        """Obtener estado de todos los modelos incluyendo cuotas (solo disponibles)"""
        # Filtrar solo modelos disponibles
        available_working_models = [
            m for m in self.available_models 
            if self.model_quota_status.get(m, {}).get("available", False)
        ]
        
        # Debug: verificar modelos OpenAI
        all_openai_models = [m for m in self.available_models if m.startswith("openai:")]
        openai_models_in_list = [m for m in available_working_models if m.startswith("openai:")]
        
        if all_openai_models:
            print(f"🔍 Debug: Total modelos OpenAI en available_models: {all_openai_models}")
            for om in all_openai_models:
                om_status = self.model_quota_status.get(om, {})
                print(f"   - {om}: available={om_status.get('available', False)}, status={om_status}")
        
        if openai_models_in_list:
            print(f"🔍 Debug: Modelos OpenAI en lista disponible: {openai_models_in_list}")
        elif all_openai_models:
            print(f"⚠️  Debug: Modelos OpenAI encontrados pero NO en lista disponible. Revisando...")
        
        status = {
            "current_model": self.current_model_name,
            "available_models": available_working_models,  # Solo los que funcionan
            "all_models": self.available_models,  # Todos los encontrados (incluidos no disponibles)
            "models_quota_status": {}
        }
        
        # Solo incluir modelos disponibles en el status
        for model_name in available_working_models:
            quota_info = self.model_quota_status.get(model_name, {
                "exceeded": False,
                "reset_time": None,
                "request_count": 0,
                "available": False
            })
            
            # Calcular tiempo restante si está excedido
            remaining_time = None
            if quota_info.get("exceeded") and quota_info.get("reset_time"):
                remaining = (quota_info["reset_time"] - datetime.now()).total_seconds()
                if remaining > 0:
                    remaining_hours = int(remaining // 3600)
                    remaining_minutes = int((remaining % 3600) // 60)
                    remaining_time = {
                        "hours": remaining_hours,
                        "minutes": remaining_minutes,
                        "total_seconds": int(remaining)
                    }
            
            status["models_quota_status"][model_name] = {
                "exceeded": quota_info.get("exceeded", False),
                "request_count": quota_info.get("request_count", 0),
                "remaining_time": remaining_time,
                "is_current": model_name == self.current_model_name,
                "available": quota_info.get("available", False),
                "provider": quota_info.get("provider", "gemini")
            }
        
        return status
    
    def change_model(self, model_name: str) -> Dict:
        """
        Cambiar manualmente al modelo especificado
        Retorna dict con success y mensaje
        """
        if model_name not in self.available_models:
            return {
                "success": False,
                "message": f"Modelo {model_name} no está disponible. Modelos disponibles: {', '.join(self.available_models[:5])}"
            }
        
        if model_name == self.current_model_name:
            return {
                "success": True,
                "message": f"Ya estás usando el modelo {model_name}"
            }
        
        success = self._switch_model(model_name)
        if success:
            return {
                "success": True,
                "message": f"Modelo cambiado exitosamente a {model_name}",
                "current_model": self.current_model_name
            }
        else:
            return {
                "success": False,
                "message": f"Error al cambiar al modelo {model_name}"
            }

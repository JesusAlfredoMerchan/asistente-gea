from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from assistant_engine import GEAAssistant

app = FastAPI(title="Asistente GEA API", version="1.0.0")

# Configurar CORS para permitir conexiones desde React
# En producción, configura ALLOWED_ORIGINS con tu URL de Vercel
allowed_origins_str = os.getenv(
    "ALLOWED_ORIGINS", 
    "http://localhost:3000,http://localhost:5173"
)
allowed_origins = [origin.strip() for origin in allowed_origins_str.split(",") if origin.strip()]

# En desarrollo, permitir todos los orígenes. En producción, usa solo los específicos.
if os.getenv("ENVIRONMENT") != "production":
    allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar el asistente (esto mostrará los mensajes de inicialización de Gemini)
print("\n" + "="*50)
print("Inicializando Asistente GEA...")
print("="*50 + "\n")
import os
from pathlib import Path

# Determinar la ruta correcta para la base de conocimiento
# En Render: si estamos en backend/, buscar en la raíz (un nivel arriba)
# En desarrollo local: buscar relativo desde backend/
cwd = Path.cwd()
if cwd.name == "backend":
    kb_path = cwd.parent / "Base_Conocimiento_GEA.md"
else:
    kb_path = cwd / "Base_Conocimiento_GEA.md"

print(f"📁 Directorio de trabajo: {cwd}")
print(f"📄 Buscando base de conocimiento en: {kb_path}")
assistant = GEAAssistant(knowledge_base_path=str(kb_path))
print("\n" + "="*50)
print("Asistente GEA listo para recibir consultas")
print("="*50 + "\n")

class MessageRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class MessageResponse(BaseModel):
    response: str
    conversation_id: str
    suggestions: Optional[List[str]] = None

@app.get("/")
def read_root():
    return {"message": "Asistente GEA API está funcionando"}

@app.post("/api/chat", response_model=MessageResponse)
async def chat(request: MessageRequest):
    """
    Endpoint principal para interactuar con el asistente
    """
    try:
        response_data = assistant.process_message(
            request.message, 
            request.conversation_id
        )
        return MessageResponse(**response_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/models")
async def get_models():
    """
    Obtener información sobre modelos disponibles y estado
    """
    try:
        status = assistant.get_model_status()
        # Debug en el endpoint
        all_models = status.get("available_models", [])
        openai_models = [m for m in all_models if m.startswith("openai:")]
        gemini_models = [m for m in all_models if not m.startswith("openai:")]
        
        print(f"📡 API /api/models llamado:")
        print(f"   - Total modelos en respuesta: {len(all_models)}")
        print(f"   - Modelos OpenAI: {openai_models}")
        print(f"   - Modelos Gemini: {len(gemini_models)}")
        
        if not openai_models:
            print(f"   ⚠️  WARNING: No se encontraron modelos OpenAI en la respuesta!")
            # Verificar directamente en el assistant
            all_available = assistant.get_available_models()
            openai_in_assistant = [m for m in all_available if m.startswith("openai:")]
            if openai_in_assistant:
                print(f"   🔍 Pero OpenAI está en assistant.available_models: {openai_in_assistant}")
                # Usar método público para verificar estado
                model_status_dict = assistant.get_model_status()
                for om in openai_in_assistant:
                    quota_info = model_status_dict.get("models_quota_status", {}).get(om, {})
                    print(f"      - {om}: available={quota_info.get('available', False)}")
        
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/models/change")
async def change_model(request: dict):
    """
    Cambiar el modelo actual manualmente
    Body: {"model_name": "gemini-2.0-flash-exp"}
    """
    try:
        model_name = request.get("model_name")
        if not model_name:
            raise HTTPException(status_code=400, detail="model_name es requerido")
        
        result = assistant.change_model(model_name)
        if result["success"]:
            return result
        else:
            raise HTTPException(status_code=400, detail=result["message"])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/suggestions")
async def get_suggestions():
    """
    Obtener sugerencias de preguntas comunes
    """
    suggestions = assistant.get_suggestions()
    return {"suggestions": suggestions}

@app.get("/api/health")
async def health_check():
    """
    Verificar el estado del servicio
    """
    return {"status": "healthy", "assistant_loaded": assistant.is_ready()}


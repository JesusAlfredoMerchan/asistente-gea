# 🏗️ Arquitectura del Sistema - Asistente Inteligente GEA

## 📋 Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Stack Tecnológico](#stack-tecnológico)
4. [Componentes Principales](#componentes-principales)
5. [Flujo de Datos](#flujo-de-datos)
6. [Estructura de Directorios](#estructura-de-directorios)
7. [Patrones de Diseño](#patrones-de-diseño)
8. [Integraciones](#integraciones)
9. [Seguridad](#seguridad)
10. [Escalabilidad](#escalabilidad)

---

## 🎯 Visión General

El Asistente Inteligente GEA está construido con una arquitectura de **separación de responsabilidades** (frontend/backend), siguiendo principios de diseño modernos y mejores prácticas de desarrollo web.

### Características Arquitectónicas

- ✅ **Separación Frontend/Backend**: API REST independiente y cliente web
- ✅ **Arquitectura de Microservicios**: Servicios desacoplados y escalables
- ✅ **RESTful API**: Comunicación mediante endpoints REST estándar
- ✅ **Integración con IA**: Uso de Google Gemini AI para procesamiento de lenguaje natural
- ✅ **State Management**: Gestión de estado en el frontend con React Hooks
- ✅ **CORS**: Configuración para comunicación cross-origin

---

## 🏛️ Arquitectura del Sistema

### Diagrama de Alto Nivel

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENTE WEB                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              React + TypeScript + Vite                │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│  │  │ Chat UI  │  │ Messages │  │Suggestions│           │   │
│  │  └──────────┘  └──────────┘  └──────────┘           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTP/REST
                            │
┌─────────────────────────────────────────────────────────────┐
│                      API BACKEND (FastAPI)                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                  main.py (API Layer)                  │   │
│  │  • POST /api/chat                                     │   │
│  │  • GET /api/suggestions                               │   │
│  │  • GET /api/health                                    │   │
│  └──────────────────────────────────────────────────────┘   │
│                            │                                 │
│                            ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │          assistant_engine.py (Business Logic)         │   │
│  │  • GEAAssistant Class                                 │   │
│  │  • Procesamiento de mensajes                          │   │
│  │  • Gestión de conversaciones                          │   │
│  └──────────────────────────────────────────────────────┘   │
│                            │                                 │
│                            ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Google Gemini AI Integration              │   │
│  │  • Generación de respuestas                           │   │
│  │  • Validación de respuestas                           │   │
│  └──────────────────────────────────────────────────────┘   │
│                            │                                 │
│                            ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Base_Conocimiento_GEA.md (Knowledge Base)      │   │
│  │  • Información sobre GEA                              │   │
│  │  • Procedimientos y guías                             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Stack Tecnológico

### Frontend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **React** | 18.2.0 | Biblioteca UI para componentes interactivos |
| **TypeScript** | 5.2.2 | Tipado estático para JavaScript |
| **Vite** | 5.0.8 | Build tool y servidor de desarrollo rápido |
| **Axios** | 1.6.2 | Cliente HTTP para comunicación con API |
| **CSS3** | - | Estilos personalizados y responsive design |

### Backend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.8+ | Lenguaje de programación |
| **FastAPI** | 0.104.1 | Framework web moderno y rápido |
| **Uvicorn** | 0.24.0 | Servidor ASGI de alto rendimiento |
| **Pydantic** | 2.5.0 | Validación de datos y modelos |
| **Google Generative AI** | 0.3.2 | SDK para integración con Gemini AI |
| **python-dotenv** | 1.0.0 | Gestión de variables de entorno |

---

## 🔧 Componentes Principales

### Frontend Components

#### 1. **App.tsx** - Componente Principal
- Punto de entrada de la aplicación React
- Renderiza el header y el componente ChatInterface
- Maneja el layout general de la aplicación

#### 2. **ChatInterface.tsx** - Interfaz de Chat
**Responsabilidades:**
- Gestión del estado de mensajes
- Manejo de conversaciones (conversation_id)
- Coordinación entre componentes hijos
- Comunicación con la API

**Estados:**
- `messages`: Array de mensajes (usuario/asistente)
- `suggestions`: Sugerencias de preguntas
- `isLoading`: Estado de carga durante procesamiento
- `conversationId`: ID único de la conversación

#### 3. **MessageList.tsx** - Lista de Mensajes
- Renderiza la lista de mensajes
- Diferenciación visual entre mensajes del usuario y asistente
- Scroll automático a los nuevos mensajes

#### 4. **MessageBubble.tsx** - Burbuja de Mensaje
- Componente para renderizar un mensaje individual
- Estilos diferenciados para usuario/asistente
- Formateo de texto (markdown básico)

#### 5. **MessageInput.tsx** - Input de Mensaje
- Campo de texto para escribir mensajes
- Botón de envío
- Manejo de eventos (Enter para enviar)

#### 6. **Suggestions.tsx** - Sugerencias
- Muestra sugerencias de preguntas
- Interacción click para enviar sugerencia como mensaje

#### 7. **api.ts** - Cliente API
- Funciones para comunicación con el backend
- `sendMessage()`: Envía mensaje al asistente
- `getSuggestions()`: Obtiene sugerencias iniciales

### Backend Components

#### 1. **main.py** - API FastAPI

**Endpoints:**

```python
POST /api/chat
```
- Recibe mensajes del usuario
- Devuelve respuestas del asistente
- Incluye conversation_id y sugerencias

```python
GET /api/suggestions
```
- Retorna sugerencias de preguntas comunes

```python
GET /api/health
```
- Health check del servicio
- Verifica estado del asistente

**Middleware:**
- **CORS**: Permite conexiones desde el frontend
- **Request Validation**: Validación automática con Pydantic

#### 2. **assistant_engine.py** - Motor del Asistente

**Clase Principal: `GEAAssistant`**

**Métodos Principales:**

- `__init__()`: Inicialización del asistente
  - Carga base de conocimiento
  - Inicializa Gemini AI
  - Configura modelo de IA

- `process_message()`: Procesa mensaje del usuario
  - Genera respuesta usando Gemini o fallback
  - Genera sugerencias relacionadas
  - Guarda en historial de conversación

- `_generate_with_gemini()`: Genera respuesta con IA
  - Construye prompt con base de conocimiento
  - Llama a Gemini API
  - Valida respuesta

- `_find_answer_fallback()`: Método de fallback
  - Búsqueda de texto en base de conocimiento
  - Extracción de keywords
  - Construcción de respuesta basada en relevancia

- `_validate_response()`: Valida respuestas de IA
  - Verifica que no sea inventada
  - Asegura relevancia con la pregunta
  - Detecta respuestas honestas sobre desconocimiento

- `_generate_suggestions()`: Genera sugerencias contextuales
  - Basadas en keywords de la pregunta
  - Sugerencias relacionadas con el tema

---

## 📊 Flujo de Datos

### Flujo de una Conversación

```
1. Usuario escribe mensaje
   │
   ▼
2. MessageInput envía mensaje a ChatInterface
   │
   ▼
3. ChatInterface actualiza estado (añade mensaje usuario)
   │
   ▼
4. ChatInterface llama api.sendMessage()
   │
   ▼
5. Axios hace POST request a /api/chat
   │
   ▼
6. FastAPI recibe request en main.py
   │
   ▼
7. main.py llama assistant.process_message()
   │
   ▼
8. assistant_engine.py procesa:
   │  ├─ Carga contexto de conversación
   │  ├─ Busca en base de conocimiento
   │  ├─ Genera respuesta con Gemini AI
   │  ├─ Valida respuesta
   │  └─ Genera sugerencias
   │
   ▼
9. Respuesta vuelve a FastAPI
   │
   ▼
10. FastAPI devuelve JSON response
   │
   ▼
11. Axios recibe respuesta en frontend
   │
   ▼
12. ChatInterface actualiza estado:
    ├─ Añade mensaje del asistente
    └─ Actualiza sugerencias
   │
   ▼
13. React re-renderiza componentes
   │
   ▼
14. Usuario ve respuesta
```

### Flujo de Inicialización

```
1. Backend inicia
   │
   ▼
2. main.py importa assistant_engine
   │
   ▼
3. GEAAssistant.__init__() ejecuta:
   │  ├─ Carga Base_Conocimiento_GEA.md
   │  ├─ Inicializa Gemini AI
   │  ├─ Verifica API key
   │  └─ Carga modelo de IA
   │
   ▼
4. Backend listo para recibir requests
   │
   ▼
5. Frontend inicia
   │
   ▼
6. App.tsx monta
   │
   ▼
7. ChatInterface carga:
   │  ├─ Muestra mensaje de bienvenida
   │  └─ Carga sugerencias iniciales (GET /api/suggestions)
   │
   ▼
8. Frontend listo para usar
```

---

## 📁 Estructura de Directorios

```
asistente GEA/
│
├── backend/                          # Backend Python
│   ├── __pycache__/                  # Cache de Python
│   ├── venv/                         # Entorno virtual Python
│   ├── main.py                       # API FastAPI principal
│   ├── assistant_engine.py           # Motor del asistente
│   ├── requirements.txt              # Dependencias Python
│   ├── env.example                   # Ejemplo de variables de entorno
│   ├── .env                          # Variables de entorno (no versionado)
│   └── start-backend.bat             # Script de inicio (Windows)
│
├── frontend/                         # Frontend React
│   ├── node_modules/                 # Dependencias npm
│   ├── src/
│   │   ├── components/               # Componentes React
│   │   │   ├── ChatInterface.tsx     # Componente principal del chat
│   │   │   ├── ChatInterface.css     # Estilos del chat
│   │   │   ├── MessageList.tsx       # Lista de mensajes
│   │   │   ├── MessageList.css       # Estilos de la lista
│   │   │   ├── MessageBubble.tsx     # Burbuja individual
│   │   │   ├── MessageBubble.css     # Estilos de burbuja
│   │   │   ├── MessageInput.tsx      # Input de mensaje
│   │   │   ├── MessageInput.css      # Estilos del input
│   │   │   ├── Suggestions.tsx       # Componente de sugerencias
│   │   │   └── Suggestions.css       # Estilos de sugerencias
│   │   ├── services/
│   │   │   └── api.ts                # Cliente API
│   │   ├── types/
│   │   │   └── index.ts              # Tipos TypeScript
│   │   ├── App.tsx                   # Componente principal
│   │   ├── App.css                   # Estilos globales
│   │   ├── main.tsx                  # Punto de entrada
│   │   ├── index.css                 # Estilos base
│   │   └── vite-env.d.ts             # Tipos de Vite
│   ├── index.html                    # HTML principal
│   ├── package.json                  # Dependencias y scripts npm
│   ├── package-lock.json             # Lock file de dependencias
│   ├── tsconfig.json                 # Configuración TypeScript
│   ├── tsconfig.node.json            # Config TypeScript para Node
│   ├── vite.config.ts                # Configuración Vite
│   └── start-frontend.bat            # Script de inicio (Windows)
│
├── docs/                             # Documentación
│   ├── documentacion.md              # Documentación completa
│   ├── ARQUITECTURA.md               # Este archivo
│   └── GUIAS_USO.md                  # Guías de uso
│
├── Base_Conocimiento_GEA.md          # Base de conocimiento
├── README.md                         # README principal
├── iniciar-aplicacion.bat            # Script de inicio automático
└── detener-aplicacion.bat            # Script para detener servidores
```

---

## 🎨 Patrones de Diseño

### 1. **Separación de Responsabilidades (SoC)**

- **Frontend**: Solo UI y presentación
- **Backend**: Lógica de negocio y procesamiento
- **Base de Conocimiento**: Datos independientes del código

### 2. **API RESTful**

- Endpoints semánticos y predecibles
- Métodos HTTP estándar (GET, POST)
- Respuestas en formato JSON
- Códigos de estado HTTP apropiados

### 3. **State Management (Frontend)**

- React Hooks (`useState`, `useEffect`)
- Estado local en componentes
- Props para comunicación entre componentes

### 4. **Dependency Injection (Backend)**

- Dependencias inyectadas en `GEAAssistant`
- Configuración mediante variables de entorno
- Fácil testing y mocking

### 5. **Template Method Pattern**

- `process_message()` define el flujo
- Métodos específicos para cada paso (Gemini/fallback)

### 6. **Strategy Pattern**

- Estrategia Gemini AI vs Fallback
- Selección dinámica según disponibilidad

### 7. **Factory Pattern**

- Creación de modelos de Gemini
- Generación de UUIDs para conversaciones

---

## 🔗 Integraciones

### Google Gemini AI

**Integración:**
- SDK: `google-generativeai`
- Configuración mediante API key
- Modelo: `gemini-2.5-flash` (configurable)

**Flujo:**
1. Prompt construido con base de conocimiento
2. Llamada a `model.generate_content()`
3. Validación de respuesta
4. Fallback si falla

**Parámetros:**
```python
temperature: 0.3  # Respuestas más precisas
top_p: 0.8        # Nucleus sampling
top_k: 40         # Top-k sampling
```

### Base de Conocimiento

**Formato:** Markdown
**Estructura:**
- Secciones con `##` y `###`
- Procedimientos numerados
- Preguntas frecuentes
- Glosario

**Carga:**
- Carga al inicializar `GEAAssistant`
- Buscado en múltiples rutas
- Almacenado en memoria como string

---

## 🔒 Seguridad

### Implementaciones Actuales

1. **CORS**: Configurado para orígenes específicos
2. **Validación de Input**: Pydantic valida requests
3. **Variables de Entorno**: API keys no en código
4. **Validación de Respuestas**: Evita información inventada

### Consideraciones de Seguridad

⚠️ **No Implementado (Mejoras Futuras):**

- [ ] Autenticación de usuarios
- [ ] Rate limiting
- [ ] HTTPS/SSL
- [ ] Sanitización de input HTML
- [ ] Logging de acceso
- [ ] Encriptación de datos sensibles

### Recomendaciones

1. **Producción**: Usar HTTPS
2. **API Keys**: Rotar periódicamente
3. **CORS**: Restringir a dominios específicos
4. **Logging**: Implementar logging de seguridad
5. **Validación**: Agregar sanitización de inputs

---

## 📈 Escalabilidad

### Estado Actual

**Limitaciones:**
- Conversaciones en memoria (se pierden al reiniciar)
- Base de conocimiento en memoria
- Procesamiento síncrono

### Mejoras para Escalabilidad

#### 1. **Persistencia de Datos**

```python
# Opciones:
- Base de datos SQL (PostgreSQL, MySQL)
- Base de datos NoSQL (MongoDB, Redis)
- Almacenamiento de conversaciones
- Cache de respuestas frecuentes
```

#### 2. **Procesamiento Asíncrono**

```python
# FastAPI soporta async/await
@app.post("/api/chat")
async def chat(request: MessageRequest):
    # Procesamiento asíncrono
    response = await assistant.process_message_async(...)
```

#### 3. **Caching**

```python
# Cache de respuestas frecuentes
- Redis para cache de respuestas
- Cache de base de conocimiento procesada
- Cache de sugerencias
```

#### 4. **Load Balancing**

```
┌─────────┐
│  Nginx  │ (Load Balancer)
└────┬────┘
     │
     ├──► Backend Instance 1
     ├──► Backend Instance 2
     └──► Backend Instance 3
```

#### 5. **CDN para Frontend**

- Servir assets estáticos desde CDN
- Reducir carga en servidor

#### 6. **Microservicios**

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Chat API    │  │ Knowledge   │  │ Analytics   │
│ Service     │  │ Service     │  │ Service     │
└─────────────┘  └─────────────┘  └─────────────┘
```

### Métricas de Rendimiento

**Objetivos:**
- Tiempo de respuesta: < 2 segundos
- Disponibilidad: 99.9%
- Throughput: 100+ requests/segundo

**Monitoreo:**
- Logging estructurado
- Métricas de performance
- Alertas de errores

---

## 🔄 Ciclo de Vida de una Request

```
Request → FastAPI → CORS Middleware → Endpoint Handler
                ↓
         Validation (Pydantic)
                ↓
         Business Logic (assistant_engine)
                ↓
         AI Processing (Gemini)
                ↓
         Response Building
                ↓
         Response Validation
                ↓
Response ← JSON ← FastAPI ← Response Model
```

---

## 📝 Notas Técnicas

### Gestión de Memoria

- Base de conocimiento cargada una vez al inicio
- Conversaciones almacenadas en diccionario en memoria
- Considerar límites de memoria para muchas conversaciones

### Manejo de Errores

- Try-catch en llamadas a Gemini
- Fallback automático si Gemini falla
- Manejo de errores de red en frontend
- Mensajes de error amigables al usuario

### Testing

**Estructura recomendada:**

```
backend/
├── tests/
│   ├── test_main.py
│   ├── test_assistant_engine.py
│   └── fixtures/
└── ...

frontend/
├── src/
└── __tests__/
    ├── ChatInterface.test.tsx
    └── ...
```

---

**Última actualización**: Enero 2025


# 📚 Documentación Completa - Asistente Inteligente GEA

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Descripción del Proyecto](#descripción-del-proyecto)
3. [Características Principales](#características-principales)
4. [Instalación y Configuración](#instalación-y-configuración)
5. [Uso del Sistema](#uso-del-sistema)
6. [API Reference](#api-reference)
7. [Configuración Avanzada](#configuración-avanzada)
8. [Troubleshooting](#troubleshooting)
9. [Contribución](#contribución)
10. [Licencia y Contacto](#licencia-y-contacto)

---

## 🎯 Introducción

El **Asistente Inteligente GEA** es una aplicación web desarrollada para facilitar el uso del sistema GEA (Sistema de Gestión de IMPROTECSA S.A.S.). Esta herramienta permite a los usuarios interactuar con el sistema mediante un chat inteligente, obteniendo respuestas contextuales, guías paso a paso y soporte sin necesidad de consultar manuales extensos.

### ¿Qué es GEA?

GEA es un sistema de información de gestión basado en flujos de trabajo que permite diseñar, parametrizar y supervisar procesos de trabajo de manera eficiente. Es una plataforma 100% web desarrollada por IMPROTECSA S.A.S.

---

## 📖 Descripción del Proyecto

Este asistente inteligente está compuesto por dos componentes principales:

- **Frontend**: Interfaz de usuario moderna construida con React, TypeScript y Vite
- **Backend**: API REST construida con FastAPI (Python) que utiliza Google Gemini AI para generar respuestas inteligentes

El sistema utiliza una base de conocimiento en formato Markdown (`Base_Conocimiento_GEA.md`) que contiene toda la información sobre el sistema GEA, incluyendo módulos, procedimientos, configuraciones y preguntas frecuentes.

### Objetivos del Proyecto

- ✅ Proporcionar asistencia instantánea a usuarios de GEA
- ✅ Reducir la curva de aprendizaje del sistema
- ✅ Facilitar el acceso a información y procedimientos
- ✅ Generar respuestas contextuales basadas en la base de conocimiento
- ✅ Ofrecer una interfaz moderna y fácil de usar

---

## ✨ Características Principales

### 🗣️ Chat Interactivo

- Conversación en tiempo real con el asistente
- Mantenimiento del contexto de la conversación
- Respuestas contextuales basadas en la base de conocimiento
- Interfaz de chat moderna con burbujas de mensaje diferenciadas

### 🤖 Inteligencia Artificial

- Integración con Google Gemini AI para generar respuestas inteligentes
- Procesamiento de lenguaje natural en español
- Validación de respuestas para evitar información inventada
- Método de fallback cuando Gemini no está disponible

### 💡 Sugerencias Inteligentes

- Sugerencias de preguntas relacionadas después de cada respuesta
- Preguntas frecuentes al iniciar la conversación
- Sugerencias contextuales basadas en la pregunta del usuario

### 📱 Diseño Responsive

- Interfaz adaptable a dispositivos móviles y desktop
- Animaciones suaves y transiciones
- Diseño moderno con gradientes y colores atractivos
- Indicador de escritura mientras procesa respuestas

### 🔒 Gestión de Conversaciones

- Identificación única de conversaciones mediante UUID
- Historial de conversación persistente durante la sesión
- Soporte para múltiples conversaciones simultáneas

---

## 🚀 Instalación y Configuración

### Prerrequisitos

Antes de instalar el asistente, asegúrate de tener instalado:

- **Python 3.8 o superior**
- **Node.js 18 o superior**
- **npm o yarn**
- **Git** (opcional, para clonar el repositorio)

### Instalación Rápida (Windows)

La forma más sencilla de iniciar el proyecto es usando el script de inicio automático:

```bash
iniciar-aplicacion.bat
```

Este script automatiza:
- Verificación de Python y Node.js
- Creación del entorno virtual de Python
- Instalación de dependencias del backend
- Instalación de dependencias del frontend
- Inicio de ambos servidores

### Instalación Manual

#### Backend

1. **Navegar a la carpeta backend:**
   ```bash
   cd backend
   ```

2. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual:**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar variables de entorno:**
   - Copiar `env.example` a `.env`
   - Editar `.env` y agregar tu API key de Gemini:
     ```
     GEMINI_API_KEY=tu_api_key_aqui
     ```

6. **Ejecutar el servidor:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

#### Frontend

1. **Navegar a la carpeta frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar dependencias:**
   ```bash
   npm install
   ```

3. **Configurar variables de entorno (opcional):**
   - Crear archivo `.env` en la carpeta frontend:
     ```
     VITE_API_URL=http://localhost:8000
     ```

4. **Ejecutar en modo desarrollo:**
   ```bash
   npm run dev
   ```

### Obtener API Key de Google Gemini

1. Visita: https://makersuite.google.com/app/apikey
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API key
4. Copia la key y agrégalo al archivo `.env` del backend

**Nota**: Si no configuras la API key, el sistema funcionará con un método de fallback basado en búsqueda de texto, pero las respuestas serán menos inteligentes.

---

## 💻 Uso del Sistema

### Iniciar la Aplicación

1. **Método Automático:**
   ```bash
   iniciar-aplicacion.bat
   ```

2. **Método Manual:**
   - Abrir dos terminales
   - En la primera: iniciar el backend (ver sección Backend)
   - En la segunda: iniciar el frontend (ver sección Frontend)

### Acceder a la Interfaz

Una vez iniciados ambos servidores:

- **Frontend**: http://localhost:5173 (o el puerto que indique Vite)
- **Backend API**: http://localhost:8000
- **Documentación API**: http://localhost:8000/docs (Swagger UI)

### Usar el Chat

1. **Hacer una pregunta**: Escribe tu pregunta en el campo de texto y presiona Enter o haz clic en el botón de enviar.

2. **Ver sugerencias**: Al iniciar o después de cada respuesta, verás sugerencias de preguntas relacionadas que puedes hacer clic para preguntar rápidamente.

3. **Seguir conversando**: El asistente mantiene el contexto de la conversación, así que puedes hacer preguntas de seguimiento.

### Ejemplos de Preguntas

- "¿Cómo creo un nuevo usuario?"
- "¿Qué son las tareas pendientes?"
- "¿Cómo asigno permisos a un perfil?"
- "¿Qué módulos tiene GEA?"
- "Explícame el módulo de Procesos"
- "¿Cómo inicio un nuevo flujo de trabajo?"

### Detener la Aplicación

**Windows:**
```bash
detener-aplicacion.bat
```

**Manual:**
- Presionar `Ctrl+C` en las terminales donde están corriendo los servidores

---

## 🔌 API Reference

### Endpoints Disponibles

#### `POST /api/chat`

Envía un mensaje al asistente y recibe una respuesta.

**Request Body:**
```json
{
  "message": "¿Cómo creo un nuevo usuario?",
  "conversation_id": "opcional-uuid-de-conversacion"
}
```

**Response:**
```json
{
  "response": "Te guío paso a paso para crear un nuevo usuario...",
  "conversation_id": "uuid-de-conversacion",
  "suggestions": [
    "¿Cómo asigno un perfil a un usuario?",
    "¿Cómo gestiono los permisos de usuario?",
    "¿Qué es un perfil en GEA?"
  ]
}
```

**Status Codes:**
- `200`: Respuesta exitosa
- `500`: Error del servidor

#### `GET /api/suggestions`

Obtiene sugerencias de preguntas comunes.

**Response:**
```json
{
  "suggestions": [
    "¿Cómo creo un nuevo usuario?",
    "¿Cómo asigno permisos a un perfil?",
    "¿Qué son las tareas pendientes?",
    ...
  ]
}
```

#### `GET /api/health`

Verifica el estado del servicio.

**Response:**
```json
{
  "status": "healthy",
  "assistant_loaded": true
}
```

#### `GET /`

Endpoint de bienvenida.

**Response:**
```json
{
  "message": "Asistente GEA API está funcionando"
}
```

### Documentación Interactiva

Puedes explorar toda la API de forma interactiva visitando:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## ⚙️ Configuración Avanzada

### Variables de Entorno

#### Backend (`backend/.env`)

```env
# API Key de Google Gemini (requerido para uso completo)
GEMINI_API_KEY=tu_api_key_aqui

# Configuración opcional del servidor
HOST=0.0.0.0
PORT=8000
```

#### Frontend (`frontend/.env`)

```env
# URL del backend API
VITE_API_URL=http://localhost:8000

# Configuración opcional
VITE_APP_NAME=Asistente GEA
```

### Personalizar Base de Conocimiento

El archivo `Base_Conocimiento_GEA.md` contiene toda la información que el asistente utiliza. Para actualizar o agregar información:

1. Edita el archivo `Base_Conocimiento_GEA.md` en la raíz del proyecto
2. Reinicia el backend para que cargue los cambios
3. El formato debe ser Markdown con secciones usando `##` y `###`

### Configurar CORS

Si necesitas permitir conexiones desde otros orígenes, edita `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "tu-dominio.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Personalizar Modelo de Gemini

Para cambiar el modelo de Gemini utilizado, edita `backend/assistant_engine.py`:

```python
# Línea 62
model_name = "gemini-2.5-flash"  # Cambiar por otro modelo disponible
```

Modelos disponibles:
- `gemini-2.5-flash` (rápido y eficiente)
- `gemini-pro` (más potente)
- Otros modelos según disponibilidad en tu cuenta

### Ajustar Parámetros de Generación

En `backend/assistant_engine.py`, puedes ajustar los parámetros de generación de Gemini:

```python
generation_config={
    "temperature": 0.3,  # 0.0-1.0: más bajo = más preciso, más alto = más creativo
    "top_p": 0.8,        # Nucleus sampling
    "top_k": 40,         # Top-k sampling
}
```

---

## 🔧 Troubleshooting

### Problemas Comunes

#### El backend no inicia

**Error**: `ModuleNotFoundError: No module named 'fastapi'`

**Solución**: Asegúrate de estar en el entorno virtual y las dependencias están instaladas:
```bash
cd backend
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

#### Gemini no funciona

**Error**: `GEMINI_API_KEY no encontrada`

**Solución**:
1. Verifica que el archivo `.env` existe en `backend/`
2. Verifica que contiene `GEMINI_API_KEY=tu_api_key`
3. Reinicia el backend

**Nota**: El sistema funcionará con fallback si Gemini no está disponible, pero las respuestas serán menos inteligentes.

#### El frontend no se conecta al backend

**Error**: `Network Error` o `CORS error`

**Solución**:
1. Verifica que el backend está corriendo en `http://localhost:8000`
2. Verifica la variable `VITE_API_URL` en `frontend/.env`
3. Verifica que CORS permite el origen del frontend

#### La base de conocimiento no se carga

**Error**: Respuestas genéricas o "No tengo información"

**Solución**:
1. Verifica que `Base_Conocimiento_GEA.md` existe en la raíz del proyecto
2. Verifica que el archivo tiene contenido válido
3. Revisa los logs del backend para ver errores de carga

#### Puerto ya en uso

**Error**: `Address already in use`

**Solución**:
- Cambia el puerto en el comando de inicio:
  ```bash
  uvicorn main:app --reload --port 8001  # Backend
  ```
- O mata el proceso que está usando el puerto:
  - Windows: `netstat -ano | findstr :8000` y luego `taskkill /PID <PID> /F`
  - Linux/Mac: `lsof -ti:8000 | xargs kill`

### Logs y Debugging

#### Backend

Los logs se muestran en la consola. Para más detalles, puedes agregar logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Frontend

Abre las herramientas de desarrollador del navegador (F12) para ver:
- Errores en la consola
- Requests de red en la pestaña Network
- Estado de React en React DevTools

---

## 🤝 Contribución

### Estructura del Código

```
asistente GEA/
├── backend/
│   ├── main.py              # API FastAPI principal
│   ├── assistant_engine.py  # Motor del asistente
│   ├── requirements.txt     # Dependencias Python
│   └── .env                 # Variables de entorno
├── frontend/
│   ├── src/
│   │   ├── components/      # Componentes React
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── MessageList.tsx
│   │   │   ├── MessageInput.tsx
│   │   │   └── Suggestions.tsx
│   │   ├── services/
│   │   │   └── api.ts       # Cliente API
│   │   ├── types/
│   │   │   └── index.ts     # Tipos TypeScript
│   │   └── App.tsx          # Componente principal
│   └── package.json
├── Base_Conocimiento_GEA.md # Base de conocimiento
└── docs/                    # Documentación
```

### Mejoras Futuras

- [ ] Persistencia de conversaciones en base de datos
- [ ] Autenticación de usuarios
- [ ] Historial de conversaciones
- [ ] Exportación de conversaciones
- [ ] Soporte para múltiples idiomas
- [ ] Integración con sistema GEA real
- [ ] Dashboard de estadísticas
- [ ] Modo oscuro/claro
- [ ] Notificaciones push

---

## 📄 Licencia y Contacto

### Licencia

© 2023 IMPROTECSA S.A.S. - Todos los derechos reservados.

### Información de Contacto

**Empresa**: IMPROTECSA S.A.S.  
**Sitio Web**: [WWW.IMPROTECSA.COM](http://www.improtecsa.com)  
**Sistema**: GEA - Sistema de Gestión

### Soporte

Para más información sobre GEA o soporte técnico, visita el sitio web oficial o contacta al equipo de IMPROTECSA S.A.S.

---

**Última actualización**: Enero 2025


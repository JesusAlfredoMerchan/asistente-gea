# 🤖 Asistente Inteligente GEA

Asistente web inteligente para facilitar el uso del sistema GEA. Permite a los usuarios interactuar con el sistema sin necesidad de consultar el manual, proporcionando respuestas contextuales y guías paso a paso.

## 🏗️ Arquitectura

- **Frontend**: React + TypeScript + Vite
- **Backend**: Python + FastAPI
- **Arquitectura**: Separación frontend/backend

## 📁 Estructura del Proyecto

```
asistente GEA/
├── backend/
│   ├── main.py                 # API FastAPI principal
│   ├── assistant_engine.py     # Motor del asistente inteligente
│   └── requirements.txt        # Dependencias Python
├── frontend/
│   ├── src/
│   │   ├── components/         # Componentes React
│   │   ├── services/           # Servicios API
│   │   ├── types/              # Tipos TypeScript
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   └── vite.config.ts
├── Base_Conocimiento_GEA.md    # Base de conocimiento
├── iniciar-aplicacion.bat      # Script de inicio automático (Windows)
├── detener-aplicacion.bat      # Script para detener servidores
└── README.md
```

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.8 o superior
- Node.js 18 o superior
- npm o yarn

### Inicio Rápido (Windows)

**Opción más fácil:** Ejecuta el script de inicio automático:

```bash
iniciar-aplicacion.bat
```

Este script:
- ✅ Verifica que Python y Node.js estén instalados
- ✅ Crea el entorno virtual de Python si no existe
- ✅ Instala todas las dependencias automáticamente
- ✅ Inicia el backend y frontend en ventanas separadas

Para detener los servidores, ejecuta:
```bash
detener-aplicacion.bat
```

### Inicio Manual

#### Backend

1. Navegar a la carpeta backend:
```bash
cd backend
```

2. Crear entorno virtual (recomendado):
```bash
python -m venv venv
```

3. Activar entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Ejecutar el servidor:
```bash
uvicorn main:app --reload --port 8000
```

El backend estará disponible en `http://localhost:8000`

#### Frontend

1. Navegar a la carpeta frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Ejecutar en modo desarrollo:
```bash
npm run dev
```

El frontend estará disponible en `http://localhost:3000`

## 🎯 Funcionalidades

- ✅ Chat interactivo con el asistente
- ✅ Respuestas contextuales basadas en la base de conocimiento
- ✅ Guías paso a paso para procedimientos comunes
- ✅ Sugerencias de preguntas relacionadas
- ✅ Interfaz moderna y responsive
- ✅ Soporte para múltiples conversaciones

## 📚 Base de Conocimiento

El asistente utiliza el archivo `Base_Conocimiento_GEA.md` que contiene:
- Información general del sistema GEA
- Descripción de módulos (Tareas, Procesos, Informes, etc.)
- Procedimientos paso a paso
- Preguntas frecuentes
- Glosario de términos

## 🔧 Configuración

### Variables de Entorno

**Frontend:**
Crea un archivo `.env` en la carpeta `frontend`:
```
VITE_API_URL=http://localhost:8000
```

**Backend (Gemini AI):**
1. Obtén tu API key de Google Gemini en: https://makersuite.google.com/app/apikey
2. Copia el archivo `backend/env.example` como `backend/.env`
3. Reemplaza `tu_api_key_aqui` con tu API key real:
```
GEMINI_API_KEY=tu_api_key_real_aqui
```

**Nota:** El asistente usa Gemini AI para generar respuestas inteligentes. Si no configuras la API key, el sistema usará un método de fallback basado en búsqueda de texto.

## 📝 API Endpoints

### POST `/api/chat`
Envía un mensaje al asistente y recibe una respuesta.

**Request:**
```json
{
  "message": "¿Cómo creo un nuevo usuario?",
  "conversation_id": "opcional-uuid"
}
```

**Response:**
```json
{
  "response": "Te guío paso a paso...",
  "conversation_id": "uuid",
  "suggestions": ["sugerencia 1", "sugerencia 2"]
}
```

### GET `/api/suggestions`
Obtiene sugerencias de preguntas comunes.

### GET `/api/health`
Verifica el estado del servicio.

## 🎨 Características de la Interfaz

- Diseño moderno con gradientes
- Animaciones suaves
- Responsive (móvil y desktop)
- Indicador de escritura mientras procesa
- Burbujas de mensaje diferenciadas
- Sugerencias interactivas

## 🔄 Flujo de Conversación

1. Usuario escribe una pregunta
2. El sistema busca información relevante en la base de conocimiento
3. Genera una respuesta contextual
4. Proporciona sugerencias relacionadas
5. Mantiene el contexto de la conversación

## 🛠️ Tecnologías Utilizadas

**Backend:**
- FastAPI: Framework web moderno y rápido
- Python: Lenguaje de programación
- Procesamiento de texto: Búsqueda semántica en markdown

**Frontend:**
- React 18: Biblioteca UI
- TypeScript: Tipado estático
- Vite: Build tool rápido
- Axios: Cliente HTTP

## 📄 Licencia

© 2023 IMPROTECSA S.A.S.

## 🤝 Soporte

Para más información sobre GEA, visita: [WWW.IMPROTECSA.COM](http://www.improtecsa.com)


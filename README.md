# 🤖 Asistente Inteligente GEA

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18.2-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688.svg)](https://fastapi.tiangolo.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.2-3178C6.svg)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](http://www.improtecsa.com)

Asistente web inteligente para facilitar el uso del sistema GEA. Permite a los usuarios interactuar con el sistema sin necesidad de consultar el manual, proporcionando respuestas contextuales y guías paso a paso mediante inteligencia artificial.

## 📖 Descripción del Proyecto

El **Asistente Inteligente GEA** es una aplicación web desarrollada para facilitar el acceso y uso del sistema GEA (Sistema de Gestión de IMPROTECSA S.A.S.). Utiliza inteligencia artificial generativa (Google Gemini AI y OpenAI) para proporcionar respuestas contextuales, guías paso a paso y soporte técnico en tiempo real.

### ¿Qué es GEA?

GEA es un sistema de información de gestión basado en flujos de trabajo que permite diseñar, parametrizar y supervisar procesos de trabajo de manera eficiente. Es una plataforma 100% web desarrollada por IMPROTECSA S.A.S.

### Características Principales

- ✅ **Chat Interactivo**: Conversación en tiempo real con el asistente
- ✅ **Inteligencia Artificial**: Integración con Google Gemini AI y OpenAI GPT
- ✅ **Gestión de Modelos**: Selección automática y manual de modelos de IA
- ✅ **Modo Oscuro/Claro**: Interfaz adaptable con persistencia de preferencias
- ✅ **Exportar Conversaciones**: Exportación en TXT, Markdown y JSON
- ✅ **Búsqueda en Conversación**: Búsqueda rápida de mensajes anteriores
- ✅ **Historial de Conversaciones**: Gestión de múltiples conversaciones
- ✅ **Atajos de Teclado**: Navegación rápida con teclado
- ✅ **Responsive Design**: Interfaz adaptable a móviles y desktop
- ✅ **Mantenimiento de Contexto**: El asistente recuerda la conversación

---

## 🚀 Instalación

### Prerrequisitos

- **Python** 3.11 o superior
- **Node.js** 18 o superior
- **npm** o **yarn**
- Cuentas con API keys de:
  - [Google Gemini AI](https://makersuite.google.com/app/apikey)
  - [OpenAI](https://platform.openai.com/api-keys) (opcional)

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

Para detener los servidores:
```bash
detener-aplicacion.bat
```

### Instalación Manual

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/asistente-gea.git
cd asistente-gea
```

#### 2. Configurar Backend

```bash
# Navegar a la carpeta backend
cd backend

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp env.example .env
# Editar .env y agregar tus API keys:
# GEMINI_API_KEY=tu_api_key_aqui
# OPENAI_API_KEY=tu_api_key_aqui (opcional)
```

#### 3. Configurar Frontend

```bash
# Navegar a la carpeta frontend
cd frontend

# Instalar dependencias
npm install

# Crear archivo .env (opcional, para desarrollo local)
echo "VITE_API_URL=http://localhost:8000" > .env
```

#### 4. Iniciar Servidores

**Backend:**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm run dev
```

El backend estará disponible en `http://localhost:8000`  
El frontend estará disponible en `http://localhost:3000`

---

## 💻 Uso

### Interfaz de Usuario

1. **Abrir la aplicación**: Navega a `http://localhost:3000` (o la URL de producción)
2. **Escribir pregunta**: Escribe tu pregunta sobre GEA en el campo de texto
3. **Enviar mensaje**: Presiona `Enter` o click en el botón de enviar
4. **Recibir respuesta**: El asistente generará una respuesta contextual
5. **Seguir conversación**: El asistente mantiene el contexto de la conversación

### Funcionalidades Disponibles

#### 🔍 Búsqueda en Conversación
- Presiona `Ctrl/Cmd + K` para abrir la búsqueda
- Busca mensajes anteriores rápidamente
- Navega entre resultados con `Enter` y `Shift + Enter`

#### 📥 Exportar Conversación
- Click en el botón de exportar (📄)
- Selecciona formato: TXT, Markdown o JSON
- Descarga la conversación completa

#### 🌓 Modo Oscuro/Claro
- Click en el botón de tema (🌙/☀️)
- La preferencia se guarda automáticamente

#### 💬 Nueva Conversación
- Click en "Nueva conversación" en el historial
- Inicia una conversación nueva sin perder las anteriores

#### ⌨️ Atajos de Teclado

- `Ctrl/Cmd + K`: Abrir búsqueda
- `Ctrl/Cmd + L`: Limpiar conversación
- `Esc`: Cerrar búsqueda o paneles
- `Enter`: Enviar mensaje
- `Shift + Enter`: Nueva línea

#### 🤖 Selección de Modelo

- Click en el estado del modelo en el header
- Selecciona un modelo diferente
- El sistema cambiará automáticamente cuando la cuota esté excedida

---

## 🏗️ Arquitectura

### Stack Tecnológico

**Backend:**
- **FastAPI**: Framework web moderno y rápido para Python
- **Python 3.11+**: Lenguaje de programación
- **Google Gemini AI**: Modelo de IA generativa principal
- **OpenAI GPT**: Modelo alternativo de IA
- **Uvicorn**: Servidor ASGI de alto rendimiento

**Frontend:**
- **React 18**: Biblioteca de interfaz de usuario
- **TypeScript**: Tipado estático para JavaScript
- **Vite**: Build tool y dev server rápido
- **Axios**: Cliente HTTP para peticiones API
- **React Markdown**: Renderizado de Markdown en respuestas

### Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENTE WEB                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         React + TypeScript + Vite                    │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │ Chat UI  │  │ Messages │  │Suggestions│          │   │
│  │  └──────────┘  └──────────┘  └──────────┘          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTP/REST API
                            │
┌─────────────────────────────────────────────────────────────┐
│                      BACKEND (FastAPI)                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              assistant_engine.py                     │   │
│  │  ┌──────────────┐  ┌──────────────┐                 │   │
│  │  │  Gemini AI   │  │   OpenAI     │                 │   │
│  │  └──────────────┘  └──────────────┘                 │   │
│  │                                                     │   │
│  │  ┌──────────────────────────────────────┐          │   │
│  │  │  Base de Conocimiento (Markdown)     │          │   │
│  │  └──────────────────────────────────────┘          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Componentes Principales

#### Backend
- **`main.py`**: API REST principal con endpoints FastAPI
- **`assistant_engine.py`**: Motor del asistente con lógica de IA
- **`Base_Conocimiento_GEA.md`**: Base de conocimiento en Markdown

#### Frontend
- **`App.tsx`**: Componente raíz de la aplicación
- **`ChatInterface.tsx`**: Interfaz principal de chat
- **`MessageBubble.tsx`**: Componente de burbuja de mensaje
- **`ModelStatus.tsx`**: Componente de estado de modelos
- **`services/api.ts`**: Cliente API para comunicación con backend

### Flujo de Datos

1. Usuario escribe mensaje en el frontend
2. Frontend envía petición POST a `/api/chat`
3. Backend procesa mensaje con `assistant_engine.py`
4. Motor busca información relevante en base de conocimiento
5. Genera respuesta usando IA (Gemini/OpenAI)
6. Retorna respuesta al frontend con sugerencias
7. Frontend renderiza respuesta y actualiza UI

---

## 🔌 APIs Utilizadas

### Google Gemini AI

- **Uso**: Modelo principal de IA generativa
- **Funcionalidad**: Generación de respuestas contextuales
- **Modelos disponibles**: Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini Flash Lite, y más
- **Características**:
  - Procesamiento de lenguaje natural en español
  - Mantenimiento de contexto conversacional
  - Validación de respuestas contra base de conocimiento
  - Cambio automático de modelo cuando se excede la cuota

### OpenAI API

- **Uso**: Modelo alternativo de IA
- **Funcionalidad**: Fallback cuando Gemini no está disponible
- **Modelos disponibles**: GPT-3.5-turbo
- **Características**:
  - Respuestas rápidas y precisas
  - Compatible con el mismo formato de conversación

### FastAPI REST API

**Endpoints principales:**

- `POST /api/chat` - Enviar mensaje al asistente
- `GET /api/suggestions` - Obtener sugerencias de preguntas
- `GET /api/models` - Estado de modelos disponibles
- `POST /api/models/change` - Cambiar modelo manualmente
- `GET /api/health` - Verificar estado del servicio

Para documentación completa de la API, ver [GUIA_APIS.md](docs/GUIA_APIS.md)

---

## 📁 Estructura del Proyecto

```
asistente-gea/
├── backend/
│   ├── main.py                 # API FastAPI principal
│   ├── assistant_engine.py     # Motor del asistente inteligente
│   ├── requirements.txt        # Dependencias Python
│   ├── env.example            # Ejemplo de variables de entorno
│   └── runtime.txt            # Versión de Python para despliegue
├── frontend/
│   ├── src/
│   │   ├── components/         # Componentes React
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── MessageBubble.tsx
│   │   │   ├── ModelStatus.tsx
│   │   │   └── ...
│   │   ├── services/          # Servicios API
│   │   │   └── api.ts
│   │   ├── hooks/             # Custom hooks
│   │   ├── contexts/          # React contexts
│   │   └── types/             # Tipos TypeScript
│   ├── public/                # Archivos estáticos
│   ├── package.json
│   └── vite.config.ts
├── docs/                      # Documentación
│   ├── ARQUITECTURA.md
│   ├── GUIA_DESPLIEGUE.md
│   └── ...
├── Base_Conocimiento_GEA.md   # Base de conocimiento
├── render.yaml                # Configuración Render
├── vercel.json                # Configuración Vercel
└── README.md
```

---

## 🔧 Configuración

### Variables de Entorno

#### Backend (`backend/.env`)

```env
GEMINI_API_KEY=tu_api_key_de_gemini
OPENAI_API_KEY=tu_api_key_de_openai
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
ENVIRONMENT=development
```

#### Frontend (`frontend/.env`)

```env
VITE_API_URL=http://localhost:8000
```

**Nota**: En producción, estas variables se configuran en las plataformas de despliegue (Render y Vercel).

### Obtener API Keys

- **Google Gemini**: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- **OpenAI**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

Ver guías detalladas en `docs/GUIA_OBTENER_GEMINI_KEY.md` y `docs/GUIA_OBTENER_OPENAI_KEY.md`

---

## 🚀 Despliegue

El proyecto está configurado para desplegarse en:

- **Backend**: [Render](https://render.com)
- **Frontend**: [Vercel](https://vercel.com)

Ver guía completa de despliegue en [`docs/GUIA_DESPLIEGUE.md`](docs/GUIA_DESPLIEGUE.md)

---

## 📚 Documentación Adicional

- [Arquitectura del Sistema](docs/ARQUITECTURA.md)
- [Guía de APIs](docs/GUIA_APIS.md)
- [Guía de Despliegue](docs/GUIA_DESPLIEGUE.md)
- [Casos de Uso](docs/CASOS_DE_USO.md)
- [Guías de Uso](docs/GUIAS_USO.md)

---

## 🤝 Contribución

Este es un proyecto privado desarrollado para IMPROTECSA S.A.S.

---

## 📄 Licencia

© 2025 IMPROTECSA S.A.S. Todos los derechos reservados.

---

## 🔗 Enlaces

- **IMPROTECSA**: [www.improtecsa.com](http://www.improtecsa.com)
- **GitHub**: [github.com/JesusAlfredoMerchan/asistente-gea](https://github.com/JesusAlfredoMerchan/asistente-gea)

---

## 📞 Soporte

Para más información sobre GEA o soporte técnico, visita [www.improtecsa.com](http://www.improtecsa.com)

---

**Desarrollado con ❤️ para IMPROTECSA S.A.S.**

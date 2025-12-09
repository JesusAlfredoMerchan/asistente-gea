# 📖 Guías de Uso - Asistente Inteligente GEA

## 📋 Tabla de Contenidos

1. [Guía para Usuarios Finales](#guía-para-usuarios-finales)
2. [Guía para Desarrolladores](#guía-para-desarrolladores)
3. [Guía de Instalación Detallada](#guía-de-instalación-detallada)
4. [Guía de Configuración](#guía-de-configuración)
5. [Guía de Mantenimiento](#guía-de-mantenimiento)
6. [Preguntas Frecuentes Técnicas](#preguntas-frecuentes-técnicas)

---

## 👥 Guía para Usuarios Finales

### Primeros Pasos

#### 1. Acceder al Asistente

1. Abre tu navegador web (Chrome, Firefox, Edge, Safari)
2. Navega a la dirección del asistente (normalmente: `http://localhost:5173`)
3. Verás la interfaz del chat con un mensaje de bienvenida

#### 2. Hacer tu Primera Pregunta

1. **Escribe tu pregunta** en el campo de texto en la parte inferior
2. **Presiona Enter** o haz clic en el botón de enviar (➤)
3. **Espera la respuesta** del asistente (verás un indicador de "escribiendo...")

#### 3. Usar Sugerencias

- Al iniciar verás **sugerencias de preguntas comunes** en la parte inferior
- **Haz clic** en cualquier sugerencia para hacerla rápidamente
- Después de cada respuesta, aparecerán **sugerencias relacionadas**

### Consejos para Obtener Mejores Respuestas

#### ✅ Haz Preguntas Específicas

**Buenas preguntas:**
- "¿Cómo creo un nuevo usuario en GEA?"
- "Explícame qué son las tareas pendientes"
- "¿Cuáles son los pasos para asignar permisos a un perfil?"

**Preguntas menos efectivas:**
- "Ayuda" (demasiado genérico)
- "GEA" (muy vaga)
- "¿Qué puedo hacer?" (muy amplia)

#### ✅ Usa Palabras Clave de GEA

El asistente reconoce términos específicos de GEA:
- **Módulos**: Tareas, Procesos, Informes, Mapas, Parámetros, Seguridad
- **Conceptos**: Usuario, Perfil, Permiso, Actividad, Proceso, Flujo
- **Acciones**: Crear, Asignar, Gestionar, Configurar

#### ✅ Haz Preguntas de Seguimiento

El asistente mantiene el contexto de la conversación, así que puedes:
- Preguntar por más detalles: "¿Y cómo hago eso?"
- Pedir ejemplos: "¿Puedes darme un ejemplo?"
- Aclarar dudas: "¿Qué significa 'perfil'?"

### Ejemplos de Conversaciones

#### Ejemplo 1: Crear un Usuario

```
Tú: ¿Cómo creo un nuevo usuario?

Asistente: Te guío paso a paso para crear un nuevo usuario en GEA:
1. Ingresar en el módulo Seguridad → Menú Administración → Usuarios
2. Hacer clic en Nuevo Registro
3. Completar los campos solicitados...
...

Tú: ¿Cuál es el mínimo de caracteres para la contraseña?

Asistente: El mínimo de caracteres para la contraseña es 8 caracteres...
```

#### Ejemplo 2: Entender un Módulo

```
Tú: Explícame el módulo de Tareas

Asistente: El módulo de Tareas en GEA te permite gestionar...
- Tareas Pendientes: Tareas asignadas que están pendientes...
- Tareas Iniciadas: Tareas que has iniciado...
...

Tú: ¿Cuál es la diferencia entre tareas pendientes y en proceso?

Asistente: La diferencia principal es...
```

### Funcionalidades de la Interfaz

#### Mensajes del Usuario
- Aparecen a la **derecha** con fondo azul/gradiente
- Incluyen timestamp

#### Mensajes del Asistente
- Aparecen a la **izquierda** con fondo gris/blanco
- Formateo de texto (negrita, listas, etc.)
- Incluyen timestamp

#### Indicadores Visuales
- **"Escribiendo..."**: El asistente está procesando tu mensaje
- **Sugerencias**: Aparecen como botones clickeables

### Solución de Problemas para Usuarios

#### El asistente no responde

**Posibles causas:**
1. El backend no está corriendo
2. Problemas de conexión
3. Error en el servidor

**Solución:**
- Verifica que los servidores estén corriendo
- Recarga la página (F5)
- Intenta de nuevo después de unos segundos

#### Respuestas genéricas o "No tengo información"

**Posibles causas:**
1. La pregunta es muy vaga
2. La información no está en la base de conocimiento
3. Palabras mal escritas

**Solución:**
- Reformula tu pregunta de forma más específica
- Usa términos clave de GEA
- Revisa la ortografía

#### La página no carga

**Solución:**
- Verifica la URL correcta
- Asegúrate de que el frontend esté corriendo
- Limpia la caché del navegador (Ctrl+Shift+Delete)

---

## 💻 Guía para Desarrolladores

### Configuración del Entorno de Desarrollo

#### 1. Clonar/Configurar el Repositorio

```bash
# Navegar al directorio del proyecto
cd "C:\Users\Improtecsa\Desktop\asistente GEA"
```

#### 2. Configurar Backend

```bash
# Crear entorno virtual
cd backend
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
copy env.example .env
# Editar .env y agregar GEMINI_API_KEY
```

#### 3. Configurar Frontend

```bash
# Navegar a frontend
cd ../frontend

# Instalar dependencias
npm install

# (Opcional) Configurar variables de entorno
# Crear .env con VITE_API_URL=http://localhost:8000
```

### Flujo de Desarrollo

#### Iniciar Servidores en Modo Desarrollo

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate  # Windows
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

#### Hot Reload

- **Backend**: Cambios en `.py` recargan automáticamente
- **Frontend**: Cambios en React recargan automáticamente (HMR)

### Estructura del Código

#### Agregar un Nuevo Endpoint

**1. Editar `backend/main.py`:**

```python
@app.get("/api/nuevo-endpoint")
async def nuevo_endpoint():
    """Descripción del endpoint"""
    return {"mensaje": "Respuesta"}
```

**2. Agregar función en el cliente (opcional):**

**`frontend/src/services/api.ts`:**
```typescript
export const nuevoEndpoint = async () => {
  const response = await axios.get(`${API_URL}/api/nuevo-endpoint`);
  return response.data;
};
```

#### Agregar un Nuevo Componente React

**1. Crear archivo del componente:**

**`frontend/src/components/NuevoComponente.tsx`:**
```typescript
import React from 'react';
import './NuevoComponente.css';

interface Props {
  // Props del componente
}

export const NuevoComponente: React.FC<Props> = ({}) => {
  return (
    <div className="nuevo-componente">
      {/* Contenido */}
    </div>
  );
};
```

**2. Crear archivo CSS:**

**`frontend/src/components/NuevoComponente.css`:**
```css
.nuevo-componente {
  /* Estilos */
}
```

**3. Importar y usar:**

```typescript
import { NuevoComponente } from './components/NuevoComponente';

// En tu componente padre
<NuevoComponente />
```

### Debugging

#### Backend

**1. Logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Usar logging
logging.debug("Mensaje de debug")
logging.info("Información")
logging.warning("Advertencia")
logging.error("Error")
```

**2. Debugger:**
```python
# Agregar breakpoint
import pdb; pdb.set_trace()

# O usar VS Code debugger
```

**3. Swagger UI:**
- Visita `http://localhost:8000/docs`
- Prueba endpoints directamente

#### Frontend

**1. Console Logs:**
```typescript
console.log("Mensaje", variable);
console.error("Error", error);
```

**2. React DevTools:**
- Instalar extensión del navegador
- Inspeccionar componentes y estado

**3. Network Tab:**
- Abrir DevTools (F12)
- Pestaña Network
- Ver requests y responses

### Testing

#### Ejecutar Tests (cuando se implementen)

**Backend:**
```bash
cd backend
pytest
```

**Frontend:**
```bash
cd frontend
npm test
```

### Versionado de Código

**Git Workflow recomendado:**

```bash
# Crear nueva rama
git checkout -b feature/nueva-funcionalidad

# Hacer cambios y commits
git add .
git commit -m "Descripción del cambio"

# Push a remoto
git push origin feature/nueva-funcionalidad

# Crear Pull Request
```

### Mejores Prácticas

#### Código Backend

- ✅ Usar type hints en Python
- ✅ Documentar funciones con docstrings
- ✅ Validar inputs con Pydantic
- ✅ Manejar errores apropiadamente
- ✅ Usar variables de entorno para configuración

#### Código Frontend

- ✅ Usar TypeScript para tipado
- ✅ Componentes funcionales con hooks
- ✅ Separar lógica de presentación
- ✅ Manejar estados de carga y error
- ✅ Componentes reutilizables

---

## 🔧 Guía de Instalación Detallada

### Instalación desde Cero

#### Paso 1: Verificar Prerrequisitos

**Python:**
```bash
python --version
# Debe ser 3.8 o superior
```

**Node.js:**
```bash
node --version
# Debe ser 18 o superior
```

**npm:**
```bash
npm --version
# Debe estar instalado
```

#### Paso 2: Instalar Backend

```bash
# 1. Navegar a backend
cd backend

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Actualizar pip
python -m pip install --upgrade pip

# 5. Instalar dependencias
pip install -r requirements.txt

# 6. Verificar instalación
python -c "import fastapi; print('FastAPI instalado correctamente')"
```

#### Paso 3: Configurar Backend

```bash
# 1. Copiar archivo de ejemplo
copy env.example .env

# 2. Editar .env y agregar:
# GEMINI_API_KEY=tu_api_key_aqui
```

#### Paso 4: Instalar Frontend

```bash
# 1. Navegar a frontend
cd ../frontend

# 2. Instalar dependencias
npm install

# 3. Verificar instalación
npm list --depth=0
```

#### Paso 5: Verificar Instalación

**Backend:**
```bash
cd backend
venv\Scripts\activate
python -m uvicorn main:app --port 8000
# Visitar http://localhost:8000
# Debe mostrar: {"message": "Asistente GEA API está funcionando"}
```

**Frontend:**
```bash
cd frontend
npm run dev
# Visitar la URL que muestra (normalmente http://localhost:5173)
# Debe mostrar la interfaz del chat
```

### Instalación en Producción

#### Backend

**1. Usar servidor WSGI:**
```bash
# Instalar gunicorn (recomendado para producción)
pip install gunicorn

# Ejecutar
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

**2. Configurar Nginx (opcional):**
```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### Frontend

**1. Build de producción:**
```bash
cd frontend
npm run build
```

**2. Servir archivos estáticos:**
- Los archivos están en `frontend/dist/`
- Servir con Nginx, Apache, o servicio estático

**Nginx ejemplo:**
```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    root /ruta/a/frontend/dist;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

---

## ⚙️ Guía de Configuración

### Variables de Entorno

#### Backend (`.env`)

```env
# API Key de Google Gemini (REQUERIDO)
GEMINI_API_KEY=tu_api_key_aqui

# Configuración del servidor (OPCIONAL)
HOST=0.0.0.0
PORT=8000

# Configuración de Gemini (OPCIONAL)
GEMINI_MODEL=gemini-2.5-flash
GEMINI_TEMPERATURE=0.3
```

#### Frontend (`.env`)

```env
# URL del backend API
VITE_API_URL=http://localhost:8000

# Configuración de la app (OPCIONAL)
VITE_APP_NAME=Asistente GEA
VITE_APP_VERSION=1.0.0
```

### Personalizar Base de Conocimiento

**1. Editar archivo:**
- `Base_Conocimiento_GEA.md` en la raíz del proyecto

**2. Formato recomendado:**
```markdown
## Título Principal

### Subtítulo

Texto descriptivo...

**Pasos:**
1. Primer paso
2. Segundo paso
3. Tercer paso
```

**3. Reiniciar backend** para cargar cambios

### Personalizar Estilos

#### Cambiar Colores Principales

**Frontend CSS:**
```css
/* En App.css o variables CSS */
:root {
  --primary-color: #tu-color;
  --secondary-color: #tu-color;
  --background-gradient: linear-gradient(...);
}
```

#### Personalizar Componentes

- Editar archivos CSS de cada componente
- `frontend/src/components/*.css`

---

## 🔧 Guía de Mantenimiento

### Actualizar Dependencias

#### Backend

```bash
cd backend
venv\Scripts\activate
pip list --outdated
pip install --upgrade nombre-paquete
pip freeze > requirements.txt
```

#### Frontend

```bash
cd frontend
npm outdated
npm update
# O para un paquete específico:
npm install nombre-paquete@latest
```

### Backup de Base de Conocimiento

```bash
# Copiar archivo
copy Base_Conocimiento_GEA.md backup_Base_Conocimiento_GEA_$(date +%Y%m%d).md
```

### Logs

**Backend:**
- Los logs aparecen en la consola
- Para producción, considerar redirigir a archivo:
```bash
python -m uvicorn main:app > logs/backend.log 2>&1
```

**Frontend:**
- Logs en consola del navegador
- Errores en DevTools

### Monitoreo

**Health Check:**
```bash
curl http://localhost:8000/api/health
```

**Verificar estado:**
```json
{
  "status": "healthy",
  "assistant_loaded": true
}
```

---

## ❓ Preguntas Frecuentes Técnicas

### ¿Cómo cambio el modelo de Gemini?

Edita `backend/assistant_engine.py`, línea 62:
```python
model_name = "gemini-pro"  # Cambiar por el modelo deseado
```

### ¿Cómo agrego más sugerencias?

Edita `backend/assistant_engine.py`, método `get_suggestions()`:
```python
def get_suggestions(self) -> List[str]:
    return [
        "Tu nueva sugerencia aquí",
        # ... más sugerencias
    ]
```

### ¿Cómo cambio los puertos?

**Backend:**
```bash
uvicorn main:app --port 8001
```

**Frontend:**
```bash
npm run dev -- --port 3000
```

Y actualiza `VITE_API_URL` en frontend `.env`

### ¿Cómo desactivo Gemini y uso solo fallback?

Simplemente no configures `GEMINI_API_KEY` en `.env`. El sistema usará automáticamente el método de fallback.

### ¿Cómo agrego nuevos endpoints?

Ver sección [Agregar un Nuevo Endpoint](#agregar-un-nuevo-endpoint) en Guía para Desarrolladores.

### ¿Cómo personalizo los mensajes del asistente?

Edita `frontend/src/components/ChatInterface.tsx`, línea 21:
```typescript
text: 'Tu mensaje personalizado aquí',
```

---

**Última actualización**: Enero 2025


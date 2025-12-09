# 🚀 Guía de Despliegue - Asistente GEA

Esta guía te ayudará a desplegar el Asistente GEA en GitHub, Render (backend) y Vercel (frontend).

## 📋 Prerrequisitos

1. Cuenta en [GitHub](https://github.com)
2. Cuenta en [Render](https://render.com) (para backend)
3. Cuenta en [Vercel](https://vercel.com) (para frontend)
4. Git instalado en tu máquina

---

## 1️⃣ Subir el Proyecto a GitHub

### Paso 1: Inicializar Git (si no está inicializado)

```bash
git init
```

### Paso 2: Agregar todos los archivos

```bash
git add .
```

### Paso 3: Hacer el primer commit

```bash
git commit -m "Initial commit: Asistente GEA - Proyecto completo"
```

### Paso 4: Crear repositorio en GitHub

1. Ve a [GitHub](https://github.com) y crea un nuevo repositorio
2. **NO** inicialices con README, .gitignore o licencia (ya los tenemos)
3. Copia la URL del repositorio (ejemplo: `https://github.com/tu-usuario/asistente-gea.git`)

### Paso 5: Conectar y subir a GitHub

```bash
git remote add origin https://github.com/tu-usuario/asistente-gea.git
git branch -M main
git push -u origin main
```

---

## 2️⃣ Desplegar Backend en Render

### Paso 1: Crear nuevo servicio en Render

1. Ve a [Render Dashboard](https://dashboard.render.com)
2. Click en **"New +"** → **"Web Service"**
3. Conecta tu repositorio de GitHub
4. Selecciona el repositorio `asistente-gea`

### Paso 2: Configurar el servicio

- **Name**: `asistente-gea-backend`
- **Region**: Elige la región más cercana
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Paso 3: Configurar Variables de Entorno

En la sección **"Environment Variables"**, agrega:

```
GEMINI_API_KEY=tu_api_key_de_gemini
OPENAI_API_KEY=tu_api_key_de_openai
PYTHON_VERSION=3.11.0
```

### Paso 4: Desplegar

1. Click en **"Create Web Service"**
2. Render comenzará a construir y desplegar tu backend
3. Espera a que termine (puede tomar 5-10 minutos)
4. Anota la URL de tu backend (ejemplo: `https://asistente-gea-backend.onrender.com`)

### Paso 5: Verificar el despliegue

Visita: `https://tu-backend-url.onrender.com/api/health`

Deberías ver: `{"message": "Asistente GEA API está funcionando"}`

---

## 3️⃣ Desplegar Frontend en Vercel

### Paso 1: Actualizar URL del Backend

Antes de desplegar, actualiza la URL del backend en `frontend/src/services/api.ts`:

```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://tu-backend-url.onrender.com'
```

O crea un archivo `.env.production` en `frontend/`:

```
VITE_API_URL=https://tu-backend-url.onrender.com
```

### Paso 2: Desplegar en Vercel

#### Opción A: Desde la CLI de Vercel

```bash
cd frontend
npm install -g vercel
vercel
```

Sigue las instrucciones:
- Login con tu cuenta de Vercel
- Presiona Enter para confirmar el proyecto
- Presiona Enter para confirmar la configuración

#### Opción B: Desde el Dashboard de Vercel

1. Ve a [Vercel Dashboard](https://vercel.com/dashboard)
2. Click en **"Add New..."** → **"Project"**
3. Importa tu repositorio de GitHub
4. Configura el proyecto:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

### Paso 3: Configurar Variables de Entorno en Vercel

En la configuración del proyecto → **"Environment Variables"**, agrega:

```
VITE_API_URL=https://tu-backend-url.onrender.com
```

### Paso 4: Desplegar

1. Click en **"Deploy"**
2. Vercel construirá y desplegará tu frontend
3. Espera a que termine (2-5 minutos)
4. Obtendrás una URL (ejemplo: `https://asistente-gea.vercel.app`)

---

## 4️⃣ Configurar CORS en el Backend

Render y Vercel tienen dominios diferentes, así que necesitas permitir CORS.

Verifica que `backend/main.py` tenga configurado CORS:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambia por tu URL de Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Para producción**, actualiza `allow_origins` con tu URL de Vercel:

```python
allow_origins=[
    "https://tu-app.vercel.app",
    "http://localhost:3000"  # Para desarrollo local
]
```

---

## 5️⃣ Verificar el Despliegue

1. **Backend**: `https://tu-backend-url.onrender.com/api/health`
2. **Frontend**: `https://tu-app.vercel.app`

Prueba enviar un mensaje desde el frontend desplegado para verificar que la comunicación funcione.

---

## 🔧 Solución de Problemas

### Backend no responde en Render

- Verifica que el `Start Command` use `$PORT`
- Revisa los logs en Render Dashboard
- Verifica que las variables de entorno estén configuradas

### Frontend no puede conectar con el backend

- Verifica que `VITE_API_URL` esté configurada en Vercel
- Verifica CORS en el backend
- Revisa la consola del navegador para ver errores

### Cambios no se reflejan

- Render y Vercel hacen deploy automático cuando haces push a GitHub
- Puedes forzar un nuevo deploy desde el dashboard
- Verifica que los cambios estén en el repositorio de GitHub

---

## 📝 Notas Importantes

1. **Render Free Tier**: El backend puede "dormir" después de inactividad. El primer request puede tardar ~30 segundos.
2. **Variables de Entorno**: Nunca subas archivos `.env` a GitHub. Usa las variables de entorno de Render/Vercel.
3. **Actualizaciones**: Cada push a `main` desplegará automáticamente en Render y Vercel.

---

## ✅ Checklist Final

- [ ] Proyecto subido a GitHub
- [ ] Backend desplegado en Render
- [ ] Frontend desplegado en Vercel
- [ ] Variables de entorno configuradas
- [ ] CORS configurado correctamente
- [ ] URLs verificadas y funcionando
- [ ] Pruebas de funcionalidad completadas

¡Listo! Tu Asistente GEA está desplegado y listo para usar 🎉


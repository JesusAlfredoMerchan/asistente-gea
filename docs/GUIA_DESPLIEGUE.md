# 🚀 Guía de Despliegue - Asistente GEA

Esta guía completa te ayudará a desplegar el Asistente GEA en GitHub, Render (backend) y Vercel (frontend).

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
git commit -m "Initial commit: Asistente GEA"
```

### Paso 4: Crear repositorio en GitHub

1. Ve a [GitHub](https://github.com/new)
2. Crea un nuevo repositorio (ejemplo: `asistente-gea`)
3. **NO** inicialices con README, .gitignore o licencia (ya tienes archivos locales)

### Paso 5: Conectar y subir

```bash
git remote add origin https://github.com/TU_USUARIO/asistente-gea.git
git branch -M main
git push -u origin main
```

---

## 2️⃣ Desplegar Backend en Render

### Paso 1: Crear Nuevo Servicio en Render

1. Ve a [Render Dashboard](https://dashboard.render.com)
2. Click en **"New +"** → **"Web Service"**
3. Conecta tu repositorio de GitHub si no lo has hecho
4. Selecciona el repositorio `asistente-gea`

### Paso 2: Configurar el Servicio

- **Name:** `asistente-gea-backend` (o el nombre que prefieras)
- **Environment:** `Python 3`
- **Build Command:** `cd backend && pip install -r requirements.txt`
- **Start Command:** `cd backend && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Root Directory:** `/` (raíz del proyecto)

### Paso 3: Configurar Variables de Entorno

En **"Environment Variables"**, agrega:

```
GEMINI_API_KEY=tu_api_key_de_gemini
OPENAI_API_KEY=tu_api_key_de_openai
PYTHON_VERSION=3.11.0
ALLOWED_ORIGINS=https://tu-app.vercel.app,http://localhost:3000
```

**⚠️ IMPORTANTE:** 
- Después de agregar `ALLOWED_ORIGINS`, agrega la URL de Vercel **DESPUÉS** de desplegar el frontend
- Por ahora puedes dejarlo con `http://localhost:3000` para pruebas

### Paso 4: Desplegar

1. Click en **"Create Web Service"**
2. Render comenzará a construir y desplegar tu backend
3. Espera 5-10 minutos
4. Obtendrás una URL tipo: `https://asistente-gea-backend.onrender.com`

### Paso 5: Verificar el Backend

Visita: `https://tu-backend-url.onrender.com/api/health`

Deberías ver: `{"message": "Asistente GEA API está funcionando"}`

---

## 3️⃣ Desplegar Frontend en Vercel

### Paso 1: Crear Proyecto en Vercel

1. Ve a [Vercel Dashboard](https://vercel.com/dashboard)
2. Click en **"Add New..."** → **"Project"**
3. Si no has conectado GitHub, hazlo primero
4. Selecciona el repositorio: `asistente-gea`

### Paso 2: Configurar el Proyecto

**Framework Preset:** `Vite` (debería detectarse automáticamente)

**Root Directory:** 
```
frontend
```

**Build Command:**
```
npm run build
```

**Output Directory:**
```
dist
```

**Install Command:**
```
npm install
```

### Paso 3: Configurar Variable de Entorno

**ANTES de hacer deploy**, agrega la variable:

1. Busca **"Environment Variables"** en la configuración
2. Click en **"Add"**
3. Agrega:

   **Key:** `VITE_API_URL`
   
   **Value:** La URL de tu backend en Render
   
   Ejemplo: `https://asistente-gea-backend.onrender.com`
   
   **⚠️ IMPORTANTE:** Sin barra final (`/`)
   
   **Environments:** ✅ Production, ✅ Preview, ✅ Development

4. Click en **"Save"**

### Paso 4: Desplegar

1. Click en **"Deploy"**
2. Espera 2-5 minutos
3. Obtendrás una URL tipo: `https://asistente-gea.vercel.app`

### Paso 5: Actualizar CORS en Render

**DESPUÉS de obtener la URL de Vercel:**

1. Ve a Render Dashboard → Tu Backend → **"Environment"**
2. Edita la variable `ALLOWED_ORIGINS`:

   ```
   https://asistente-gea.vercel.app,http://localhost:3000
   ```

3. Guarda (Render se reiniciará automáticamente)

---

## 4️⃣ Verificación Final

### Test 1: Verificar Backend

```bash
curl https://tu-backend-url.onrender.com/api/health
```

Debería responder: `{"message": "Asistente GEA API está funcionando"}`

### Test 2: Verificar Frontend

1. Visita `https://tu-app.vercel.app`
2. Abre la consola del navegador (F12)
3. Verifica que no haya errores de CORS
4. Prueba enviar un mensaje al asistente

### Test 3: Verificar Variable de Entorno

En la consola del navegador (F12), escribe:

```javascript
console.log(import.meta.env.VITE_API_URL)
```

Debería mostrar: La URL de tu backend (NO `http://localhost:8000`)

---

## ✅ Checklist Final

- [ ] Proyecto subido a GitHub
- [ ] Backend desplegado en Render
- [ ] Backend responde a `/api/health`
- [ ] Variables de entorno configuradas en Render
- [ ] Frontend desplegado en Vercel
- [ ] Variable `VITE_API_URL` configurada en Vercel
- [ ] Redeploy realizado después de configurar variable
- [ ] CORS configurado en Render con URL de Vercel
- [ ] Aplicación funcionando correctamente en producción

---

## 🔍 Solución de Problemas Comunes

### Error: "ERR_CONNECTION_RESET" en Vercel

**Causa:** Variable `VITE_API_URL` no configurada o redeploy no realizado.

**Solución:**
1. Verifica que `VITE_API_URL` exista en Vercel
2. Haz un **redeploy** después de agregar la variable
3. Verifica en consola: `console.log(import.meta.env.VITE_API_URL)`

### Error: "CORS policy" en el navegador

**Causa:** `ALLOWED_ORIGINS` no configurado en Render.

**Solución:**
1. Render Dashboard → Backend → Environment
2. Agrega/edita `ALLOWED_ORIGINS` con tu URL de Vercel
3. Guarda (Render se reiniciará)

### Backend no inicia en Render

**Causa:** Ruta incorrecta a `requirements.txt` o `Base_Conocimiento_GEA.md`.

**Solución:**
- Verifica que `Build Command` use `cd backend &&`
- Verifica que `Start Command` use `cd backend &&`
- Verifica que `Base_Conocimiento_GEA.md` esté en la raíz del proyecto

---

## 📝 Notas Importantes

- **Vite inyecta variables en build time:** Necesitas redeploy después de cambiar `VITE_API_URL`
- **Variables deben empezar con `VITE_`:** Solo estas son expuestas al cliente
- **No uses valores sensibles en `VITE_*`:** Son visibles en el código del cliente
- **Render tiene cold start:** La primera petición puede tardar 30-60 segundos

---

## 📚 Recursos Adicionales

- [Documentación de Render](https://render.com/docs)
- [Documentación de Vercel](https://vercel.com/docs)
- [Documentación de Vite](https://vitejs.dev)

---

¡Felicitaciones! 🎊 Tu asistente GEA está en producción.


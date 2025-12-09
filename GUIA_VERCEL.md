# 🚀 Guía de Despliegue en Vercel

## 📋 Pasos para Desplegar el Frontend

### Paso 1: Obtener URL del Backend en Render

1. Ve a tu servicio en Render Dashboard
2. Copia la URL de tu backend (ejemplo: `https://asistente-gea-backend.onrender.com`)
3. Guárdala, la necesitarás para configurar Vercel

### Paso 2: Crear Proyecto en Vercel

#### Opción A: Desde el Dashboard de Vercel (Recomendado)

1. Ve a [Vercel Dashboard](https://vercel.com/dashboard)
2. Click en **"Add New..."** → **"Project"**
3. Si no has conectado GitHub, hazlo primero:
   - Click en **"Import Git Repository"**
   - Conecta tu cuenta de GitHub
   - Autoriza a Vercel
4. Selecciona el repositorio: `asistente-gea`

### Paso 3: Configurar el Proyecto

Vercel debería detectar automáticamente que es un proyecto Vite. Si no, configura manualmente:

#### Configuración del Proyecto:

- **Framework Preset**: `Vite`
- **Root Directory**: `frontend` ← **IMPORTANTE**
- **Build Command**: `npm run build` (o déjalo en blanco, Vercel lo detectará)
- **Output Directory**: `dist` (Vercel lo detecta automáticamente)
- **Install Command**: `npm install` (automático)

### Paso 4: Configurar Variables de Entorno

Antes de hacer deploy, agrega la variable de entorno:

1. En la configuración del proyecto, busca **"Environment Variables"**
2. Click en **"Add"** o **"Add New"**
3. Agrega:

   **Nombre:** `VITE_API_URL`
   
   **Valor:** La URL de tu backend en Render
   
   Ejemplo: `https://asistente-gea-backend.onrender.com`
   
   **Environment:** Selecciona todas (Production, Preview, Development)

4. Guarda la variable

### Paso 5: Desplegar

1. Click en **"Deploy"**
2. Vercel comenzará a construir y desplegar tu frontend
3. Espera a que termine (2-5 minutos)
4. Obtendrás una URL (ejemplo: `https://asistente-gea.vercel.app`)

### Paso 6: Verificar el Despliegue

1. Visita la URL de Vercel
2. Abre la consola del navegador (F12)
3. Verifica que no haya errores de conexión con el backend
4. Prueba enviar un mensaje

---

## ⚠️ Configuración de CORS en Render

Después de obtener la URL de Vercel, debes actualizar CORS en Render:

1. Ve a Render Dashboard → Tu Servicio Backend → **Environment**
2. Agrega o edita la variable:

   **Nombre:** `ALLOWED_ORIGINS`
   
   **Valor:** Tu URL de Vercel (ejemplo: `https://asistente-gea.vercel.app`)
   
   **O múltiples orígenes:** `https://asistente-gea.vercel.app,http://localhost:3000`

3. Guarda y Render reiniciará el servicio

---

## 🔧 Configuración Recomendada en Vercel

### Settings → General

- **Framework Preset**: Vite
- **Root Directory**: `frontend`
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`

### Settings → Environment Variables

```
VITE_API_URL=https://tu-backend-url.onrender.com
```

---

## 📝 Estructura de URLs

- **Frontend (Vercel)**: `https://tu-app.vercel.app`
- **Backend (Render)**: `https://tu-backend.onrender.com`

El frontend se conecta al backend usando la variable `VITE_API_URL`.

---

## ✅ Checklist

- [ ] Proyecto creado en Vercel
- [ ] Repositorio de GitHub conectado
- [ ] Root Directory configurado como `frontend`
- [ ] Variable de entorno `VITE_API_URL` configurada
- [ ] Deploy completado exitosamente
- [ ] URL de Vercel obtenida
- [ ] CORS configurado en Render con la URL de Vercel
- [ ] Pruebas de funcionalidad completadas

---

## 🔍 Solución de Problemas

### Error: "Cannot find module"

- Verifica que `package.json` tenga todas las dependencias
- Si falta `react-markdown`, agregarlo (ver abajo)

### Frontend no se conecta al backend

1. Verifica que `VITE_API_URL` esté configurada en Vercel
2. Verifica CORS en Render
3. Revisa la consola del navegador para ver errores

### Build falla en Vercel

- Verifica que el Root Directory sea `frontend`
- Verifica que `package.json` esté en `frontend/`
- Revisa los logs de build en Vercel

---

¡Listo! Tu frontend estará desplegado en Vercel 🎉


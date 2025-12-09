# 🔧 Solución: Error de Carga en Vercel (ERR_CONNECTION_RESET)

## 🔍 Diagnóstico del Problema

El error **ERR_CONNECTION_RESET** y la página que se queda cargando suelen deberse a:

1. **Variable de entorno `VITE_API_URL` no configurada** → El frontend intenta conectarse a `localhost:8000`
2. **El componente `ModelStatusComponent` hace peticiones al cargar** → Si falla, bloquea la carga
3. **Problemas de CORS** → El backend rechaza las peticiones

---

## ✅ Solución Paso a Paso

### Paso 1: Verificar Variable de Entorno en Vercel

1. Ve a **Vercel Dashboard** → Tu proyecto
2. Click en **"Settings"**
3. Click en **"Environment Variables"**
4. **VERIFICA** que exista:

   ```
   Key: VITE_API_URL
   Value: https://tu-backend-url.onrender.com
   ```

   **⚠️ IMPORTANTE:** 
   - El valor debe ser **SIN** barra final (`/`)
   - Ejemplo correcto: `https://asistente-gea-backend.onrender.com`
   - Ejemplo incorrecto: `https://asistente-gea-backend.onrender.com/`

5. **VERIFICA** que esté en los 3 entornos:
   - ✅ Production
   - ✅ Preview  
   - ✅ Development

### Paso 2: Hacer Redeploy Después de Configurar la Variable

**CRÍTICO:** Después de agregar/cambiar la variable, **DEBES** hacer un nuevo deploy:

1. Ve a **"Deployments"**
2. Click en los **tres puntos (⋯)** del último deployment
3. Click en **"Redeploy"**
4. O simplemente haz un nuevo commit y push (esto activará un auto-deploy)

**Por qué es necesario:** Las variables de entorno de Vite se inyectan **durante el build**, no en runtime. Si agregas la variable pero no haces rebuild, seguirá usando el valor por defecto.

### Paso 3: Verificar que la Variable Está en el Build

Para verificar que Vercel está usando la variable:

1. Ve a **Deployments** → Último deployment
2. Click en **"Build Logs"**
3. Busca en los logs si aparece `VITE_API_URL` o la URL de tu backend
4. Si no aparece, la variable no está configurada correctamente

### Paso 4: Verificar Backend en Render

1. Ve a Render Dashboard → Tu backend
2. Verifica que el estado sea **"Live"** o **"Running"**
3. Prueba la URL directamente en el navegador:
   ```
   https://tu-backend-url.onrender.com/api/health
   ```
   Deberías ver: `{"message": "Asistente GEA API está funcionando"}`

### Paso 5: Verificar CORS en Render

1. Render Dashboard → Tu backend → **"Environment"**
2. Verifica que exista:

   ```
   Key: ALLOWED_ORIGINS
   Value: https://asistente-gea.vercel.app
   ```

3. Si no existe, agrégalo y guarda (Render se reiniciará automáticamente)

---

## 🧪 Pruebas de Verificación

### Test 1: Verificar Variable en Consola del Navegador

1. Abre `https://asistente-gea.vercel.app`
2. Abre **Consola del navegador** (F12)
3. Escribe en la consola:
   ```javascript
   console.log(import.meta.env.VITE_API_URL)
   ```
4. **Debería mostrar:** La URL de tu backend (NO `http://localhost:8000`)

### Test 2: Verificar Peticiones al Backend

1. Abre **Network tab** en DevTools (F12)
2. Recarga la página
3. Busca peticiones a `/api/` o a tu backend
4. Verifica el status:
   - ✅ **200**: Funciona correctamente
   - ❌ **CORS Error**: Problema de CORS
   - ❌ **Connection Reset**: Variable mal configurada o backend caído
   - ❌ **404**: Ruta incorrecta

---

## 🛠️ Solución Rápida: Agregar Manejo de Errores

Si el problema persiste, podemos agregar manejo de errores en el frontend para evitar que se quede cargando indefinidamente.

### Opción A: Deshabilitar Temporalmente ModelStatus

Mientras solucionas, puedes comentar temporalmente el `ModelStatusComponent` en `App.tsx`:

```tsx
// Temporalmente comentado hasta resolver conexión
// <ModelStatusComponent />
```

### Opción B: Agregar Timeout y Fallback

Modificar `ModelStatus.tsx` para que no bloquee la carga si falla.

---

## 📋 Checklist de Diagnóstico

- [ ] Variable `VITE_API_URL` existe en Vercel
- [ ] Variable tiene el valor correcto (sin `/` al final)
- [ ] Variable está en Production, Preview y Development
- [ ] Se hizo redeploy después de agregar la variable
- [ ] Backend está corriendo en Render (estado "Live")
- [ ] Backend responde a `/api/health`
- [ ] CORS configurado en Render con URL de Vercel
- [ ] Consola del navegador muestra la URL correcta
- [ ] Network tab muestra peticiones exitosas (200)

---

## 🆘 Si Nada Funciona

1. **Revisa los Build Logs en Vercel:**
   - ¿Hay errores durante el build?
   - ¿Se está usando la variable de entorno?

2. **Revisa los Runtime Logs en Render:**
   - ¿El backend está recibiendo peticiones?
   - ¿Hay errores en los logs?

3. **Prueba la URL del backend directamente:**
   ```bash
   curl https://tu-backend-url.onrender.com/api/health
   ```

4. **Verifica que no haya problemas de red/firewall**

---

## 📝 Notas Importantes

- **Vite inyecta variables en build time:** Por eso necesitas redeploy después de cambiar variables
- **Variables deben empezar con `VITE_`:** Solo las variables con este prefijo son expuestas al cliente
- **No uses valores sensibles:** Las variables `VITE_*` son visibles en el código del cliente

---

¿Necesitas ayuda con algún paso específico?


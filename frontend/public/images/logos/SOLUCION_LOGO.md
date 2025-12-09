# 🔧 Solución: Logo no Aparece

## ✅ Verificación

El archivo `Logo GEA.png` está en: `frontend/public/images/logos/Logo GEA.png`

## 🔄 Pasos para Solucionar

### 1. Reiniciar el Servidor de Desarrollo

**IMPORTANTE**: Después de agregar archivos en `public/`, necesitas reiniciar Vite:

1. Detén el servidor (Ctrl+C)
2. Inicia nuevamente:
   ```bash
   cd frontend
   npm run dev
   ```

### 2. Limpiar Caché del Navegador

1. Abre las herramientas de desarrollador (F12)
2. Click derecho en el botón de recargar
3. Selecciona "Vaciar caché y volver a cargar forzadamente" (Ctrl+Shift+R)

### 3. Verificar la Ruta en el Navegador

1. Abre las herramientas de desarrollador (F12)
2. Ve a la pestaña "Network" (Red)
3. Recarga la página
4. Busca la petición a `/images/logos/Logo GEA.png`
5. Verifica si da error 404 o si se carga correctamente

### 4. Verificar en la Consola

Abre la consola del navegador (F12 → Console) y verifica:
- Si aparece "Logo cargado exitosamente" → El logo está funcionando
- Si aparece un error 404 → El archivo no se encuentra
- Si aparece otro error → Revisa el mensaje

---

## 🐛 Problemas Comunes

### Problema 1: Error 404
**Solución**: 
- Verifica que el archivo esté en `frontend/public/images/logos/Logo GEA.png`
- El nombre debe ser exactamente `Logo GEA.png` (respetando mayúsculas)
- Reinicia el servidor

### Problema 2: El logo se carga pero no se ve
**Solución**:
- Abre las herramientas de desarrollador (F12)
- Inspecciona el elemento `<img>`
- Verifica que tenga dimensiones (width/height)
- Verifica que no esté oculto con `display: none`

### Problema 3: El logo es muy grande/pequeño
**Solución**:
- Ajusta los valores en `frontend/src/App.css`:
  - `max-height: 60px` (altura máxima)
  - `max-width: 200px` (ancho máximo)

---

## 📍 Ruta Correcta

El archivo debe estar en:
```
frontend/
└── public/
    └── images/
        └── logos/
            └── Logo GEA.png
```

Y se accede desde el código como:
```html
<img src="/images/logos/Logo GEA.png" />
```

---

## ✅ Verificación Final

1. ✅ Archivo existe en `frontend/public/images/logos/Logo GEA.png`
2. ✅ Servidor de desarrollo reiniciado
3. ✅ Caché del navegador limpiada
4. ✅ Consola del navegador sin errores
5. ✅ Logo visible en el header

---

## 📞 Si Sigue Sin Funcionar

1. Verifica en la consola del navegador qué error aparece
2. Verifica en Network si la imagen se está cargando
3. Intenta acceder directamente a: `http://localhost:5173/images/logos/Logo%20GEA.png`
4. Si accedes directamente y funciona, el problema es en el código React
5. Si no funciona directamente, el problema es en la ubicación del archivo

---

**Última actualización**: Enero 2025


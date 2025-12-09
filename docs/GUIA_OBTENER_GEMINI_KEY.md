# 🔑 Guía: Cómo Obtener tu API Key de Gemini

## 📋 Pasos para Obtener tu API Key

### **Paso 1: Ir al sitio de Google AI Studio**

Ve directamente a: **https://makersuite.google.com/app/apikey**

O sigue estos pasos:
1. Ve a: **https://ai.google.dev/**
2. Haz clic en **"Get API Key"** o **"Get started"**
3. O ve directamente a: **https://makersuite.google.com/app/apikey**

---

### **Paso 2: Iniciar Sesión**

1. Inicia sesión con tu cuenta de Google
2. Si no tienes cuenta, créala (es gratis)

---

### **Paso 3: Crear API Key**

1. Una vez dentro, verás un botón **"Create API Key"** o **"Get API Key"**
2. Selecciona o crea un proyecto de Google Cloud (si es primera vez, crea uno nuevo)
3. Haz clic en **"Create API Key in new project"** o **"Create API Key"**
4. **⚠️ IMPORTANTE:** Copia la key inmediatamente - se muestra solo una vez
5. La key se verá algo así: `AIzaSy...` (empieza con "AIza")

---

### **Paso 4: Configurar en tu Proyecto**

1. Ve a la carpeta `backend` de tu proyecto
2. Abre el archivo `.env`
3. Reemplaza `tu_api_key_aqui` con tu API key real:

```env
GEMINI_API_KEY=AIzaSyTuApiKeyRealAqui
```

4. Guarda el archivo

---

### **Paso 5: Reiniciar el Backend**

1. Detén el servidor backend (Ctrl+C)
2. Inícialo nuevamente:

```bash
python main.py
```

O si usas el batch:

```bash
start-backend.bat
```

---

## 🆓 Plan Gratuito

**Gemini tiene plan gratuito** con estos límites:
- **20 requests por día** por modelo
- Múltiples modelos disponibles
- No requiere tarjeta de crédito (para el tier gratuito)

---

## ⚠️ Si el Error Persiste

### Verificar que la Key sea Correcta:

1. **Formato correcto:** Debe empezar con `AIzaSy`
2. **Sin espacios:** Asegúrate de no tener espacios antes o después del `=`
3. **Sin comillas:** No pongas comillas alrededor de la key

**Ejemplo CORRECTO:**
```env
GEMINI_API_KEY=AIzaSyAbCdEf123456789
```

**Ejemplo INCORRECTO:**
```env
GEMINI_API_KEY="AIzaSyAbCdEf123456789"  ❌ Con comillas
GEMINI_API_KEY = AIzaSyAbCdEf123456789  ❌ Con espacios
```

---

## 🔗 Enlaces Útiles

- **Obtener API Key**: https://makersuite.google.com/app/apikey
- **Google AI Studio**: https://ai.google.dev/
- **Documentación**: https://ai.google.dev/docs
- **Dashboard**: https://aistudio.google.com/app/apikey

---

## ✅ Checklist

- [ ] Ir a https://makersuite.google.com/app/apikey
- [ ] Iniciar sesión con Google
- [ ] Crear nueva API key
- [ ] Copiar la key (empieza con AIzaSy)
- [ ] Agregar al archivo `backend/.env`
- [ ] Verificar formato correcto (sin espacios, sin comillas)
- [ ] Reiniciar backend
- [ ] Verificar que funciona

---

## 🆘 Troubleshooting

**Error: "API key not valid"**
- ✅ Verifica que la key esté correctamente en `.env`
- ✅ Verifica que no tenga espacios
- ✅ Verifica que empiece con `AIzaSy`
- ✅ Asegúrate de haber copiado la key completa
- ✅ Verifica que el archivo `.env` esté en la carpeta `backend/`

**Error: "File .env not found"**
- ✅ Asegúrate de crear el archivo en `backend/.env`
- ✅ No en `backend/env.txt` o `backend/.env.txt`

---

**Nota:** Si ya tienes una API key de Gemini de antes, solo necesitas agregarla al archivo `.env`. Si no la tienes, sigue los pasos arriba para obtener una nueva.


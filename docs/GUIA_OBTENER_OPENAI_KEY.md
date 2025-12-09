# 🔑 Guía: Cómo Obtener tu API Key de OpenAI

## 📋 Pasos para Obtener tu API Key

### **Paso 1: Crear Cuenta en OpenAI**

1. Ve a: **https://platform.openai.com/**
2. Haz clic en **"Sign up"** o **"Log in"** si ya tienes cuenta
3. Si es primera vez, completa el registro con tu email

---

### **Paso 2: Acceder a las API Keys**

1. Una vez dentro, haz clic en tu **nombre de usuario** (esquina superior derecha)
2. Selecciona **"View API keys"** o ve directamente a:
   **https://platform.openai.com/api-keys**

---

### **Paso 3: Crear una Nueva API Key**

1. En la página de API Keys, haz clic en **"Create new secret key"**
2. Dale un nombre descriptivo (ej: "Asistente GEA")
3. Haz clic en **"Create secret key"**
4. **⚠️ IMPORTANTE:** Copia la key inmediatamente - solo se muestra UNA vez
5. Guárdala en un lugar seguro

---

### **Paso 4: Configurar en tu Proyecto**

1. Ve a la carpeta `backend` de tu proyecto
2. Abre o crea el archivo `.env`
3. Agrega esta línea:

```env
OPENAI_API_KEY=sk-tu-api-key-aqui
```

**Ejemplo:**
```env
OPENAI_API_KEY=sk-proj-abc123xyz789...
```

4. Guarda el archivo

---

### **Paso 5: Instalar la Librería (si no está instalada)**

```bash
cd backend
pip install openai
```

O si usas el entorno virtual:

```bash
cd backend
.\venv\Scripts\activate
pip install openai
```

---

### **Paso 6: Reiniciar el Backend**

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

## 🆓 Información sobre el Plan Gratuito

### **¿Tiene plan gratuito OpenAI?**

**Respuesta corta:** OpenAI ya **no ofrece plan gratuito** permanente desde 2023.

**Opciones disponibles:**

1. **Créditos iniciales** (para nuevos usuarios):
   - Algunos usuarios nuevos reciben $5 USD de crédito gratuito
   - Se agota después de usar los créditos
   - No se renueva automáticamente

2. **Pay-as-you-go** (Pago por uso):
   - Precios muy bajos para GPT-3.5-turbo
   - ~$0.0015 por 1K tokens (muy económico)
   - Solo pagas por lo que usas

### **Costos Aproximados:**

- **GPT-3.5-turbo**: ~$0.0015 por 1K tokens de entrada
- **Ejemplo**: 1000 mensajes cortos ≈ $1-2 USD

---

## ⚠️ Alternativas Gratuitas

Si buscas una alternativa **completamente gratuita**, considera:

### **1. Hugging Face (Gratis)**
- Modelos open-source gratuitos
- API gratuita con límites

### **2. Cohere (Tier Gratuito)**
- Tiene plan gratuito con límites
- Buena calidad

### **3. Continuar solo con Gemini**
- Ya tienes múltiples modelos de Gemini configurados
- El cambio automático entre modelos te da más disponibilidad

---

## 📝 Notas Importantes

1. **Seguridad:**
   - ⚠️ **NUNCA** subas tu `.env` a GitHub
   - El archivo `.env` ya debería estar en `.gitignore`

2. **Verificación:**
   - Después de agregar la key, al iniciar el backend deberías ver:
   ```
   ✓ OpenAI inicializado. Modelos disponibles: gpt-3.5-turbo
   ```

3. **Si no funciona:**
   - Verifica que la key esté correctamente en `.env`
   - Verifica que no haya espacios extras
   - Asegúrate de haber instalado `openai` con pip
   - Revisa que tengas créditos en tu cuenta OpenAI

---

## 🔗 Enlaces Útiles

- **Crear cuenta/Login**: https://platform.openai.com/
- **API Keys**: https://platform.openai.com/api-keys
- **Documentación**: https://platform.openai.com/docs
- **Precios**: https://openai.com/pricing
- **Billing**: https://platform.openai.com/account/billing

---

## ✅ Checklist Rápido

- [ ] Crear cuenta en OpenAI
- [ ] Ir a API Keys
- [ ] Crear nueva secret key
- [ ] Copiar la key
- [ ] Agregar a `backend/.env`
- [ ] Instalar: `pip install openai`
- [ ] Reiniciar backend
- [ ] Verificar que aparece en la lista de modelos

---

**Nota:** Si no quieres usar OpenAI (por el costo), el sistema funciona perfectamente solo con Gemini. La integración de OpenAI es **opcional** y solo se activa si configuras la API key.


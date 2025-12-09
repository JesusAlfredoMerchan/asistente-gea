# 🔌 Guía de APIs - Asistente Inteligente GEA

Esta guía documenta todos los endpoints disponibles en la API REST del Asistente GEA.

## 📋 Base URL

**Desarrollo:**
```
http://localhost:8000
```

**Producción:**
```
https://tu-backend-url.onrender.com
```

---

## 📡 Endpoints Disponibles

### 1. POST `/api/chat`

Enviar un mensaje al asistente y recibir una respuesta.

**Endpoint:** `POST /api/chat`

**Descripción:** Endpoint principal para interactuar con el asistente. Procesa el mensaje del usuario, busca información relevante en la base de conocimiento y genera una respuesta usando IA.

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Formato de Request:**

```json
{
  "message": "¿Cómo creo una nueva tarea?",
  "conversation_id": "uuid-opcional"
}
```

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `message` | string | ✅ Sí | Mensaje del usuario |
| `conversation_id` | string | ❌ No | ID de la conversación para mantener contexto. Si no se proporciona, se crea uno nuevo |

**Formato de Response:**

**Éxito (200 OK):**
```json
{
  "response": "Para crear una nueva tarea en GEA, sigue estos pasos:\n\n1. Accede al módulo de Tareas\n2. Click en 'Nueva Tarea'\n3. Completa los campos requeridos\n4. Guarda la tarea",
  "conversation_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "suggestions": [
    "¿Cómo edito una tarea existente?",
    "¿Qué campos son obligatorios en una tarea?",
    "¿Cómo asigno una tarea a un usuario?"
  ]
}
```

**Campos de Response:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `response` | string | Respuesta generada por el asistente |
| `conversation_id` | string | UUID de la conversación (usar en próximas peticiones) |
| `suggestions` | array[string] | Sugerencias de preguntas relacionadas (opcional) |

**Errores:**

- `400 Bad Request`: Mensaje vacío o formato inválido
- `500 Internal Server Error`: Error al procesar el mensaje

**Ejemplo con cURL:**

```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "¿Cómo creo una nueva tarea?",
    "conversation_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  }'
```

**Ejemplo con JavaScript (fetch):**

```javascript
const response = await fetch('http://localhost:8000/api/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: '¿Cómo creo una nueva tarea?',
    conversation_id: 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
  })
});

const data = await response.json();
console.log(data.response);
```

---

### 2. GET `/api/suggestions`

Obtener sugerencias de preguntas comunes.

**Endpoint:** `GET /api/suggestions`

**Descripción:** Retorna una lista de preguntas sugeridas que el usuario puede hacer al asistente.

**Formato de Request:**

No requiere body ni parámetros.

**Formato de Response:**

**Éxito (200 OK):**
```json
{
  "suggestions": [
    "¿Qué es GEA y para qué sirve?",
    "¿Cómo creo una nueva tarea?",
    "¿Cómo configuro un proceso?",
    "¿Qué son los informes y cómo los genero?",
    "¿Cómo gestiono usuarios en el sistema?"
  ]
}
```

**Campos de Response:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `suggestions` | array[string] | Lista de preguntas sugeridas |

**Ejemplo con cURL:**

```bash
curl -X GET "http://localhost:8000/api/suggestions"
```

---

### 3. GET `/api/models`

Obtener información sobre modelos de IA disponibles y su estado.

**Endpoint:** `GET /api/models`

**Descripción:** Retorna información sobre los modelos de IA disponibles, el modelo actual activo, y el estado de cuotas de cada modelo.

**Formato de Request:**

No requiere body ni parámetros.

**Formato de Response:**

**Éxito (200 OK):**
```json
{
  "current_model": "models/gemini-2.5-flash-lite",
  "available_models": [
    "models/gemini-2.5-flash-lite",
    "models/gemma-3-1b-it",
    "openai:gpt-3.5-turbo"
  ],
  "models_quota_status": {
    "models/gemini-2.5-flash-lite": {
      "exceeded": false,
      "request_count": 5,
      "remaining_time": null,
      "is_current": true,
      "available": true
    },
    "models/gemma-3-1b-it": {
      "exceeded": false,
      "request_count": 0,
      "remaining_time": null,
      "is_current": false,
      "available": true
    },
    "openai:gpt-3.5-turbo": {
      "exceeded": false,
      "request_count": 0,
      "remaining_time": null,
      "is_current": false,
      "available": true
    }
  }
}
```

**Campos de Response:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `current_model` | string | Nombre del modelo actualmente activo |
| `available_models` | array[string] | Lista de todos los modelos disponibles |
| `models_quota_status` | object | Estado detallado de cada modelo |

**Estructura de `models_quota_status[model_name]`:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `exceeded` | boolean | Si la cuota del modelo está excedida |
| `request_count` | number | Número de requests realizados |
| `remaining_time` | object/null | Tiempo restante hasta que se libere la cuota (si está excedida) |
| `is_current` | boolean | Si este es el modelo actualmente activo |
| `available` | boolean | Si el modelo está disponible para usar |

**Ejemplo con cURL:**

```bash
curl -X GET "http://localhost:8000/api/models"
```

---

### 4. POST `/api/models/change`

Cambiar el modelo de IA activo manualmente.

**Endpoint:** `POST /api/models/change`

**Descripción:** Permite cambiar el modelo de IA que se está usando para generar respuestas.

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Formato de Request:**

```json
{
  "model_name": "models/gemini-2.5-flash-lite"
}
```

**Parámetros:**

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `model_name` | string | ✅ Sí | Nombre del modelo a activar (debe estar en `available_models`) |

**Formato de Response:**

**Éxito (200 OK):**
```json
{
  "success": true,
  "message": "Modelo cambiado exitosamente a models/gemini-2.5-flash-lite",
  "current_model": "models/gemini-2.5-flash-lite"
}
```

**Error (400 Bad Request):**
```json
{
  "success": false,
  "message": "Modelo no disponible o no encontrado"
}
```

**Campos de Response:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `success` | boolean | Si el cambio fue exitoso |
| `message` | string | Mensaje descriptivo del resultado |
| `current_model` | string | Modelo actualmente activo (solo si success es true) |

**Errores:**

- `400 Bad Request`: Modelo no disponible o no encontrado
- `500 Internal Server Error`: Error al cambiar el modelo

**Ejemplo con cURL:**

```bash
curl -X POST "http://localhost:8000/api/models/change" \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "models/gemini-2.5-flash-lite"
  }'
```

---

### 5. GET `/api/health`

Verificar el estado del servicio.

**Endpoint:** `GET /api/health`

**Descripción:** Endpoint de salud para verificar que el servicio esté funcionando correctamente.

**Formato de Request:**

No requiere body ni parámetros.

**Formato de Response:**

**Éxito (200 OK):**
```json
{
  "status": "healthy",
  "assistant_loaded": true
}
```

**Campos de Response:**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `status` | string | Estado del servicio (`"healthy"` o `"unhealthy"`) |
| `assistant_loaded` | boolean | Si el asistente está cargado y listo |

**Ejemplo con cURL:**

```bash
curl -X GET "http://localhost:8000/api/health"
```

---

## 🔐 Autenticación

Actualmente, la API no requiere autenticación. En producción, se recomienda implementar autenticación basada en tokens.

## 🌐 CORS

La API está configurada para permitir peticiones desde orígenes específicos. En producción, configura `ALLOWED_ORIGINS` en las variables de entorno del backend.

## 📝 Notas Importantes

1. **Conversation ID**: Usa el mismo `conversation_id` en múltiples peticiones para mantener el contexto de la conversación.

2. **Rate Limiting**: Los modelos de IA tienen límites de cuota. El sistema cambiará automáticamente a otro modelo si se excede la cuota.

3. **Timeout**: Las peticiones tienen un timeout de 10 segundos en el frontend. Respuestas más largas pueden tardar más.

4. **Formato de Respuestas**: Las respuestas están en formato Markdown y pueden incluir listas, enlaces y formato de texto.

---

## 🧪 Ejemplos Completos

### Flujo de Conversación Completo

```javascript
// 1. Obtener sugerencias iniciales
const suggestionsResponse = await fetch('http://localhost:8000/api/suggestions');
const { suggestions } = await suggestionsResponse.json();

// 2. Enviar primer mensaje
const firstMessage = await fetch('http://localhost:8000/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: suggestions[0]
  })
});
const firstData = await firstMessage.json();
const conversationId = firstData.conversation_id;

// 3. Continuar la conversación con el mismo conversation_id
const followUp = await fetch('http://localhost:8000/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: '¿Puedes darme más detalles?',
    conversation_id: conversationId
  })
});
const followUpData = await followUp.json();

// 4. Verificar estado de modelos
const modelsStatus = await fetch('http://localhost:8000/api/models');
const modelsData = await modelsStatus.json();
console.log('Modelo actual:', modelsData.current_model);
```

---

## 🔗 Recursos Adicionales

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Gemini AI](https://ai.google.dev/docs)
- [Documentación de OpenAI](https://platform.openai.com/docs)

---

**Última actualización**: 2024


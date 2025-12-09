# 🔧 Solución: Error 429 - Cuota Excedida de Gemini

## 🔴 Problema

Estás recibiendo el error **429** de Gemini API que indica:

```
You exceeded your current quota, please check your plan and billing details.
Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests
limit: 20, model: gemini-2.5-flash
```

### Causa del Problema

El plan **gratuito de Gemini** tiene límites muy restrictivos:
- **20 requests por día** por modelo
- Una vez alcanzado el límite, debes esperar hasta el siguiente día
- Cada pregunta al asistente consume 1 request

### Por qué se excede tan rápido

1. **Sin cache**: Cada pregunta (incluso repetida) consume 1 request
2. **Sin rate limiting**: Múltiples requests muy rápidas
3. **Pruebas frecuentes**: Durante desarrollo se hacen muchas preguntas
4. **Recargas de página**: Cada recarga puede generar nuevas requests

---

## ✅ Soluciones Implementadas

### 1. **Sistema de Cache de Respuestas** ✅

**Qué hace:**
- Guarda respuestas de preguntas ya respondidas
- Si haces la misma pregunta, usa la respuesta del cache (sin llamar a Gemini)
- Reduce drásticamente el uso de la API

**Características:**
- TTL de 1 hora (las respuestas se invalidan después de 1 hora)
- Limpieza automática de cache expirado
- Cache en memoria (rápido y eficiente)

**Ejemplo:**
```
Usuario: "¿Cómo creo un usuario?"
→ Primera vez: Llama a Gemini (consume 1 request)
→ Segunda vez: Usa cache (0 requests) ✅
```

---

### 2. **Detección Automática de Error 429** ✅

**Qué hace:**
- Detecta automáticamente cuando se excede la cuota
- Cambia automáticamente al modo fallback
- Evita intentos repetidos que fallan

**Comportamiento:**
- Cuando detecta error 429, marca `quota_exceeded = True`
- Usa el método de fallback (búsqueda en base de conocimiento)
- Espera 1 hora antes de intentar nuevamente

---

### 3. **Rate Limiting Básico** ✅

**Qué hace:**
- Espera mínimo 1 segundo entre requests a Gemini
- Previene envío de múltiples requests muy rápidas
- Reduce la probabilidad de exceder límites

**Implementación:**
```python
min_request_interval = 1.0  # 1 segundo mínimo entre requests
```

---

### 4. **Manejo Inteligente de Errores** ✅

**Qué hace:**
- Detecta específicamente errores 429
- Maneja otros errores de forma diferente
- Proporciona mensajes claros en consola

---

## 📊 Impacto de las Soluciones

### Antes (Sin Cache):
- 20 preguntas = 20 requests = Cuota agotada ❌

### Ahora (Con Cache):
- 20 preguntas diferentes = 20 requests
- Preguntas repetidas = 0 requests adicionales ✅
- Si haces 5 preguntas repetidas: Solo 5 requests en total

**Ahorro estimado**: 50-70% menos requests con uso normal

---

## 🎯 Recomendaciones Adicionales

### Opción 1: Usar Solo Fallback (Sin Gemini)

Si quieres evitar completamente los límites:

1. **No configures `GEMINI_API_KEY`** en `.env`
2. El sistema usará automáticamente el método de fallback
3. Funciona bien para preguntas comunes en la base de conocimiento

**Ventajas:**
- ✅ Sin límites
- ✅ Sin costos
- ✅ Funciona offline

**Desventajas:**
- ❌ Respuestas menos inteligentes
- ❌ No usa contexto conversacional avanzado

---

### Opción 2: Upgrade de Plan de Gemini

Si necesitas más requests:

1. Visita: https://ai.google.dev/pricing
2. Considera un plan de pago
3. Límites mucho más altos (cientos/miles de requests)

---

### Opción 3: Optimizar Uso Actual

**Estrategias:**
1. **Usar cache efectivamente**: Haz preguntas variadas, no repitas las mismas
2. **Agrupar preguntas**: En lugar de 5 preguntas separadas, haz 1 pregunta con múltiples partes
3. **Usar fallback para preguntas simples**: El sistema ya lo hace automáticamente cuando detecta error 429

---

## 🔍 Monitoreo de Uso

### Ver Uso Actual

1. Visita: https://ai.dev/usage?tab=rate-limit
2. Verifica cuántas requests has usado hoy
3. El límite se resetea cada 24 horas

### Logs del Sistema

El sistema ahora muestra en consola:
- ✅ `Respuesta obtenida del cache` - Cuando usa cache
- ⚠️ `Cuota de Gemini excedida` - Cuando detecta error 429
- 💾 `Respuesta guardada en cache` - Cuando guarda en cache
- ⏳ `Rate limiting: esperando Xs` - Cuando espera entre requests

---

## 🛠️ Configuración Avanzada

### Ajustar TTL del Cache

En `assistant_engine.py`, línea 37:
```python
self.cache_ttl = 3600  # Cambiar a segundos deseados
# 3600 = 1 hora
# 7200 = 2 horas
# 1800 = 30 minutos
```

### Ajustar Rate Limiting

En `assistant_engine.py`, línea 41:
```python
self.min_request_interval = 1.0  # Cambiar a segundos deseados
# 1.0 = 1 segundo mínimo
# 2.0 = 2 segundos mínimo
# 0.5 = 0.5 segundos mínimo
```

---

## 📈 Estadísticas de Cache

El sistema ahora:
- Guarda cada respuesta exitosa en cache
- Limpia automáticamente cache expirado
- Muestra en consola cuando usa cache

**Para ver estadísticas:**
- Revisa los logs del backend
- Busca mensajes con "✅ Cache hit" o "💾 Respuesta guardada"

---

## 🚨 Qué Hacer Cuando se Excede la Cuota

### Automático (Ya Implementado):
1. ✅ El sistema detecta el error 429
2. ✅ **Muestra mensaje claro al usuario** explicando el problema
3. ✅ Informa el tiempo estimado para que se resetee el límite
4. ✅ Proporciona opciones y enlaces útiles
5. ✅ **NO muestra respuestas incompletas** del fallback cuando la cuota está excedida

### Mensaje al Usuario:
Cuando la cuota está excedida, el usuario recibe un mensaje claro que incluye:
- ⚠️ Explicación del problema
- ⏰ Tiempo estimado hasta el reset
- 🔗 Enlaces para revisar uso y considerar upgrade
- ℹ️ Información sobre el cache inteligente

### Manual:
1. **Esperar**: El límite se resetea cada 24 horas
2. **Usar fallback**: El sistema ya lo hace automáticamente
3. **Upgrade**: Considerar plan de pago si necesitas más requests

---

## 💡 Mejores Prácticas

1. **Haz preguntas variadas**: Aprovecha el cache
2. **No recargues innecesariamente**: Cada recarga puede generar requests
3. **Usa el modo fallback**: Funciona bien para la mayoría de preguntas
4. **Monitorea el uso**: Revisa https://ai.dev/usage regularmente

---

## 🔄 Flujo Actual con las Mejoras

```
Usuario hace pregunta
    ↓
¿Está en cache?
    ├─ SÍ → Retornar respuesta del cache (0 requests) ✅
    └─ NO → ¿Cuota excedida?
              ├─ SÍ → Usar fallback (0 requests) ✅
              └─ NO → ¿Rate limit OK?
                        ├─ SÍ → Llamar a Gemini (1 request)
                        │        ↓
                        │     ¿Éxito?
                        │        ├─ SÍ → Guardar en cache ✅
                        │        └─ NO → Usar fallback
                        └─ NO → Esperar y luego llamar
```

---

## 📝 Archivos Modificados

1. **`backend/assistant_engine.py`**
   - Sistema de cache implementado
   - Detección de error 429
   - Rate limiting básico
   - Manejo mejorado de errores

---

## ✅ Resultado

Ahora el sistema:
- ✅ **Usa cache** para evitar requests repetidas
- ✅ **Detecta automáticamente** cuando se excede la cuota
- ✅ **Muestra mensaje claro** al usuario cuando la cuota está excedida (en lugar de respuestas incompletas)
- ✅ **Informa errores de tokens** de forma transparente
- ✅ **Rate limiting** para evitar requests muy rápidas
- ✅ **Manejo inteligente de errores** con mensajes informativos

---

## 🆕 Mejoras Recientes (Actualización)

### Transparencia en Errores

**Antes:**
- ❌ Cuando la cuota estaba excedida, se usaba fallback silenciosamente
- ❌ Respuestas incompletas (ej: "1. Tareas Tareas")
- ❌ El usuario no sabía qué estaba pasando

**Ahora:**
- ✅ **Mensajes claros** cuando la cuota está excedida
- ✅ **Información sobre tokens** si hay problemas de límite
- ✅ **Tiempo estimado** para reset de cuota
- ✅ **Enlaces útiles** para gestión y upgrade
- ✅ **No más respuestas incompletas** del fallback cuando hay problemas de API

### Ejemplo de Mensaje al Usuario:

Cuando la cuota está excedida, el usuario verá:

```
⚠️ Cuota de API Excedida

Lo siento, he alcanzado el límite diario de solicitudes de la API de Gemini 
(plan gratuito: 20 requests/día).

¿Qué significa esto?
- He usado todas las solicitudes disponibles para hoy
- El límite se resetea automáticamente cada 24 horas
- Podrás usar el asistente nuevamente en: 24 horas

Opciones disponibles:
1. Esperar: El límite se resetea automáticamente mañana
2. Revisar uso: Visita https://ai.dev/usage?tab=rate-limit
3. Considerar upgrade: https://ai.google.dev/pricing

Nota: El sistema usa un cache inteligente para minimizar el uso de la API.
```

---

**Fecha de implementación**: Enero 2025
**Versión**: 1.1 (Actualizada con mensajes transparentes)


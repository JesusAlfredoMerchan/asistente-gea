# 📚 Diseño Conversacional - Documentación Completa

## 🎯 Visión General

Esta documentación define la arquitectura conversacional del Asistente Inteligente GEA, incluyendo casos de uso, flujos conversacionales, intents y configuraciones técnicas.

---

## 📑 Documentos Disponibles

### 1. [CASOS_DE_USO.md](./CASOS_DE_USO.md)
**Contenido**:
- ✅ Personas y roles de usuario
- ✅ 10 casos de uso principales definidos
- ✅ Flujos detallados por caso de uso
- ✅ Intents y entidades
- ✅ Escenarios especiales
- ✅ Métricas de éxito

**Útil para**: Entender qué puede hacer el asistente y cómo lo usa cada tipo de usuario

---

### 2. [FLUJOS_CONVERSACIONALES.md](./FLUJOS_CONVERSACIONALES.md)
**Contenido**:
- ✅ Principios de diseño conversacional
- ✅ Estructura de diálogos
- ✅ Flujos por tipo de usuario (Nuevo, Regular, Administrador)
- ✅ 5 plantillas de respuesta completas
- ✅ Manejo de errores y excepciones
- ✅ Diagramas de flujo
- ✅ Patrones conversacionales

**Útil para**: Diseñar cómo debe fluir cada conversación y cómo responder

---

### 3. [CONFIGURACION_INTENTS.md](./CONFIGURACION_INTENTS.md)
**Contenido**:
- ✅ 10 intents configurados con JSON
- ✅ Estructura de plantillas de respuesta
- ✅ Base de datos de procedimientos
- ✅ Ejemplos de procesamiento
- ✅ Estructura de implementación sugerida

**Útil para**: Implementación técnica y configuración del sistema

---

## 🗺️ Guía de Uso de la Documentación

### Para Diseñadores UX/Conversacionales

1. **Empezar con**: [CASOS_DE_USO.md](./CASOS_DE_USO.md)
   - Entender personas y necesidades
   - Revisar casos de uso completos

2. **Continuar con**: [FLUJOS_CONVERSACIONALES.md](./FLUJOS_CONVERSACIONALES.md)
   - Ver plantillas de respuesta
   - Entender patrones conversacionales

3. **Referencia**: [CONFIGURACION_INTENTS.md](./CONFIGURACION_INTENTS.md)
   - Ver estructura técnica si necesitas detalles

---

### Para Desarrolladores

1. **Empezar con**: [CONFIGURACION_INTENTS.md](./CONFIGURACION_INTENTS.md)
   - Ver estructura de intents y plantillas
   - Entender cómo se procesan las preguntas

2. **Referencia**: [FLUJOS_CONVERSACIONALES.md](./FLUJOS_CONVERSACIONALES.md)
   - Ver manejo de errores
   - Entender flujos técnicos

3. **Contexto**: [CASOS_DE_USO.md](./CASOS_DE_USO.md)
   - Entender el "por qué" detrás de cada decisión

---

### Para Product Owners/Stakeholders

1. **Leer**: [CASOS_DE_USO.md](./CASOS_DE_USO.md)
   - Ver qué puede hacer el asistente
   - Entender casos de uso y métricas

2. **Revisar**: [FLUJOS_CONVERSACIONALES.md](./FLUJOS_CONVERSACIONALES.md) (sección de principios y patrones)
   - Entender la experiencia de usuario

---

## 🎯 Casos de Uso Principales Resumidos

| ID | Nombre | Descripción | Prioridad |
|----|--------|-------------|-----------|
| CU-001 | Información General | Consultar qué es GEA y sus características | Alta |
| CU-002 | Procedimientos | Obtener guías paso a paso | Alta |
| CU-003 | Conceptos | Entender términos y conceptos | Alta |
| CU-004 | Explorar Módulo | Conocer un módulo específico | Media |
| CU-005 | Resolver Problema | Solucionar errores o problemas | Alta |
| CU-006 | Navegación Contextual | Mantener contexto en conversación | Alta |
| CU-007 | Preguntas Frecuentes | Respuestas rápidas a preguntas comunes | Media |
| CU-008 | Búsqueda Específica | Buscar información puntual | Media |
| CU-009 | Comparar Conceptos | Entender diferencias entre conceptos | Baja |
| CU-010 | Información No Disponible | Manejar preguntas sin respuesta | Media |

---

## 🔄 Flujos Conversacionales Clave

### Flujo 1: Procedimiento Simple
```
Usuario pregunta → Identificar procedimiento → Mostrar pasos → Verificar comprensión → Seguimiento
```

### Flujo 2: Exploración
```
Usuario pregunta sobre módulo → Descripción general → Profundizar según interés → Navegación
```

### Flujo 3: Resolución de Problema
```
Usuario reporta problema → Diagnosticar → Proponer solución → Verificar → Alternativas
```

### Flujo 4: Aprendizaje Conceptual
```
Usuario pregunta concepto → Definir → Ejemplos → Relaciones → Aplicación práctica
```

---

## 🎭 Intents Definidos

| Intent ID | Nombre | Ejemplos de Uso |
|-----------|--------|-----------------|
| `greeting` | Saludo | "Hola", "Buenos días" |
| `ask_what_is` | Preguntar qué es | "¿Qué es un perfil?" |
| `ask_how_to` | Preguntar cómo hacer | "¿Cómo creo un usuario?" |
| `explore_module` | Explorar módulo | "Háblame del módulo de Tareas" |
| `solve_problem` | Resolver problema | "No puedo crear un usuario" |
| `compare_concepts` | Comparar | "¿Cuál es la diferencia entre X e Y?" |
| `request_examples` | Solicitar ejemplos | "Dame un ejemplo" |
| `clarification_request` | Aclaración | "No entiendo", "Explícame mejor" |
| `navigation` | Navegación | "Volver", "Cambiar de tema" |
| `unknown_intent` | Desconocido | Fallback para intents no reconocidos |

---

## 📊 Plantillas de Respuesta

1. **procedure_template**: Procedimientos paso a paso
2. **concept_definition_template**: Definiciones de conceptos
3. **module_info_template**: Información de módulos
4. **problem_solution_template**: Resolución de problemas
5. **unknown_template**: Respuesta cuando no hay información

---

## 🔍 Escenarios Especiales Manejados

1. **Usuario Perdido**: Ofrecer menú de opciones
2. **Pregunta Ambigua**: Pedir aclaración
3. **Contexto Perdido**: Solicitar información necesaria
4. **Información No Disponible**: Ofrecer alternativas

---

## 📈 Métricas Objetivo

| Métrica | Objetivo |
|---------|----------|
| Tasa de Completitud | > 85% |
| Tiempo Promedio de Respuesta | < 2 segundos |
| Satisfacción del Usuario | > 4.5/5 |
| Claridad (aclaraciones necesarias) | < 2 por conversación |
| Tasa de Resolución de Problemas | > 70% |

---

## 🚀 Próximos Pasos

### Fase 1: Implementación Básica
- [ ] Implementar clasificador de intents básico
- [ ] Crear plantillas de respuesta
- [ ] Integrar con sistema actual

### Fase 2: Mejoras
- [ ] Machine Learning para intents
- [ ] Extracción avanzada de entidades
- [ ] Personalización por usuario

### Fase 3: Avanzado
- [ ] Análisis de sentimiento
- [ ] Multilenguaje
- [ ] Integración con GEA real

---

## 📝 Notas de Diseño

### Principios Clave

1. **Claridad**: Siempre preferir claridad sobre brevedad
2. **Contexto**: Mantener contexto de la conversación
3. **Proactividad**: Ofrecer ayuda antes de que se solicite
4. **Honestidad**: Reconocer limitaciones
5. **Flexibilidad**: Adaptarse a diferentes estilos de usuario

### Decisiones de Diseño

- **Mantener historial**: Últimos 10 turnos de conversación
- **Sugerencias**: Ofrecer 3-4 sugerencias relacionadas
- **Profundización**: Permitir detalle en cada paso de procedimiento
- **Navegación**: Siempre permitir cambiar de tema

---

## 🔗 Referencias

- [Base de Conocimiento GEA](../Base_Conocimiento_GEA.md)
- [Documentación Técnica](./documentacion.md)
- [Arquitectura del Sistema](./ARQUITECTURA.md)

---

## 📞 Contacto y Soporte

Para preguntas sobre el diseño conversacional:
- Revisar documentación específica en cada archivo
- Consultar ejemplos en cada documento
- Revisar casos de uso para escenarios específicos

---

**Última actualización**: Enero 2025
**Versión**: 1.0


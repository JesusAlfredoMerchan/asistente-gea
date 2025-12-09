# 📋 Casos de Uso - Asistente Inteligente GEA

## 📑 Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Personas y Roles](#personas-y-roles)
3. [Casos de Uso Principales](#casos-de-uso-principales)
4. [Flujos Conversacionales](#flujos-conversacionales)
5. [Intents y Entidades](#intents-y-entidades)
6. [Escenarios Especiales](#escenarios-especiales)

---

## 🎯 Visión General

El Asistente Inteligente GEA está diseñado para ayudar a usuarios de todos los niveles a:
- **Aprender** a usar el sistema GEA
- **Resolver dudas** sobre funcionalidades específicas
- **Seguir procedimientos** paso a paso
- **Entender conceptos** y terminología del sistema
- **Encontrar información** rápidamente sin consultar manuales

---

## 👥 Personas y Roles

### 1. **Usuario Nuevo**
- **Características**: Primera vez usando GEA, necesita orientación general
- **Necesidades**: Información básica, tutoriales, conceptos fundamentales
- **Objetivos**: Aprender a navegar y realizar tareas básicas

### 2. **Usuario Regular**
- **Características**: Conoce GEA pero necesita ayuda ocasional
- **Necesidades**: Procedimientos específicos, solución de problemas puntuales
- **Objetivos**: Resolver dudas rápidamente, optimizar su trabajo

### 3. **Administrador del Sistema**
- **Características**: Experto en GEA, configura y mantiene el sistema
- **Necesidades**: Información técnica, procedimientos avanzados, configuración
- **Objetivos**: Configurar, parametrizar y mantener el sistema

### 4. **Supervisor/Gerente**
- **Características**: Usa GEA para supervisar y tomar decisiones
- **Necesidades**: Informes, reportes, análisis de datos, visualizaciones
- **Objetivos**: Obtener información para toma de decisiones

---

## 🔄 Casos de Uso Principales

### CU-001: Consultar Información General sobre GEA

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario accede al asistente

**Flujo Principal**:
1. Usuario pregunta sobre qué es GEA o sus características
2. Asistente proporciona información general del sistema
3. Asistente ofrece información sobre módulos disponibles
4. Usuario puede hacer preguntas de seguimiento

**Flujo Alternativo**:
- Si el usuario pregunta algo muy específico, el asistente redirige al módulo correspondiente

**Criterios de Éxito**:
- Usuario entiende qué es GEA
- Usuario conoce los módulos principales
- Se proporcionan ejemplos claros

---

### CU-002: Obtener Guía Paso a Paso para un Procedimiento

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario sabe qué procedimiento necesita realizar

**Flujo Principal**:
1. Usuario pregunta "¿Cómo hago X?" (ej: "¿Cómo creo un usuario?")
2. Asistente identifica el procedimiento
3. Asistente presenta los pasos numerados
4. Usuario puede solicitar más detalles de cualquier paso
5. Usuario puede pedir que se repita algún paso

**Flujo Alternativo**:
- Si el procedimiento no existe, el asistente ofrece alternativas similares
- Si el usuario está perdido, ofrece volver al inicio del procedimiento

**Criterios de Éxito**:
- Pasos claros y ordenados
- Información suficiente para completar la tarea
- Posibilidad de obtener ayuda adicional

**Ejemplos**:
- "¿Cómo creo un nuevo usuario?"
- "¿Cómo asigno permisos a un perfil?"
- "¿Cómo inicio un nuevo proceso?"

---

### CU-003: Entender un Concepto o Término de GEA

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario encuentra un término desconocido

**Flujo Principal**:
1. Usuario pregunta qué es X (ej: "¿Qué es un perfil?")
2. Asistente proporciona definición clara
3. Asistente explica relación con otros conceptos
4. Asistente ofrece ejemplos prácticos
5. Usuario puede hacer preguntas relacionadas

**Flujo Alternativo**:
- Si el concepto no existe, buscar términos similares
- Si es muy técnico, proporcionar explicación simple primero

**Criterios de Éxito**:
- Definición clara y comprensible
- Contexto de uso
- Ejemplos prácticos

**Ejemplos**:
- "¿Qué es un perfil?"
- "¿Qué son las tareas pendientes?"
- "¿Qué es un flujo de trabajo?"

---

### CU-004: Explorar un Módulo Específico

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario quiere conocer un módulo

**Flujo Principal**:
1. Usuario pregunta sobre un módulo (ej: "Háblame del módulo de Tareas")
2. Asistente describe el módulo y sus funcionalidades
3. Asistente lista subsecciones principales
4. Usuario puede profundizar en cualquier aspecto
5. Asistente ofrece procedimientos relacionados

**Flujo Alternativo**:
- Si el módulo no existe, sugerir módulos similares
- Si el usuario no especifica, listar todos los módulos disponibles

**Criterios de Éxito**:
- Descripción completa del módulo
- Funcionalidades principales claras
- Navegación intuitiva a subsecciones

**Ejemplos**:
- "¿Qué hace el módulo de Procesos?"
- "Explícame el módulo de Seguridad"
- "¿Qué puedo hacer en el módulo de Informes?"

---

### CU-005: Resolver un Problema o Error

**Actor**: Usuario Regular / Administrador

**Precondiciones**: Usuario encuentra un problema al usar GEA

**Flujo Principal**:
1. Usuario describe el problema o error
2. Asistente identifica la causa probable
3. Asistente proporciona solución paso a paso
4. Usuario confirma si la solución funcionó
5. Si no funcionó, asistente ofrece alternativas

**Flujo Alternativo**:
- Si el problema no está documentado, sugerir contactar soporte
- Si es muy técnico, ofrecer información para administradores

**Criterios de Éxito**:
- Identificación correcta del problema
- Solución clara y aplicable
- Alternativas si la primera solución no funciona

**Ejemplos**:
- "No puedo crear un usuario"
- "¿Por qué no veo mis tareas?"
- "Mi proceso no avanza"

---

### CU-006: Navegar entre Temas Relacionados

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario está en medio de una conversación

**Flujo Principal**:
1. Usuario hace una pregunta relacionada con el tema anterior
2. Asistente mantiene el contexto de la conversación
3. Asistente responde usando información previa
4. Asistente puede referenciar mensajes anteriores
5. Usuario puede cambiar de tema en cualquier momento

**Flujo Alternativo**:
- Si el usuario cambia completamente de tema, el asistente adapta la respuesta
- Si el contexto es ambiguo, el asistente pregunta para aclarar

**Criterios de Éxito**:
- Mantenimiento correcto del contexto
- Respuestas coherentes con la conversación
- Transiciones suaves entre temas

**Ejemplos**:
```
Usuario: "¿Cómo creo un usuario?"
Asistente: [Proporciona pasos]
Usuario: "¿Y después de crearlo?"
Asistente: [Sabe que se refiere al usuario recién creado]
```

---

### CU-007: Obtener Información de Preguntas Frecuentes

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario tiene una pregunta común

**Flujo Principal**:
1. Usuario hace una pregunta frecuente
2. Asistente reconoce que es una pregunta común
3. Asistente proporciona respuesta directa y completa
4. Asistente ofrece información relacionada
5. Usuario puede profundizar si necesita más detalles

**Criterios de Éxito**:
- Respuesta rápida y precisa
- Información completa
- Enlaces a temas relacionados

**Ejemplos**:
- "¿Cómo inicio sesión en GEA?"
- "¿Puedo usar GEA desde mi móvil?"
- "¿Cómo exporto un informe?"

---

### CU-008: Búsqueda de Información Específica

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario busca información específica

**Flujo Principal**:
1. Usuario formula una pregunta específica
2. Asistente busca en la base de conocimiento
3. Asistente presenta información relevante
4. Si hay múltiples resultados, los organiza por relevancia
5. Usuario puede solicitar más detalles de cualquier resultado

**Flujo Alternativo**:
- Si no encuentra información, sugerir búsquedas similares
- Si hay demasiada información, priorizar lo más relevante

**Criterios de Éxito**:
- Información precisa y relevante
- Resultados organizados
- Opción de profundizar

---

### CU-009: Comparar Conceptos o Funcionalidades

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario quiere entender diferencias

**Flujo Principal**:
1. Usuario pregunta sobre diferencias entre dos conceptos
2. Asistente identifica ambos conceptos
3. Asistente compara características principales
4. Asistente proporciona tabla comparativa (si aplica)
5. Asistente explica cuándo usar cada uno

**Criterios de Éxito**:
- Diferencias claras y concisas
- Contexto de uso para cada opción
- Ejemplos prácticos

**Ejemplos**:
- "¿Cuál es la diferencia entre tareas pendientes y en proceso?"
- "¿Perfil y usuario son lo mismo?"
- "¿Qué diferencia hay entre procesos y flujos?"

---

### CU-010: Obtener Ayuda cuando No se Encuentra Información

**Actor**: Usuario (cualquier tipo)

**Precondiciones**: Usuario pregunta algo que no está en la base de conocimiento

**Flujo Principal**:
1. Usuario hace una pregunta
2. Asistente no encuentra información específica
3. Asistente reconoce honestamente que no tiene esa información
4. Asistente ofrece información relacionada que sí conoce
5. Asistente sugiere alternativas o contacto con soporte

**Criterios de Éxito**:
- Honestidad sobre limitaciones
- Ofrecer alternativas útiles
- Mantener buena experiencia de usuario

---

## 🎭 Flujos Conversacionales Detallados

### Flujo 1: Procedimiento Completo (Crear Usuario)

```
Usuario: "¿Cómo creo un usuario?"
         ↓
Asistente: "Te guío paso a paso para crear un nuevo usuario en GEA:
          1. Ingresar en el módulo Seguridad → Menú Administración → Usuarios
          2. Hacer clic en Nuevo Registro
          3. Completar los campos solicitados...
          
          ¿Quieres que explique algún paso con más detalle?"
         ↓
[Opciones del usuario]
- "Sí, explícame el paso 3" → Asistente detalla campos
- "¿Cuál es el mínimo de caracteres para la contraseña?" → Asistente responde
- "Gracias" → Asistente ofrece ayuda adicional
- "¿Y después de crear el usuario?" → Continúa con siguiente procedimiento
```

### Flujo 2: Exploración de Módulo

```
Usuario: "Háblame del módulo de Tareas"
         ↓
Asistente: "El módulo de Tareas en GEA te permite gestionar y controlar
          tareas relacionadas con diferentes procesos. Incluye:
          
          • Tareas Pendientes: Tareas asignadas que están pendientes...
          • Tareas Iniciadas: Control sobre tareas que has iniciado...
          • Tareas en Proceso: Visualización del estado...
          • Tareas Denegadas: Panel para tareas no aprobadas...
          
          ¿Sobre cuál aspecto te gustaría saber más?"
         ↓
[Opciones del usuario]
- "Tareas pendientes" → Profundiza en esa sección
- "¿Cómo veo mis tareas pendientes?" → Procedimiento específico
- "Gracias" → Finaliza
```

### Flujo 3: Resolución de Problema

```
Usuario: "No puedo crear un usuario, me da error"
         ↓
Asistente: "Entiendo. Para ayudarte mejor, necesito más información:
          
          • ¿Qué mensaje de error exacto aparece?
          • ¿Estás en el módulo Seguridad → Usuarios?
          • ¿Tienes permisos de administrador?
          
          Mientras tanto, las causas más comunes son:
          1. Falta de permisos
          2. Campos obligatorios incompletos
          3. Usuario ya existe..."
         ↓
Usuario: "Dice que no tengo permisos"
         ↓
Asistente: "El problema es de permisos. Para solucionarlo:
          
          1. Contacta al administrador del sistema
          2. El administrador debe asignar el perfil correcto...
          
          ¿Te explico cómo el administrador puede asignar permisos?"
```

### Flujo 4: Consulta Conceptual

```
Usuario: "¿Qué es un perfil?"
         ↓
Asistente: "Un perfil en GEA es un grupo de usuarios que comparten
          permisos y características similares. Es como un 'rol' que
          define qué puede hacer un usuario en el sistema.
          
          Características:
          • Se asignan permisos a nivel de perfil
          • Varios usuarios pueden tener el mismo perfil
          • Facilita la gestión de permisos
          
          ¿Te interesa saber cómo crear o asignar un perfil?"
         ↓
[Conversación continúa según interés del usuario]
```

---

## 🎯 Intents y Entidades

### Intents Principales

#### 1. **greeting** (Saludo)
- **Ejemplos**: "Hola", "Buenos días", "Hola, necesito ayuda"
- **Respuesta**: Mensaje de bienvenida + sugerencias

#### 2. **ask_what_is** (Preguntar qué es)
- **Ejemplos**: "¿Qué es un perfil?", "Explícame qué es GEA", "¿Qué son las tareas?"
- **Entidades**: [concepto]
- **Respuesta**: Definición + ejemplos + información relacionada

#### 3. **ask_how_to** (Preguntar cómo hacer)
- **Ejemplos**: "¿Cómo creo un usuario?", "¿Cómo asigno permisos?"
- **Entidades**: [acción], [objeto]
- **Respuesta**: Pasos numerados + opción de detalles

#### 4. **explore_module** (Explorar módulo)
- **Ejemplos**: "Háblame del módulo de Tareas", "¿Qué hace el módulo de Procesos?"
- **Entidades**: [módulo]
- **Respuesta**: Descripción completa + subsecciones

#### 5. **solve_problem** (Resolver problema)
- **Ejemplos**: "No puedo crear un usuario", "Tengo un error", "Algo no funciona"
- **Entidades**: [error], [módulo], [funcionalidad]
- **Respuesta**: Diagnóstico + solución paso a paso

#### 6. **compare_concepts** (Comparar conceptos)
- **Ejemplos**: "¿Cuál es la diferencia entre X e Y?", "¿X es lo mismo que Y?"
- **Entidades**: [concepto1], [concepto2]
- **Respuesta**: Comparación estructurada

#### 7. **request_examples** (Solicitar ejemplos)
- **Ejemplos**: "Dame un ejemplo", "¿Puedes darme un ejemplo práctico?"
- **Contexto**: Basado en conversación previa
- **Respuesta**: Ejemplo relevante al contexto

#### 8. **clarification_request** (Solicitar aclaración)
- **Ejemplos**: "¿Qué significa X?", "No entendí", "Explícame mejor"
- **Contexto**: Basado en mensaje previo del asistente
- **Respuesta**: Explicación más simple o detallada

#### 9. **navigation** (Navegación)
- **Ejemplos**: "Volver al inicio", "Cambiar de tema", "Ya entendí, gracias"
- **Respuesta**: Confirmación + nueva sugerencia o cierre

#### 10. **unknown_intent** (Intent desconocido)
- **Manejo**: Buscar en base de conocimiento, ofrecer alternativas

### Entidades Clave

#### Módulos
- `tareas`, `procesos`, `informes`, `mapas`, `parametros`, `tableros`, `seguridad`

#### Conceptos
- `usuario`, `perfil`, `permiso`, `tarea`, `proceso`, `flujo`, `actividad`, `actor`

#### Acciones
- `crear`, `asignar`, `gestionar`, `configurar`, `modificar`, `eliminar`, `ver`, `exportar`

#### Estados
- `pendiente`, `iniciada`, `en_proceso`, `denegada`, `completada`

---

## 🔀 Escenarios Especiales

### Escenario 1: Usuario Perdido

**Situación**: Usuario no sabe qué preguntar o está confundido

**Flujo**:
1. Asistente detecta confusión o pregunta muy genérica
2. Ofrece menú de opciones principales
3. Presenta sugerencias categorizadas
4. Ofrece guía de inicio rápido

**Ejemplo**:
```
Usuario: "Ayuda"
Asistente: "¡Por supuesto! Puedo ayudarte con:
          
          📚 **Información General**
          • ¿Qué es GEA?
          • ¿Qué módulos tiene?
          
          🛠️ **Procedimientos Comunes**
          • Crear usuarios
          • Asignar permisos
          • Gestionar tareas
          
          💡 **Conceptos**
          • ¿Qué es un perfil?
          • ¿Qué son las tareas pendientes?
          
          ¿Sobre qué tema te gustaría saber?"
```

### Escenario 2: Pregunta Ambigua

**Situación**: La pregunta puede referirse a múltiples cosas

**Flujo**:
1. Asistente identifica la ambigüedad
2. Presenta opciones de interpretación
3. Espera aclaración del usuario
4. Proporciona respuesta específica

**Ejemplo**:
```
Usuario: "Tareas"
Asistente: "Veo que preguntas sobre 'Tareas'. ¿Te interesa saber sobre:
          
          1. ¿Qué son las tareas en GEA? (concepto)
          2. ¿Cómo gestionar tareas? (procedimiento)
          3. ¿Módulo de Tareas? (información general)
          4. ¿Ver mis tareas pendientes? (acción específica)
          
          ¿Cuál de estas opciones te interesa?"
```

### Escenario 3: Contexto Perdido

**Situación**: Usuario pregunta algo que requiere contexto previo

**Flujo**:
1. Asistente reconoce necesidad de contexto
2. Solicita información necesaria
3. Proporciona respuesta con contexto

**Ejemplo**:
```
Usuario: "¿Y luego qué hago?"
Asistente: "Para ayudarte mejor, necesito saber a qué te refieres.
          
          ¿Estás hablando de:
          • Crear un usuario (conversación anterior)
          • Asignar permisos
          • Otro procedimiento
          
          O si prefieres, puedes contarme desde el inicio qué estás
          intentando hacer."
```

### Escenario 4: Información No Disponible

**Situación**: La información no está en la base de conocimiento

**Flujo**:
1. Asistente reconoce honestamente la limitación
2. Busca información relacionada
3. Ofrece alternativas
4. Sugiere contactar soporte si es necesario

**Ejemplo**:
```
Usuario: "¿Cómo cambio el logo del sistema?"
Asistente: "Lo siento, no tengo información específica sobre cómo
          cambiar el logo del sistema en mi base de conocimiento actual.
          
          Sin embargo, esto podría estar relacionado con:
          • Configuración de parámetros
          • Personalización del sistema
          • Administración avanzada
          
          Te recomiendo:
          1. Revisar el módulo de Parámetros
          2. Contactar al administrador del sistema
          3. Consultar el manual técnico de GEA
          
          ¿Te puedo ayudar con alguno de estos temas relacionados?"
```

---

## 📊 Métricas de Éxito por Caso de Uso

### CU-001 (Información General)
- Tasa de comprensión: > 90%
- Tiempo promedio de respuesta: < 2 segundos
- Seguimiento con preguntas relacionadas: > 60%

### CU-002 (Procedimientos)
- Tasa de completitud: > 85%
- Necesidad de aclaraciones: < 30%
- Satisfacción del usuario: > 4/5

### CU-003 (Conceptos)
- Claridad de definición: > 90%
- Ejemplos proporcionados: 100%
- Navegación a temas relacionados: > 50%

### CU-005 (Resolución de Problemas)
- Tasa de resolución: > 70%
- Tiempo promedio hasta solución: < 5 minutos
- Alternativas proporcionadas: 100%

---

**Última actualización**: Enero 2025


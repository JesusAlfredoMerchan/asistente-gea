# ⚙️ Configuración de Intents y Plantillas - Asistente GEA

## 📋 Estructura de Configuración

Este documento define la estructura de datos para intents, entidades y plantillas de respuesta que pueden ser implementadas en el sistema.

---

## 🎯 Intents Configurados

### Estructura JSON de Intent

```json
{
  "intent_id": "string",
  "intent_name": "string",
  "description": "string",
  "keywords": ["array", "of", "keywords"],
  "patterns": ["regex patterns"],
  "entities_required": ["entity1", "entity2"],
  "entities_optional": ["entity3"],
  "response_template": "template_id",
  "follow_up_questions": ["question1", "question2"],
  "confidence_threshold": 0.7
}
```

---

## 📝 Intents Definidos

### 1. greeting

```json
{
  "intent_id": "greeting",
  "intent_name": "Saludo",
  "description": "Usuario saluda o inicia conversación",
  "keywords": ["hola", "buenos días", "buenas tardes", "buenas noches", "hi", "hello", "saludos"],
  "patterns": [
    "^(hola|hi|hello|buenos días|buenas tardes|buenas noches)",
    "^(hola|hi).*necesito.*ayuda",
    "^(hola|hi).*asistente"
  ],
  "entities_required": [],
  "entities_optional": [],
  "response_template": "greeting_template",
  "follow_up_questions": [
    "¿En qué puedo ayudarte?",
    "¿Tienes alguna pregunta sobre GEA?",
    "¿Sobre qué módulo te gustaría saber?"
  ],
  "confidence_threshold": 0.8
}
```

---

### 2. ask_what_is

```json
{
  "intent_id": "ask_what_is",
  "intent_name": "Preguntar qué es",
  "description": "Usuario pregunta por la definición de un concepto",
  "keywords": ["qué es", "qué son", "definición", "explica", "qué significa", "hablame de"],
  "patterns": [
    "qué (es|son) (.+)",
    "qué significa (.+)",
    "explícame qué (es|son) (.+)",
    "hablame de (.+)",
    "definición de (.+)"
  ],
  "entities_required": ["concept"],
  "entities_optional": [],
  "response_template": "concept_definition_template",
  "follow_up_questions": [
    "¿Te interesa saber cómo usarlo?",
    "¿Quieres ver un ejemplo práctico?",
    "¿Te gustaría saber cómo se relaciona con otros conceptos?"
  ],
  "confidence_threshold": 0.75
}
```

**Conceptos reconocidos**:
- `usuario`, `perfil`, `permiso`, `tarea`, `proceso`, `flujo`, `actividad`, `actor`, `módulo`, `seguridad`, `parámetro`

---

### 3. ask_how_to

```json
{
  "intent_id": "ask_how_to",
  "intent_name": "Preguntar cómo hacer",
  "description": "Usuario solicita instrucciones para realizar una acción",
  "keywords": ["cómo", "como", "pasos", "procedimiento", "guía", "tutorial", "instrucciones"],
  "patterns": [
    "cómo (crear|asignar|gestionar|configurar|modificar|eliminar|ver|exportar) (.+)",
    "pasos para (.+)",
    "procedimiento para (.+)",
    "guía para (.+)",
    "(.+) paso a paso"
  ],
  "entities_required": ["action", "object"],
  "entities_optional": ["module"],
  "response_template": "procedure_template",
  "follow_up_questions": [
    "¿Quieres que explique algún paso con más detalle?",
    "¿Necesitas ayuda con algún paso específico?",
    "¿Te interesa saber qué hacer después de completar este procedimiento?"
  ],
  "confidence_threshold": 0.8
}
```

**Acciones reconocidas**:
- `crear`, `asignar`, `gestionar`, `configurar`, `modificar`, `eliminar`, `ver`, `exportar`, `iniciar`, `completar`

**Objetos reconocidos**:
- `usuario`, `perfil`, `permiso`, `tarea`, `proceso`, `informe`, `módulo`, `parámetro`

---

### 4. explore_module

```json
{
  "intent_id": "explore_module",
  "intent_name": "Explorar módulo",
  "description": "Usuario quiere conocer información sobre un módulo específico",
  "keywords": ["módulo", "module", "sección", "apartado"],
  "patterns": [
    "módulo de (.+)",
    "hablame del módulo (.+)",
    "qué hace el módulo (.+)",
    "información sobre el módulo (.+)",
    "explícame (.+)"
  ],
  "entities_required": ["module"],
  "entities_optional": [],
  "response_template": "module_info_template",
  "follow_up_questions": [
    "¿Sobre qué aspecto del módulo te gustaría saber más?",
    "¿Te interesa algún procedimiento específico de este módulo?",
    "¿Quieres ver cómo acceder a este módulo?"
  ],
  "confidence_threshold": 0.75
}
```

**Módulos reconocidos**:
- `tareas`, `procesos`, `informes`, `mapas`, `parámetros`, `tableros`, `seguridad`, `romana`, `proveedores`, `producción`, `mantenimiento`, `logística`, `laboratorio`, `contable`

---

### 5. solve_problem

```json
{
  "intent_id": "solve_problem",
  "intent_name": "Resolver problema",
  "description": "Usuario reporta un problema o error",
  "keywords": ["error", "problema", "no funciona", "no puedo", "tengo un", "ayuda con", "no sé cómo"],
  "patterns": [
    "tengo un (error|problema)",
    "no (puedo|funciona|sé cómo) (.+)",
    "error al (.+)",
    "problema con (.+)",
    "ayuda, (.+)"
  ],
  "entities_required": ["problem_description"],
  "entities_optional": ["module", "error_type"],
  "response_template": "problem_solution_template",
  "follow_up_questions": [
    "¿Qué mensaje de error exacto aparece?",
    "¿En qué módulo estás trabajando?",
    "¿Pudiste resolver el problema?"
  ],
  "confidence_threshold": 0.7
}
```

---

### 6. compare_concepts

```json
{
  "intent_id": "compare_concepts",
  "intent_name": "Comparar conceptos",
  "description": "Usuario quiere comparar dos conceptos o funcionalidades",
  "keywords": ["diferencia", "comparar", "cuál es la diferencia", "es lo mismo", "diferencia entre"],
  "patterns": [
    "diferencia entre (.+) y (.+)",
    "(.+) es lo mismo que (.+)",
    "comparar (.+) con (.+)",
    "cuál es la diferencia entre (.+) y (.+)"
  ],
  "entities_required": ["concept1", "concept2"],
  "entities_optional": [],
  "response_template": "comparison_template",
  "follow_up_questions": [
    "¿Te aclaró la diferencia?",
    "¿Quieres saber más sobre alguno de estos conceptos?"
  ],
  "confidence_threshold": 0.75
}
```

---

### 7. request_examples

```json
{
  "intent_id": "request_examples",
  "intent_name": "Solicitar ejemplos",
  "description": "Usuario solicita ejemplos prácticos",
  "keywords": ["ejemplo", "ejemplos", "muéstrame", "muestra", "ilustra"],
  "patterns": [
    "dame un ejemplo",
    "muéstrame un ejemplo",
    "ejemplos de (.+)",
    "ilustra (.+)"
  ],
  "entities_required": [],
  "entities_optional": ["concept"],
  "response_template": "example_template",
  "follow_up_questions": [
    "¿Te sirvió el ejemplo?",
    "¿Quieres ver otro ejemplo?"
  ],
  "confidence_threshold": 0.7
}
```

---

### 8. clarification_request

```json
{
  "intent_id": "clarification_request",
  "intent_name": "Solicitar aclaración",
  "description": "Usuario necesita más claridad sobre algo",
  "keywords": ["no entiendo", "no comprendo", "explícame mejor", "más detalles", "aclarar", "confundido"],
  "patterns": [
    "no (entiendo|comprendo)",
    "explícame mejor",
    "más detalles sobre (.+)",
    "aclarar (.+)",
    "estoy confundido"
  ],
  "entities_required": [],
  "entities_optional": ["topic"],
  "response_template": "clarification_template",
  "follow_up_questions": [
    "¿Ahora está más claro?",
    "¿Necesitas más información sobre algún punto específico?"
  ],
  "confidence_threshold": 0.8
}
```

---

### 9. navigation

```json
{
  "intent_id": "navigation",
  "intent_name": "Navegación",
  "description": "Usuario quiere cambiar de tema o finalizar",
  "keywords": ["volver", "cambiar", "otro tema", "gracias", "ya entendí", "listo"],
  "patterns": [
    "volver al inicio",
    "cambiar de tema",
    "otro tema",
    "(gracias|thanks|listo|ya entendí)",
    "terminar"
  ],
  "entities_required": [],
  "entities_optional": ["new_topic"],
  "response_template": "navigation_template",
  "follow_up_questions": [],
  "confidence_threshold": 0.8
}
```

---

### 10. unknown_intent

```json
{
  "intent_id": "unknown_intent",
  "intent_name": "Intent desconocido",
  "description": "No se pudo identificar claramente la intención",
  "keywords": [],
  "patterns": [],
  "entities_required": [],
  "entities_optional": [],
  "response_template": "unknown_template",
  "follow_up_questions": [
    "¿Puedes reformular tu pregunta?",
    "¿Te puedo ayudar con algo específico sobre GEA?",
    "¿Quieres ver las opciones disponibles?"
  ],
  "confidence_threshold": 0.0
}
```

---

## 📋 Plantillas de Respuesta

### Estructura de Plantilla

```json
{
  "template_id": "string",
  "template_name": "string",
  "template_type": "text|structured|interactive",
  "content": {
    "intro": "string",
    "body": "string|array",
    "outro": "string"
  },
  "variables": ["var1", "var2"],
  "formatting": {
    "use_markdown": true,
    "use_lists": true,
    "use_bold": true
  }
}
```

---

### Plantillas Definidas

#### greeting_template

```json
{
  "template_id": "greeting_template",
  "template_name": "Plantilla de Saludo",
  "template_type": "structured",
  "content": {
    "intro": "¡Hola! 👋 Soy tu asistente inteligente para GEA.",
    "body": [
      "Puedo ayudarte a:",
      "• Aprender a usar el sistema GEA",
      "• Resolver dudas sobre funcionalidades",
      "• Guiarte paso a paso en procedimientos",
      "• Entender conceptos y terminología"
    ],
    "outro": "¿En qué puedo ayudarte hoy?"
  },
  "variables": [],
  "formatting": {
    "use_markdown": true,
    "use_lists": true,
    "use_bold": false
  }
}
```

---

#### procedure_template

```json
{
  "template_id": "procedure_template",
  "template_name": "Plantilla de Procedimiento",
  "template_type": "structured",
  "content": {
    "intro": "Te guío paso a paso para {action} {object} en GEA:",
    "body": [
      "{steps}"
    ],
    "outro": "💡 Nota: {note}\n\n¿Quieres que explique algún paso con más detalle?"
  },
  "variables": ["action", "object", "steps", "note"],
  "formatting": {
    "use_markdown": true,
    "use_lists": true,
    "use_bold": true
  }
}
```

---

#### concept_definition_template

```json
{
  "template_id": "concept_definition_template",
  "template_name": "Plantilla de Definición",
  "template_type": "structured",
  "content": {
    "intro": "{concept} en GEA es {brief_definition}.",
    "body": [
      "{detailed_explanation}",
      "",
      "Se relaciona con:",
      "{related_concepts}",
      "",
      "Ejemplo: {example}"
    ],
    "outro": "¿Te interesa saber más sobre {suggested_topic}?"
  },
  "variables": [
    "concept",
    "brief_definition",
    "detailed_explanation",
    "related_concepts",
    "example",
    "suggested_topic"
  ],
  "formatting": {
    "use_markdown": true,
    "use_lists": true,
    "use_bold": true
  }
}
```

---

## 🗄️ Base de Datos de Procedimientos

### Estructura de Procedimiento

```json
{
  "procedure_id": "create_user",
  "procedure_name": "Crear un Nuevo Usuario",
  "module": "seguridad",
  "category": "administración",
  "difficulty": "beginner|intermediate|advanced",
  "estimated_time": "5 minutos",
  "requirements": ["Permisos de administrador"],
  "steps": [
    {
      "step_number": 1,
      "step_title": "Acceder al módulo",
      "step_description": "Ingresar en el módulo Seguridad → Menú Administración → Usuarios",
      "step_details": "Desde el menú principal, busca la sección de Seguridad..."
    },
    {
      "step_number": 2,
      "step_title": "Crear nuevo registro",
      "step_description": "Hacer clic en el botón 'Nuevo Registro'",
      "step_details": "El botón se encuentra en la parte superior de la lista de usuarios..."
    }
  ],
  "notes": [
    "Asegúrate de tener permisos de administrador",
    "La contraseña debe tener mínimo 8 caracteres"
  ],
  "related_procedures": ["assign_profile_to_user", "assign_permissions"],
  "related_concepts": ["usuario", "perfil", "permisos"]
}
```

---

## 📊 Ejemplos de Uso

### Ejemplo 1: Procesamiento de Pregunta

**Input del usuario**: "¿Cómo creo un usuario?"

**Procesamiento**:
1. Intent detectado: `ask_how_to` (confidence: 0.9)
2. Entidades extraídas:
   - `action`: "crear"
   - `object`: "usuario"
3. Procedimiento identificado: `create_user`
4. Plantilla aplicada: `procedure_template`
5. Variables rellenadas:
   - `action`: "crear"
   - `object`: "un nuevo usuario"
   - `steps`: [pasos del procedimiento]
   - `note`: "Requiere permisos de administrador"

**Output**:
```
Te guío paso a paso para crear un nuevo usuario en GEA:

1. Ingresar en el módulo Seguridad → Menú Administración → Usuarios
2. Hacer clic en Nuevo Registro
3. Completar los campos solicitados...
...

💡 Nota: Requiere permisos de administrador

¿Quieres que explique algún paso con más detalle?
```

---

### Ejemplo 2: Pregunta Conceptual

**Input del usuario**: "¿Qué es un perfil?"

**Procesamiento**:
1. Intent detectado: `ask_what_is` (confidence: 0.95)
2. Entidades extraídas:
   - `concept`: "perfil"
3. Concepto identificado en base de conocimiento
4. Plantilla aplicada: `concept_definition_template`
5. Variables rellenadas desde base de conocimiento

**Output**:
```
Un perfil en GEA es un grupo de usuarios que comparten permisos y características similares.

Los perfiles facilitan la gestión porque se asignan permisos al perfil y todos los usuarios con ese perfil los heredan automáticamente.

Se relaciona con:
• Usuarios
• Permisos
• Módulos

Ejemplo: Si tienes un perfil "Administrador", todos los usuarios con ese perfil tendrán permisos de administrador.

¿Te interesa saber cómo crear un nuevo perfil?
```

---

## 🔧 Implementación Sugerida

### Estructura de Archivos

```
backend/
├── config/
│   ├── intents.json          # Definición de intents
│   ├── templates.json        # Plantillas de respuesta
│   ├── procedures.json       # Base de procedimientos
│   └── concepts.json         # Base de conceptos
└── services/
    ├── intent_classifier.py  # Clasificador de intents
    ├── entity_extractor.py   # Extractor de entidades
    └── response_builder.py   # Constructor de respuestas
```

---

## 📈 Mejoras Futuras

1. **Machine Learning para Intent Classification**
   - Entrenar modelo con ejemplos etiquetados
   - Mejorar precisión de detección

2. **NLP Avanzado**
   - Análisis de sentimiento
   - Detección de urgencia
   - Identificación de emociones

3. **Personalización**
   - Adaptar respuestas según historial del usuario
   - Aprender preferencias de comunicación

4. **Multilenguaje**
   - Detección automática de idioma
   - Traducción de intents y plantillas

---

**Última actualización**: Enero 2025


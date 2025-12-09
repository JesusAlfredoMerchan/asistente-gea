# 💬 Diseño de Flujos Conversacionales - Asistente GEA

## 📑 Tabla de Contenidos

1. [Principios de Diseño](#principios-de-diseño)
2. [Estructura de Diálogos](#estructura-de-diálogos)
3. [Flujos por Tipo de Usuario](#flujos-por-tipo-de-usuario)
4. [Plantillas de Respuesta](#plantillas-de-respuesta)
5. [Manejo de Errores y Excepciones](#manejo-de-errores-y-excepciones)
6. [Diagramas de Flujo](#diagramas-de-flujo)

---

## 🎨 Principios de Diseño

### 1. **Claridad y Simplicidad**
- Lenguaje claro y directo
- Evitar jerga técnica innecesaria
- Explicaciones progresivas (simple → complejo)

### 2. **Contextualización**
- Mantener contexto de la conversación
- Referencias a mensajes anteriores cuando sea relevante
- Transiciones suaves entre temas

### 3. **Proactividad**
- Ofrecer sugerencias relevantes
- Anticipar necesidades del usuario
- Guiar al usuario cuando está perdido

### 4. **Flexibilidad**
- Permitir múltiples formas de expresar lo mismo
- Adaptarse al nivel de conocimiento del usuario
- Manejar desviaciones del flujo principal

### 5. **Honestidad**
- Reconocer cuando no se tiene información
- Admitir limitaciones
- Ofrecer alternativas útiles

---

## 🗣️ Estructura de Diálogos

### Componentes de un Diálogo

```
┌─────────────────────────────────────┐
│  1. SALUDO / ACERTIJO               │  ← Identificar intent
├─────────────────────────────────────┤
│  2. ENTENDIMIENTO                   │  ← Confirmar comprensión
├─────────────────────────────────────┤
│  3. INFORMACIÓN                     │  ← Proporcionar respuesta
├─────────────────────────────────────┤
│  4. CONFIRMACIÓN                    │  ← Verificar satisfacción
├─────────────────────────────────────┤
│  5. SEGUIMIENTO                     │  ← Ofrecer ayuda adicional
└─────────────────────────────────────┘
```

### Ejemplo Completo

```
[1. Saludo/Acertijo]
Usuario: "¿Cómo creo un usuario?"

[2. Entendimiento]
Asistente: "Te ayudo a crear un nuevo usuario en GEA. Este proceso
          requiere permisos de administrador."

[3. Información]
Asistente: "Pasos:
          1. Ingresar en Seguridad → Administración → Usuarios
          2. Clic en 'Nuevo Registro'
          3. Completar campos..."

[4. Confirmación]
Asistente: "¿Te gustaría que explique algún paso con más detalle?"

[5. Seguimiento]
Asistente: [Si usuario confirma entendimiento]
          "Perfecto. ¿También te interesa saber cómo asignar un
          perfil a ese usuario?"
```

---

## 👤 Flujos por Tipo de Usuario

### Flujo A: Usuario Nuevo

**Características**:
- Necesita más contexto
- Explicaciones más detalladas
- Guía paso a paso

**Estructura**:
```
1. Bienvenida extendida
   ↓
2. Explicación del concepto básico
   ↓
3. Procedimiento detallado con contexto
   ↓
4. Verificación de comprensión
   ↓
5. Próximos pasos sugeridos
```

**Ejemplo**:
```
Asistente: "¡Hola! 👋 Bienvenido al Asistente GEA.
          
          GEA es un sistema de gestión que te permite administrar
          procesos, tareas y datos de tu organización.
          
          Puedo ayudarte a:
          • Aprender a usar GEA
          • Resolver dudas específicas
          • Guiarte paso a paso en procedimientos
          
          Para empezar, ¿hay algo específico que te gustaría saber?"
```

---

### Flujo B: Usuario Regular

**Características**:
- Respuestas más directas
- Menos contexto necesario
- Enfoque en la solución

**Estructura**:
```
1. Saludo breve
   ↓
2. Respuesta directa
   ↓
3. Opciones adicionales si es necesario
```

**Ejemplo**:
```
Usuario: "¿Cómo asigno permisos?"
Asistente: "Para asignar permisos a un perfil:
          1. Seguridad → Parametrización → Seguridad
          2. Seleccionar 'Permisos Perfil'
          3. Elegir perfil y módulo
          4. Asignar permisos a menús
          5. Registrar
          
          ¿Necesitas ayuda con algún paso específico?"
```

---

### Flujo C: Administrador

**Características**:
- Información técnica
- Procedimientos avanzados
- Opciones de configuración

**Estructura**:
```
1. Confirmación de necesidad técnica
   ↓
2. Información detallada y técnica
   ↓
3. Consideraciones avanzadas
   ↓
4. Referencias adicionales
```

**Ejemplo**:
```
Usuario: "¿Cómo configuro la seguridad avanzada?"
Asistente: "Para configurar seguridad avanzada necesitas acceder a:
          
          **Configuración de Seguridad:**
          1. Módulo Seguridad → Parametrización
          2. Configurar políticas de contraseña
          3. Establecer tiempo de sesión
          4. Configurar autenticación multifactor (si aplica)
          
          **Consideraciones:**
          • Políticas de contraseña: mínimo 8 caracteres
          • Vigencia de usuario: 0 = indefinida
          • Logs de seguridad: consultar en Seguridad → Log
          
          ¿Necesitas detalles sobre alguna configuración específica?"
```

---

## 📝 Plantillas de Respuesta

### Plantilla 1: Procedimiento Paso a Paso

```
[INTRO]
Te guío paso a paso para [acción] en GEA:

[PASOS]
1. [Paso 1 - Acción específica]
2. [Paso 2 - Acción específica]
3. [Paso 3 - Acción específica]
   ...

[NOTAS IMPORTANTES]
💡 Nota: [Información relevante]

[FOLLOW-UP]
¿Quieres que explique algún paso con más detalle?
```

**Ejemplo Real**:
```
Te guío paso a paso para crear un nuevo usuario en GEA:

1. Ingresar en el módulo Seguridad → Menú Administración → Usuarios
2. Hacer clic en Nuevo Registro
3. Completar los campos:
   - Usuario: nombre.apellido
   - Descripción: Nombre completo
   - Contraseña: mínimo 8 caracteres
   - Vigencia en días: 0 para indefinida
   - Empresa: seleccionar empresa
   - Marcar "Usuario Activo"
4. Hacer clic en Registrar

💡 Nota: Asegúrate de tener permisos de administrador para crear usuarios.

¿Quieres que explique cómo asignar un perfil a este usuario después de crearlo?
```

---

### Plantilla 2: Definición de Concepto

```
[CONCEPTO]
[Concepto] en GEA es [definición breve].

[CONTEXTO]
[Explicación más detallada con contexto]

[RELACIONES]
Se relaciona con:
• [Concepto relacionado 1]
• [Concepto relacionado 2]

[EJEMPLO]
Por ejemplo: [Ejemplo práctico]

[FOLLOW-UP]
¿Te interesa saber más sobre [tema relacionado]?
```

**Ejemplo Real**:
```
Un perfil en GEA es un grupo de usuarios que comparten permisos y características similares.

Los perfiles facilitan la gestión de permisos porque en lugar de asignar permisos individualmente a cada usuario, se asignan al perfil y todos los usuarios con ese perfil heredan los permisos.

Se relaciona con:
• Usuarios (los usuarios tienen perfiles)
• Permisos (los perfiles tienen permisos)
• Módulos (los permisos se asignan por módulo)

Por ejemplo: Si tienes un perfil "Administrador", todos los usuarios con ese perfil tendrán los permisos de administrador para gestionar usuarios, crear procesos, etc.

¿Te interesa saber cómo crear un nuevo perfil o cómo asignar permisos a un perfil?
```

---

### Plantilla 3: Información de Módulo

```
[MÓDULO]
El módulo de [Módulo] en GEA permite [propósito principal].

[FUNCIONALIDADES]
Incluye las siguientes funcionalidades:
• [Funcionalidad 1]: [Descripción]
• [Funcionalidad 2]: [Descripción]
• [Funcionalidad 3]: [Descripción]

[ACCESO]
Para acceder: [Ruta de navegación]

[USO COMÚN]
Se usa comúnmente para: [Casos de uso]

[FOLLOW-UP]
¿Sobre qué aspecto del módulo te gustaría saber más?
```

**Ejemplo Real**:
```
El módulo de Tareas en GEA permite gestionar y controlar tareas relacionadas con diferentes procesos de trabajo.

Incluye las siguientes funcionalidades:
• Tareas Pendientes: Ver tareas asignadas que están pendientes de ejecución
• Tareas Iniciadas: Controlar tareas que has iniciado y no han sido atendidas
• Tareas en Proceso: Visualizar el estado de tareas en las que has intervenido
• Tareas Denegadas: Gestionar tareas que no han sido aprobadas

Para acceder: Menú principal → Tareas

Se usa comúnmente para:
• Ver qué trabajo tienes pendiente
• Seguir el progreso de procesos iniciados
• Gestionar tareas que fueron rechazadas

¿Sobre qué tipo de tareas te gustaría saber más?
```

---

### Plantilla 4: Resolución de Problema

```
[EMPATÍA]
Entiendo que estás teniendo problemas con [problema].

[DIAGNÓSTICO]
Las causas más comunes de este problema son:
1. [Causa 1]
2. [Causa 2]
3. [Causa 3]

[SOLUCIÓN]
Para resolverlo, sigue estos pasos:
1. [Paso de solución 1]
2. [Paso de solución 2]
   ...

[VERIFICACIÓN]
Si después de estos pasos el problema persiste:
• [Alternativa 1]
• [Alternativa 2]
• Contactar al administrador del sistema

[FOLLOW-UP]
¿Pudiste resolver el problema? Si no, ¿qué mensaje de error ves?
```

---

### Plantilla 5: Información No Disponible

```
[RECONOCIMIENTO]
Lo siento, no tengo información específica sobre "[tema]" en mi base de conocimiento actual sobre GEA.

[BÚSQUEDA ALTERNATIVA]
Sin embargo, puedo ayudarte con temas relacionados:
• [Tema relacionado 1]
• [Tema relacionado 2]
• [Tema relacionado 3]

[ALTERNATIVAS]
Otras opciones:
1. Revisar el módulo [Módulo relevante]
2. Consultar el manual técnico de GEA
3. Contactar al soporte técnico de IMPROTECSA

[FOLLOW-UP]
¿Te gustaría que te ayude con alguno de estos temas relacionados?
```

---

## ⚠️ Manejo de Errores y Excepciones

### Error Tipo 1: Información No Encontrada

**Detectado cuando**: No hay resultados relevantes en la base de conocimiento

**Respuesta**:
```
No encontré información específica sobre "[término]" en mi base de conocimiento.

Sin embargo, puedo ayudarte con temas relacionados:
[Lista de temas relacionados]

¿Alguno de estos te sirve, o tienes otra pregunta sobre GEA?
```

---

### Error Tipo 2: Pregunta Ambigua

**Detectado cuando**: La pregunta puede tener múltiples interpretaciones

**Respuesta**:
```
Veo que tu pregunta puede referirse a varias cosas. Para ayudarte mejor, ¿podrías aclarar si te interesa:

1. [Interpretación 1]
2. [Interpretación 2]
3. [Interpretación 3]

O puedes reformular tu pregunta con más detalles.
```

---

### Error Tipo 3: Contexto Perdido

**Detectado cuando**: La pregunta requiere contexto previo que no está claro

**Respuesta**:
```
Para ayudarte mejor, necesito un poco más de contexto.

[Pregunta específica sobre el contexto]

O si prefieres, puedes contarme desde el inicio qué estás intentando hacer.
```

---

### Error Tipo 4: Error Técnico

**Detectado cuando**: Error en el procesamiento

**Respuesta**:
```
Disculpa, hubo un error al procesar tu pregunta. Por favor, intenta de nuevo.

Si el problema persiste, puedes:
• Reformular tu pregunta
• Intentar con una pregunta más específica
• Contactar al soporte técnico

[Log del error para debugging]
```

---

## 🔄 Diagramas de Flujo

### Flujo Principal de Conversación

```
                    INICIO
                      ↓
              [Usuario pregunta]
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
   [Intent claro]           [Intent ambiguo]
        ↓                           ↓
   [Buscar info]            [Pedir aclaración]
        ↓                           ↓
   ┌────┴────┐              [Usuario aclara]
   ↓         ↓                      ↓
[Encontrado] [No encontrado]  [Buscar info]
   ↓              ↓                 ↓
[Responder]  [Ofrecer alternativas] ↓
   ↓              ↓            [Responder]
   ↓              ↓                 ↓
   └──────┬───────┴─────────────────┘
          ↓
   [Ofrecer seguimiento]
          ↓
   [Usuario continúa?]
          ↓
    ┌─────┴─────┐
    ↓           ↓
  [Sí]        [No]
    ↓           ↓
[Continuar] [Finalizar]
```

### Flujo de Procedimiento Paso a Paso

```
[Usuario: "¿Cómo hago X?"]
        ↓
[Identificar procedimiento]
        ↓
[Presentar pasos]
        ↓
[Usuario necesita más info?]
        ↓
┌───────┴───────┐
↓               ↓
[Sí]           [No]
↓               ↓
[Detallar paso] [Siguiente paso?]
↓               ↓
[Continuar] ┌───┴───┐
            ↓       ↓
          [Sí]    [No]
            ↓       ↓
      [Siguiente] [Finalizar]
```

### Flujo de Resolución de Problema

```
[Usuario: "Tengo un problema"]
        ↓
[Identificar problema]
        ↓
[Buscar causas comunes]
        ↓
[Proponer solución]
        ↓
[Usuario: "Funcionó?"]
        ↓
┌───────┴───────┐
↓               ↓
[Sí]           [No]
↓               ↓
[Finalizar]  [Alternativa]
                ↓
        [Otra solución]
                ↓
        [¿Funcionó?]
                ↓
        ┌───────┴───────┐
        ↓               ↓
      [Sí]           [No]
        ↓               ↓
  [Finalizar]   [Contactar soporte]
```

---

## 🎯 Patrones Conversacionales

### Patrón 1: "Progresión Natural"

```
Pregunta general → Detalles específicos → Ejemplo práctico → Aplicación
```

**Ejemplo**:
```
U: "¿Qué son las tareas?"
A: [Definición]
U: "¿Cómo veo mis tareas pendientes?"
A: [Procedimiento]
U: "Dame un ejemplo"
A: [Ejemplo]
U: "Perfecto, voy a probarlo"
A: [Confirmación + seguimiento]
```

---

### Patrón 2: "Exploración Guiada"

```
Concepto principal → Subtemas → Profundización → Aplicación práctica
```

**Ejemplo**:
```
U: "Háblame del módulo de Seguridad"
A: [Descripción general + subtemas]
U: "¿Qué es un perfil?"
A: [Definición]
U: "¿Cómo creo uno?"
A: [Procedimiento]
```

---

### Patrón 3: "Solución de Problema"

```
Problema → Diagnóstico → Solución → Verificación → Alternativas
```

---

## 📊 Métricas de Calidad de Flujo

### Indicadores

1. **Tasa de Completitud**: % de conversaciones que alcanzan su objetivo
2. **Tiempo Promedio**: Tiempo desde pregunta hasta solución
3. **Claridad**: Número de aclaraciones necesarias
4. **Satisfacción**: Feedback del usuario sobre la utilidad
5. **Navegación**: Facilidad para cambiar de tema

### Objetivos

- Tasa de completitud: > 85%
- Tiempo promedio: < 3 minutos por caso
- Claridad: < 2 aclaraciones por conversación
- Satisfacción: > 4.5/5
- Navegación: 100% de conversaciones permiten cambio de tema

---

**Última actualización**: Enero 2025


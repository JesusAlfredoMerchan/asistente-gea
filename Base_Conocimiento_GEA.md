# Base de Conocimiento - Plataforma GEA

## 📋 Información General

### ¿Qué es GEA?
GEA es un sistema de información de gestión basado en flujos de trabajo desarrollado por IMPROTECSA S.A.S. Es una herramienta que permite diseñar, parametrizar y supervisar procesos de trabajo de manera eficiente.

### Características Principales
- **Plataforma 100% WEB**: Acceso desde cualquier navegador
- **Aplicaciones móviles**: Disponible para iOS y Android
- **Integración**: Compatible con sistemas ERP, SCADA, CRM y otras plataformas
- **Personalizable**: Parametrización a medida según necesidades específicas
- **Tiempo real**: Informes y datos en tiempo real

### Objetivo del Sistema
Implementar una herramienta de gestión de procesos que se adhiera a estándares de clase mundial, proporcionando una solución integral para la optimización y mejora continua de las operaciones.

---

## 🎯 Beneficios de la Solución

1. **Mejora la eficiencia operativa**: Permite el diseño y parametrización personalizada de procesos
2. **Facilita la toma de decisiones**: Proporciona informes en tiempo real y datos precisos
3. **Mejora la colaboración**: Permite asignación y seguimiento de tareas entre equipos
4. **Mejora la seguridad**: Configuración personalizada de permisos de acceso

---

## 🚀 Inicio del Sistema

Al ingresar al sistema GEA, encontrarás los siguientes apartados en el lado derecho de la pantalla:

### Apartados Principales

#### 1. **Tareas**
- Ver, asignar y gestionar tareas relacionadas con diferentes procesos de trabajo
- Control de tareas pendientes, iniciadas, en proceso y denegadas

#### 2. **Procesos**
- Diseñar y supervisar flujos de trabajo
- Desglosar actividades, definir actores y establecer puntos de control
- Parametrizar el mapa de procesos
- Iniciar nuevos flujos de trabajo

#### 3. **Informes**
- Generar y consultar informes basados en datos recopilados
- Crear informes personalizados mediante combinación de diferentes fuentes de datos
- Exportación y envío automático
- Visualización desde dispositivos móviles multiplataforma

#### 4. **Mapas**
- Visualización geográfica de datos o procesos

#### 5. **Parámetros**
- Personalizar elementos de recolección de datos
- Configurar consulta de información y validación
- Acceso a todos los módulos del sistema

#### 6. **Tableros**
- Seguimiento visual de indicadores clave de rendimiento (KPIs)
- Otras métricas importantes

---

## 📊 Módulo de Tareas

### Control de Tareas

#### Tareas Pendientes
- Tareas asignadas a un usuario o perfil que se encuentran pendientes de ejecución
- Cada usuario tiene su panel de control de tareas asignadas según la parametrización de procesos

#### Tareas Iniciadas
- Control sobre tareas iniciadas por un usuario o perfil que no han sido atendidas por el siguiente actor
- Permite validar que las tareas han sido atendidas
- Permite modificar datos sobre tareas no ejecutadas

#### Tareas en Proceso
- Visualización del estado del proceso de las tareas en las que ha intervenido el usuario
- Seguimiento hasta que el proceso haya terminado

#### Tareas Denegadas
- Panel de control para tareas lanzadas por un usuario o perfil que no han sido aprobadas
- Permite gestión sobre la tarea denegada (modificar, anular)

---

## ⚙️ Módulo de Procesos

### Funcionalidades
- Parametrización del mapa de procesos
- Asignación de módulos y procesos a cada macro proceso
- Inicio de nuevos flujos de trabajo
- Personalización según necesidades específicas de usuario o perfil
- Herramientas de seguimiento y supervisión

---

## 📈 Módulo de Informes

### Características
- Creación de cualquier tipo de informe según requerimientos
- Elaboración mediante combinación de diferentes fuentes de datos
- Consulta, exportación o envío automático
- Visualización desde dispositivos móviles multiplataforma mediante APPs de consulta

---

## 🔐 Módulo de Seguridad

### Estructura del Módulo

#### ADMINISTRACIÓN

##### Estados
- Gestión de diferentes estados que pueden tener los elementos dentro del sistema

##### Operaciones
- Definición y gestión de operaciones que se pueden realizar en el sistema

##### Perfiles
- Creación y gestión de perfiles de usuario
- Determinación de permisos de cada usuario

##### Módulos
- Gestión de diferentes módulos del sistema

##### Usuarios
- Gestión de cuentas de usuario
- Creación de nuevas cuentas

#### PARAMETRIZACIÓN

##### Entidad Parámetros
- Definición de parámetros que se utilizarán en el sistema

##### Permisos Actividades - Usuario
- Gestión de actividades de cada proceso dependiendo del módulo

##### Seguridad
- **Consultar Log**: Visualización en forma de historial de todas las operaciones ejecutadas
- **Administrar Menú**: Visualización y administración de distintos menús de cada módulo
- **Permisos Perfil**: Asignación de permisos de perfiles para controlar operaciones en menús
- **Usuario Perfil**: Gestión y asignación de perfil específico a cada usuario

---

## 📝 Procedimientos del Módulo de Seguridad

### TAREA 1: Crear un Nuevo Usuario

**Pasos:**
1. Ingresar en el módulo **Seguridad** → Menú **Administración** → **Usuarios**
2. Hacer clic en **Nuevo Registro**
3. Completar los campos solicitados:
   - **Usuario**: nombre.apellido
   - **Descripción**: Nombre Apellido
   - **Contraseña**: (mínimo 8 caracteres)
   - **Vigencia en días**: Días que el usuario estará activo (0 para vigencia indefinida)
   - **Empresa**: Seleccionar la empresa donde se encuentra el usuario
   - **Usuario Activo**: Marcar la casilla ☑
4. Hacer clic en el botón **Registrar**

**Resultado**: El usuario quedará registrado en la lista de usuarios del sistema.

---

### TAREA 2: Crear un Nuevo Perfil

**Pasos:**
1. Ingresar en el módulo **Seguridad** → Menú **Administración** → **Perfiles**
2. Hacer clic en el botón **Nuevo Registro**
3. Ingresar los campos requeridos
4. Marcar la casilla **Activo**
5. Hacer clic en el botón **Guardar**

**Resultado**: El nuevo perfil será creado y visible en la lista de perfiles.

---

### TAREA 3: Asignar Permisos a un Perfil

**Pasos:**
1. Ingresar en el módulo **Seguridad** → **Parametrización** → **Seguridad**
2. En **Administración de Seguridad** seleccionar **Permisos Perfil**
3. Seleccionar el perfil al que se desea asignar permisos
4. Seleccionar un módulo específico
5. Observar el contenido de los menús del módulo
6. Hacer clic en el botón para asignar permisos a cada opción de los menús
7. Hacer clic en **Registrar** para guardar los cambios

**Nota**: Los permisos pueden ser granulares, permitiendo por ejemplo solo visualizar usuarios sin poder crear nuevos.

---

### TAREA 4: Asignar un Perfil a un Usuario

**Pasos:**
1. Ingresar en el módulo **Seguridad** → **Parametrización** → **Seguridad**
2. En **Administración de Seguridad** seleccionar **Usuario Perfil**
3. Hacer clic en **Nuevo Registro**
4. Elegir el usuario al que se desea asignar un perfil
5. Hacer clic en **Registrar**

**Resultado**: El usuario quedará asociado con el perfil seleccionado.

---

### TAREA 5: Asignar Procesos a un Usuario

**Pasos:**
1. Ingresar en el módulo **Seguridad** → **Parametrización** → **Permisos Actividades - Usuario**
2. Seleccionar el módulo donde se asignará el proceso
3. Se mostrarán todas las actividades relacionadas con el proceso seleccionado
4. Hacer clic en el ícono para asignar un usuario a dicha actividad
5. Si se asigna el mismo usuario en **Usuario Sig. Actividad**, ese usuario realizará la siguiente actividad
6. Hacer clic en el ícono para **Asignar actividades**

**Resultado**: 
- El usuario podrá ver el proceso asignado en el apartado **Procesos**
- Al seleccionar el proceso, aparecerá la actividad asignada
- Al completar el formulario y guardar, la tarea aparecerá en el apartado **Tareas**

---

### TAREA 6: Gestionar el Contenido de los Menús

**Pasos:**
1. Ingresar en el módulo **Seguridad** → **Parametrización** → **Seguridad**
2. En **Administración de Seguridad** seleccionar **Administrar Menú**
3. Seleccionar un módulo para visualizar sus menús
4. Dependiendo de los permisos, se puede:
   - Eliminar menús
   - Modificar menús
   - Crear nuevos menús

**Para crear un nuevo menú:**
- Hacer clic en **Nuevo Registro**
- Completar los campos desplegados
- Guardar

---

## 🔧 Módulo de Parámetros

### Estructura del Módulo

#### ADMINISTRACIÓN

##### Ent. Auxiliares
- Módulos o funciones que ayudan a administrar, recolectar, recuperar, procesar, almacenar y distribuir información
- Permite crear nuevas entidades auxiliares
- Opción de clasificación para relacionar entidades entre sí

##### Características
- Definición y gestión de propiedades específicas de elementos dentro del sistema
- Ejemplo: nombre, precio, proveedor (en caso de productos)

##### Catálogo de Informes
- Selección y generación de informes basados en datos recopilados
- Creación de registros con código, descripción y módulo al que pertenece

##### Parámetros
- Configuración de aspectos del sistema según necesidades de la empresa
- Variables que afectan cómo el sistema recopila, procesa y presenta datos

##### Periodos
- Definición y gestión de diferentes períodos de tiempo para seguimiento y evaluación

##### Parámetros de Procedimientos
- Definición y gestión de parámetros que controlan la ejecución de procedimientos

##### Configuración Romana
- Configuración de la forma en que el sistema interactúa con básculas o balanzas

##### Tipos de Transacción
- Definición y gestión de diferentes tipos de transacciones

##### Variables
- Definición y gestión de variables que afectan operaciones y procesos

##### Variables Conexión ERP
- Configuración de variables para conexión con sistemas ERP

#### PARAMETRIZACIÓN

##### Monitor
- Monitoreo del estado y rendimiento del sistema en tiempo real

##### Entidad Parámetros
- Definición y gestión de diferentes entidades o componentes dentro del sistema

##### Entidad Detalle Parámetros
- Visualización y gestión de detalles adicionales sobre entidades definidas

##### Procesos
- Definición, gestión y supervisión de diferentes procesos de trabajo

##### Sitio Tipo Transacción
- Definición y gestión de tipos de transacciones en sitios específicos

##### Tipo Transacción Formato
- Definición y gestión de formatos para cada tipo de transacción

##### Tipo Transacción Resultado
- Definición y gestión de resultados posibles para cada tipo de transacción

##### Tipo Transacción Variable
- Definición y gestión de variables que afectan cada tipo de transacción

---

## 🚛 Módulo de Romana

### Estructura
Solo cuenta con el menú **Administración**:
- **Conductores**: Gestión de conductores
- **Vehículos**: Gestión de vehículos

---

## 🏢 Módulo de Proveedores

### Estructura
Solo cuenta con el menú **Administración**:
- **Proveedores Bienes y Servicios**: Gestión de proveedores

---

## 🏭 Módulo de Producción

### Estructura

#### ADMINISTRACIÓN
- **Bodegas**: Gestión de bodegas
- **Jerarquía (ubicaciones)**: Gestión de jerarquías de ubicaciones
- **Niveles**: Gestión de niveles
- **Productos**: Gestión de productos
- **Variables**: Gestión de variables

---

## 🔧 Módulo de Mantenimiento

### Estructura
Solo cuenta con el menú **Administración**:
- **Equipos**: Gestión de equipos
- **Jerarquía (Componentes)**: Gestión de jerarquías de componentes

---

## 📦 Módulo de Logística

### Estructura
Solo cuenta con el menú **Administración**:
- **Certificados de Calidad**: Gestión de certificados
- **Clientes**: Gestión de clientes
- **Mercados**: Gestión de mercados

---

## 🧪 Módulo de Laboratorio

### Estructura

#### ADMINISTRACIÓN
- **Análisis**: Gestión de análisis
- **Jerarquías**: Gestión de jerarquías

#### PARAMETRIZACIÓN
- **Relación Jerarquía**: Configuración de relaciones entre jerarquías

---

## 📊 Módulo de Informes

### Estructura
Solo cuenta con el menú **Informes y consultas**:
- **Generar**: Visualización de informes disponibles en cada módulo del sistema

---

## 💰 Módulo de Contable

### Estructura
Solo cuenta con el menú **Administración**:
- **Beneficiarios**: Gestión de beneficiarios
- **Centro de Costo**: Gestión de centros de costo

---

## 💻 Requerimientos de Hardware

### Servidor
- **Procesador**: 2,4 GHz Pentium IV equivalente o superior
- **Memoria RAM**: 4 GB o superior
- **Espacio en disco**: 20 GB de espacio disponible
- **Sistema Operativo**: Microsoft Windows® 2008 Server Service Pack 2 o superior

### Estaciones de Trabajo
- **Procesador**: 600 MHz Pentium III equivalente o superior
- **Memoria RAM**: 512 MB o superior
- **Espacio en disco**: 5 GB de espacio disponible
- **Sistema Operativo**: 
  - Microsoft Windows Vista™
  - Microsoft Windows® XP con Service Pack 2 o superior
  - Microsoft Windows 2000 con Service Pack 4 o superior

---

## 📚 Glosario de Términos

### Actividad
Tarea específica dentro de un proceso que debe ser ejecutada por un usuario o perfil.

### Actor
Usuario o perfil responsable de ejecutar una actividad dentro de un proceso.

### Entidad Auxiliar
Módulo o función que ayuda a administrar, recolectar, recuperar, procesar, almacenar y distribuir información relevante para los procesos.

### Flujo de Trabajo
Secuencia de actividades que deben ejecutarse para completar un proceso.

### Macro Proceso
Conjunto de procesos relacionados que se agrupan para facilitar su gestión.

### Módulo
Conjunto de funcionalidades específicas dentro del sistema GEA.

### Parámetro
Configuración que afecta cómo el sistema recopila, procesa y presenta datos.

### Perfil
Grupo de usuarios con permisos y características similares.

### Punto de Control
Momento en un proceso donde se valida o verifica información antes de continuar.

### Proceso
Secuencia estructurada de actividades que transforma insumos en productos o servicios.

### Tarea
Actividad específica asignada a un usuario o perfil dentro de un proceso.

### Usuario
Persona con acceso al sistema GEA mediante credenciales de usuario y contraseña.

---

## 🔍 Preguntas Frecuentes

### ¿Cómo inicio sesión en GEA?
Al ingresar al sistema, encontrarás los apartados principales en el lado derecho de la pantalla: Tareas, Procesos, Informes, Mapas, Parámetros y Tableros.

### ¿Qué hago si no tengo permisos para realizar una acción?
El sistema mostrará un mensaje indicando que no tienes los permisos necesarios. Debes contactar al administrador del sistema para que asigne los permisos adecuados a tu perfil.

### ¿Cómo veo mis tareas pendientes?
Dirígete al apartado **Tareas** en el menú principal. Allí encontrarás el panel de control de tareas pendientes asignadas a tu usuario o perfil.

### ¿Cómo inicio un nuevo proceso?
Dirígete al apartado **Procesos**, selecciona el proceso que deseas iniciar y completa el formulario correspondiente.

### ¿Puedo usar GEA desde mi móvil?
Sí, GEA cuenta con aplicaciones móviles para iOS y Android que permiten acceder a las funcionalidades principales del sistema.

### ¿Cómo creo un informe personalizado?
Dirígete al apartado **Informes** y utiliza las herramientas disponibles para combinar diferentes fuentes de datos según tus requerimientos.

---

## 📞 Información de Contacto

**Empresa**: IMPROTECSA S.A.S.  
**Sitio Web**: WWW.IMPROTECSA.COM  
**Año**: © 2023

---

## 📝 Notas Importantes

- Todos los procedimientos descritos requieren los permisos adecuados según el perfil del usuario
- Los formularios pueden variar según las actividades asignadas a cada proceso
- La vigencia de un usuario puede ser indefinida escribiendo 0 en el campo "Vigencia en días"
- Los permisos se asignan a nivel de perfil, y los perfiles se asignan a usuarios
- Los procesos deben ser asignados a usuarios específicos para que aparezcan en sus paneles de tareas

---

*Última actualización: Basado en Manual GEA 2023*


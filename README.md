# lab1.

JOSHUA DANIEL REYES TELLEZ SMSS165323
BERTA ELIZABETH MEJICANOS RIVAS SMSS047723


1. Descripción del Problema
Identificación del problema:
Muchas personas que realizan actividad física a diario tienen dificultades para hacer un seguimiento adecuado de su progreso, especialmente en aspectos como el tiempo invertido, el tipo de ejercicio realizado y su intensidad. Esta falta de registro puede resultar en una disminución de la motivación o en la imposibilidad de observar avances a lo largo del tiempo. Además, no todas las aplicaciones actuales permiten registrar y visualizar estos datos de forma sencilla y accesible.
Solución propuesta:
La solución consiste en una aplicación de escritorio, desarrollada en Python, que permite a los usuarios registrar sus actividades físicas diarias, incluyendo detalles como el tipo de actividad, la duración en minutos y la intensidad del ejercicio. Además, ofrece una herramienta de visualización gráfica para monitorear el progreso. Esto permite a los usuarios observar de manera clara y práctica su constancia y avance en sus rutinas de ejercicio.

2. Funcionalidad Principal
Funcionalidad básica implementada:
La funcionalidad principal de la aplicación es el registro y visualización de actividades físicas. Los usuarios pueden ingresar información sobre el tipo de actividad, el tiempo dedicado (en minutos) y la intensidad (baja, media o alta), que se almacenan en una base de datos SQLite. Posteriormente, pueden visualizar un gráfico que muestra la duración total de ejercicio por día, lo que facilita el seguimiento de su progreso.
Funcionalidad ejecutable:
La aplicación es completamente funcional en su aspecto básico. Al abrirla, el usuario puede registrar actividades y guardarlas en la base de datos. Además, tiene la opción de generar un gráfico que muestra el tiempo dedicado a la actividad física, permitiendo visualizar el progreso.

3. Avances del Proyecto
Estado actual del proyecto y logros alcanzados:
Configuración de la base de datos SQLite: Se ha creado y configurado una base de datos actividad_fisica.db, que incluye una tabla para almacenar los registros de actividad física.
Función de registro de actividades: El usuario puede registrar el tipo de actividad, la duración y la intensidad. La fecha se añade automáticamente y se almacena junto a los otros datos en la base de datos.
Visualización del progreso: Se ha desarrollado una función que permite visualizar un gráfico con la duración total de ejercicio por día. Esta gráfica se genera con Matplotlib y facilita el análisis del progreso.
     Interfaz gráfica básica: Se creó una interfaz gráfica usando Tkinter que facilita            al usuario la entrada de datos y la visualización del progreso.

3. Avances del Proyecto
Estado actual del proyecto y logros alcanzados:
Configuración de la base de datos SQLite: Se ha creado y configurado una base de datos actividad_fisica.db, que incluye una tabla para almacenar los registros de actividad física.
Función de registro de actividades: El usuario puede registrar el tipo de actividad, la duración y la intensidad. La fecha se añade automáticamente y se almacena junto a los otros datos en la base de datos.
Visualización del progreso: Se ha desarrollado una función que permite visualizar un gráfico con la duración total de ejercicio por día. Esta gráfica se genera con Matplotlib y facilita el análisis del progreso.
Interfaz gráfica básica: Se creó una interfaz gráfica usando Tkinter que facilita al usuario la entrada de datos y la visualización del progreso.

4. Objetivos Pendientes y Plan de Desarrollo
Funcionalidades y elementos pendientes:
Mejorar la interfaz gráfica:
Descripción: Hacer la interfaz más intuitiva y visualmente agradable. Incluir opciones de selección para la intensidad y un menú que permita visualizar registros anteriores.
Plan de implementación: Se seguirá utilizando Tkinter para mejorar la usabilidad de la interfaz, añadiendo menús desplegables y cuadros de selección.

Plan de desarrollo:
Se dará prioridad a la mejora de la interfaz gráfica y a la creación de gráficos adicionales, seguidos por la edición, eliminación y exportación de registros. Para estas mejoras se emplearán principalmente tkinker para la interfaz, matplotlib para los gráficos y QLite junto a pandas para la gestión de datos.










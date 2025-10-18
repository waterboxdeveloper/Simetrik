# 2. Contexto

En Simetrik, el equipo de Product Delivery es responsable de gestionar todo el ciclo de incorporación de nuevas funcionalidades, desde su desarrollo hasta su lanzamiento y comunicación a los usuarios.

Este proceso combina tareas manuales y semi-automatizadas, y requiere una coordinación constante entre diferentes equipos y herramientas para garantizar lanzamientos oportunos, claros y correctamente documentados.

## Pasos clave del proceso

### 1. Documentación y seguimiento (Release Tracker en Notion)

Simetrik utiliza un documento colaborativo en Notion, llamado **Release Tracker**, para centralizar la información de cada nueva funcionalidad o mejora del producto.

Cada registro contiene información clave: el nombre de la funcionalidad, el proyecto asociado, su estado de desarrollo y despliegue, los responsables (Delivery Managers, Product Owners o equipos de diseño), y un enlace al documento técnico Definition of Done (DoD), disponible para exportar en formato PDF.

El Release Tracker permite monitorear el avance de cada funcionalidad desde su desarrollo hasta su lanzamiento.

Cuando una funcionalidad alcanza el estado **Regression**, significa que ya superó las pruebas de calidad (QA) y está lista para el lanzamiento.

En ese momento, el estado se actualiza dentro del tracker y el sistema envía notificaciones automáticas a los equipos involucrados, indicando las acciones que deben ejecutar en la fase previa al despliegue.

Entre estas acciones se incluye la preparación de materiales educativos y comunicacionales, lo que asegura una coordinación fluida entre los equipos de Desarrollo, QA, Educación y Comunicación.

### 2. Creación del contenido educativo

Cuando el estado de una funcionalidad cambia a **Regression**, el equipo de Educación recibe una notificación automática que le indica que debe descargar el documento técnico PDF (Definition of Done) correspondiente.

A partir de este archivo, el equipo extrae la información técnica necesaria y genera un borrador de contenido educativo utilizando herramientas de inteligencia artificial como **Notebook LM** y **Gemini**, que analizan el texto técnico y lo adaptan al tono y estilo de comunicación de Simetrik.

Posteriormente, el contenido se revisa y valida manualmente junto con los equipos técnicos, se traduce y finalmente se publica en **Zendesk**, la plataforma de soporte utilizada por clientes y usuarios internos.

### 3. Comunicación de lanzamiento

En paralelo, el equipo de Comunicación prepara los anuncios de lanzamiento (notas internas y newsletters para usuarios finales).

Con apoyo de **Gemini**, se generan y traducen versiones claras y consistentes de los mensajes, asegurando que todos los equipos y usuarios estén informados antes y durante el lanzamiento de la nueva funcionalidad.

## Herramientas utilizadas en el proceso

### Notion
Plataforma colaborativa en la nube para crear y gestionar documentos y bases de datos.
En este proceso, se utiliza para mantener el Release Tracker, un documento vivo donde se registra y actualiza toda la información esencial de nuevas funcionalidades, accesible para todos los miembros del equipo y con colaboración en tiempo real.

### Notebook LM
Herramienta especializada en procesar documentos técnicos complejos.
Permite extraer y organizar información relevante a partir del PDF Definition of Done, facilitando la generación del borrador inicial de la documentación educativa.

### Gemini
Modelo avanzado de lenguaje natural que ayuda a generar, refinar y adaptar contenido escrito automáticamente.
Convierte el borrador generado en una versión clara, coherente y alineada al estilo corporativo de Simetrik, además de apoyar en la traducción y preparación del contenido para su publicación.

### Zendesk
Plataforma de atención y soporte al usuario donde se publica y gestiona toda la documentación educativa generada, disponible para usuarios en varios idiomas.

## Desafío para la prueba

A pesar de los avances en automatización, el proceso aún implica numerosos pasos manuales para mover información entre herramientas, crear contenido y coordinar equipos.

Tu desafío es diseñar una solución que explore cómo automatizar y conectar algunas de estas etapas para reducir la intervención manual y mejorar la eficiencia del equipo.

El enfoque, la claridad en tu planteamiento y la documentación de tus decisiones serán tan importantes como la implementación técnica.


# Prueba Técnica Simetrik

## Página 1
Prueba Técnica - Prompt Engineer
1. Instrucciones Generales
Duración estimada: 7 horas de trabajo efectivo
Modalidad: Trabajo asincrónico
Ventana disponible: 20 horas en horario laboral (8:00 AM – 6:00 PM)
Nota: Aunque dispones de una ventana total de 20 horas, la prueba está diseñada para completarse en
aproximadamente 7 horas de trabajo efectivo. Organiza tu tiempo para avanzar de forma equilibrada en
cada parte del ejercicio.
Objetivo:
Evaluar tus habilidades técnicas en programación, integración de APIs, automatización de flujos de
trabajo y diseño de soluciones simples y bien documentadas.
La prueba está inspirada en situaciones reales del rol de Prompt Engineer Junior en Simetrik, donde se
espera que combines pensamiento lógico, creatividad y uso estratégico de herramientas de inteligencia
artificial.
Recomendaciones:
● Organiza tu tiempo para poder avanzar en todos los bloques y entregar un trabajo equilibrado.
● Lee cuidadosamente cada sección y utiliza los ejemplos base y plantillas proporcionadas para
facilitar el desarrollo.
● La calidad, claridad y orden del código y documentación son tan importantes como la
funcionalidad.
Recuerda:
● No buscamos perfección, sino entender tu proceso de pensamiento.
● Puedes usar herramientas de IA como apoyo (Cursor, Claude, ChatGPT, etc.), siempre que su
uso sea consciente y complementario.
● Documentar tus decisiones técnicas es más valioso que entregar código perfecto.
● Si algo no está claro, pregunta.
Soporte:
Si tienes alguna duda o inconveniente, contacta a Laura Basto vía correo electrónico:
laura.basto@simetrik.com. Ella gestionará que recibas una respuesta oportuna y detallada para ayudarte
a continuar con la prueba.

---

## Página 2
2. Contexto
En Simetrik, el equipo de Product Delivery es responsable de gestionar todo el ciclo de incorporación de
nuevas funcionalidades, desde su desarrollo hasta su lanzamiento y comunicación a los usuarios.
Este proceso combina tareas manuales y semi-automatizadas, y requiere una coordinación constante
entre diferentes equipos y herramientas para garantizar lanzamientos oportunos, claros y correctamente
documentados.
Pasos clave del proceso
1. Documentación y seguimiento (Release Tracker en Notion)
Simetrik utiliza un documento colaborativo en Notion, llamado Release Tracker, para centralizar la
información de cada nueva funcionalidad o mejora del producto.
Cada registro contiene información clave: el nombre de la funcionalidad, el proyecto asociado, su estado
de desarrollo y despliegue, los responsables (Delivery Managers, Product Owners o equipos de diseño),
y un enlace al documento técnico Definition of Done (DoD), disponible para exportar en formato PDF.
El Release Tracker permite monitorear el avance de cada funcionalidad desde su desarrollo hasta su
lanzamiento.
Cuando una funcionalidad alcanza el estado Regression, significa que ya superó las pruebas de calidad
(QA) y está lista para el lanzamiento.
En ese momento, el estado se actualiza dentro del tracker y el sistema envía notificaciones automáticas
a los equipos involucrados, indicando las acciones que deben ejecutar en la fase previa al despliegue.
Entre estas acciones se incluye la preparación de materiales educativos y comunicacionales, lo que
asegura una coordinación fluida entre los equipos de Desarrollo, QA, Educación y Comunicación.
2. Creación del contenido educativo
Cuando el estado de una funcionalidad cambia a Regression, el equipo de Educación recibe una
notificación automática que le indica que debe descargar el documento técnico PDF (Definition of Done)
correspondiente.
A partir de este archivo, el equipo extrae la información técnica necesaria y genera un borrador de
contenido educativo utilizando herramientas de inteligencia artificial como Notebook LM y Gemini, que
analizan el texto técnico y lo adaptan al tono y estilo de comunicación de Simetrik.
Posteriormente, el contenido se revisa y valida manualmente junto con los equipos técnicos, se traduce y
finalmente se publica en Zendesk, la plataforma de soporte utilizada por clientes y usuarios internos.
3. Comunicación de lanzamiento
En paralelo, el equipo de Comunicación prepara los anuncios de lanzamiento (notas internas y
newsletters para usuarios finales).
Con apoyo de Gemini, se generan y traducen versiones claras y consistentes de los mensajes,
asegurando que todos los equipos y usuarios estén informados antes y durante el lanzamiento de la
nueva funcionalidad.

---

## Página 3
Herramientas utilizadas en el proceso
● Notion
Plataforma colaborativa en la nube para crear y gestionar documentos y bases de datos.
En este proceso, se utiliza para mantener el Release Tracker, un documento vivo donde se
registra y actualiza toda la información esencial de nuevas funcionalidades, accesible para todos
los miembros del equipo y con colaboración en tiempo real.
● Notebook LM
Herramienta especializada en procesar documentos técnicos complejos.
Permite extraer y organizar información relevante a partir del PDF Definition of Done,
facilitando la generación del borrador inicial de la documentación educativa.
● Gemini
Modelo avanzado de lenguaje natural que ayuda a generar, refinar y adaptar contenido escrito
automáticamente.
Convierte el borrador generado en una versión clara, coherente y alineada al estilo corporativo
de Simetrik, además de apoyar en la traducción y preparación del contenido para su publicación.
● Zendesk
Plataforma de atención y soporte al usuario donde se publica y gestiona toda la documentación
educativa generada, disponible para usuarios en varios idiomas.
Desafío para la prueba
A pesar de los avances en automatización, el proceso aún implica numerosos pasos manuales para
mover información entre herramientas, crear contenido y coordinar equipos.
Tu desafío es diseñar una solución que explore cómo automatizar y conectar algunas de estas etapas
para reducir la intervención manual y mejorar la eficiencia del equipo.
El enfoque, la claridad en tu planteamiento y la documentación de tus decisiones serán tan importantes
como la implementación técnica.

---

## Página 4
3. Estructura de la Prueba Técnica
La prueba está dividida en 3 secciones que evalúan las competencias clave del rol:
● Parte 1. Automatización con Python, APIs e integración con IA (60%)
Se evalúa la capacidad para programar soluciones prácticas que integren APIs,
procesen datos, y ejecuten automatizaciones complejas incluyendo integración con
agentes de IA como Gemini.
● Parte 2. Diseño y Automatización de Flujos (30%)
Se mide la habilidad para conceptualizar, diseñar y construir flujos de automatización
utilizando herramientas low-code/no-code (como n8n) para orquestar procesos y
gestionar comunicaciones multicanal.
● Resolución de Problemas y Documentación (10%)
Se evalúa la capacidad para analizar problemas, identificar soluciones y documentar
clara y profesionalmente el trabajo realizado.
4. Documentos Disponibles en Notion
Para el desarrollo de esta prueba tendrás acceso directo a los siguientes documentos,
organizados en el espacio compartido de Notion:
https://www.notion.so/Prueba-t-cnica-28c98e9d3db980caa58ffa53ae0cbee4?source=copy_link
Parte 1:
● Release Tracker – Prueba técnica
● Data normalization in union sources – Prueba Técnica
● Definition of Done – E137 – Data Normalization in Unions
● One Pager Guide
Parte 2:
● ES_-_Conciliaciones_Avanzadas.pdf
● Matriz de traducciones

---

## Página 5
Parte 1. Automatización con Python e
Integración con Gemini (60 %)
Duración estimada: 4.5 horas
Objetivo General
Diseñar e implementar un flujo automatizado end-to-end que conecte Notion (como sistema de
gestión de lanzamientos) con Gemini API (como modelo de lenguaje generativo), con el fin de
crear documentación educativa automáticamente a partir del documento técnico Definition of
Done (DoD) de una funcionalidad lista para despliegue.
El sistema debe ser capaz de detectar un cambio de estado en el documento Release Tracker
en Notion, extraer y procesar la información técnica, generar un One Pager educativo con ayuda
de inteligencia artificial y actualizar los registros correspondientes dentro del mismo entorno de
Notion.
Nota:
No se evaluará la calidad ni la estructura del documento final, sino la implementación
técnica completa del flujo automatizado desde el disparador inicial hasta la actualización
final en Notion.
Flujo a Automatizar
1. Monitoreo y Detección Automática
● El flujo debe monitorear el documento colaborativo Release Tracker – Prueba Técnica,
disponible en el espacio de Notion compartido.
● Cuando el campo “Deployment Status” de la funcionalidad
E137 – Data Normalization in Union Sources cambia a “Regression”, el sistema debe
activar automáticamente el proceso completo.
● La detección puede implementarse mediante polling periódico (cada 5 minutos) o con
un webhook de Notion, si el candidato lo prefiere.

---

## Página 6
2. Extracción del Documento Técnico
● Usando la Notion API, el sistema debe leer el enlace ubicado en el campo “Link
Definition” del registro de la funcionalidad.
● Este enlace corresponde al documento Definition of Done – E137, disponible para extraer
en formato PDF dentro del mismo espacio de Notion.
● El flujo debe descargar el archivo o acceder a su contenido, extraer el texto y
estructurarlo para su posterior procesamiento con Gemini.
● Se sugiere el uso de librerías como PyPDF2, pdfplumber o pdfminer.six.
3. Procesamiento con Gemini API
● El texto del Definition of Done debe procesarse con la API de Gemini (modelo
gemini-pro), utilizando la plantilla corporativa One Pager Guide como referencia
estructural.
● El sistema debe construir un prompt que instruya claramente al modelo para:
○ Seguir exactamente la estructura del One Pager Guide.
○ Transformar el contenido técnico en un lenguaje claro, orientado a usuarios
finales.
○ Generar las 8 secciones corporativas obligatorias:
1. Tipo de comunicación
2. Nombre de la funcionalidad
3. Público objetivo
4. Beneficio principal
5. En qué consiste
6. Características clave
7. Cómo se usa / dónde se encuentra
8. Cierre motivacional
○ Mantener un tono profesional, cercano y alineado con el estilo Simetrik.
4. Generación del PDF
● El texto devuelto por Gemini debe convertirse en un PDF estructurado y legible, con
jerarquía visual (títulos, secciones, listas).
● Se pueden usar librerías como reportlab, fpdf, weasyprint, entre otras.

---

## Página 7
● El documento debe guardarse localmente en una carpeta /output/ con nombre
descriptivo:
E137_OnePager.pdf.
5. Actualización en Notion
● Una vez generado el PDF, el sistema debe:
○ Actualizar automáticamente el registro correspondiente en el Release Tracker –
Prueba Técnica, agregando el enlace o archivo PDF del One Pager.
○ Actualizar el documento Data Normalization in Union Sources (también en
Notion), adjuntando el PDF para revisión del equipo de Educación.
Consideraciones Adicionales
● El flujo debe incluir logs detallados con timestamps para cada etapa crítica.
● Debe implementarse manejo de errores con reintentos automáticos ante fallos de
conexión o parsing (hasta 2 intentos).
● Cada función debe contener docstrings descriptivos y nombres consistentes (e.g.,
dod_text, onepager_content, pdf_output).
● La autenticación con Notion y Gemini debe manejarse desde config.yaml o variables de
entorno.
● Se valorará la modularidad, claridad y legibilidad del código.

---

## Página 8
Criterios de Evaluación – Parte 1 (60%)
Componente Peso Criterios Específicos
Funcionalidad del flujo 25% - Detección automática del cambio de estado
a “Regression”
- Extracción correcta del DoD
- Generación exitosa del One Pager y PDF
- Actualización completa en Notion
Integración con Gemini 20% - Configuración correcta de API
API - Prompt claro y efectivo
- Respuesta estructurada
- Incorporación completa de las 8 secciones
requeridas
Calidad técnica del 15% - Estructura modular
código - Manejo de errores y reintentos
- Logs detallados
- Configuración externalizada y tests básicos
Resultado Esperado
Un sistema autónomo que:
1. Detecte automáticamente el cambio a “Regression” de la funcionalidad E137 – Data
Normalization in Union Sources en el Release Tracker de Notion.
2. Procese el documento Definition of Done – E137.
3. Genere, con ayuda de Gemini, un One Pager educativo completo y estructurado.
4. Lo exporte en PDF.
5. Y lo vuelva a cargar automáticamente en Notion para revisión y difusión interna.

---

## Página 9
Parte 2. Automatización de Flujos en n8n y
Gemini API (30%)
Duración estimada: 2.5 horas
Objetivo: Evaluar la capacidad para diseñar y documentar un flujo automatizado end-to-end en
n8n, integrando Gemini API para traducción multilingüe, aplicación de una matriz terminológica
y envío automatizado de correos personalizados.
Objetivo General
Diseñar e implementar un flujo completo en n8n que procese un documento educativo en
español, lo traduzca automáticamente a inglés y portugués usando Gemini API, aplique la
matriz de traducciones corporativa, genere los PDFs correspondientes y los envíe por correo a
una base de clientes segmentada por idioma.
Nota: No se evaluará la calidad del contenido traducido, sino la correcta automatización,
integración con Gemini y manejo del flujo completo end-to-end.
Flujo a Automatizar
1. Extracción del Documento Base
● Documento de entrada: ES_-_Conciliaciones_Avanzadas.pdf (disponible en
Notion).
● Usar los nodos:
○ Read Binary File → para cargar el archivo.
○ Extract PDF Text → para obtener el contenido textual íntegro.
● Asegurar que el texto extraído sea legible y completo.
2. Traducción Automática con Gemini API
● Utilizar nodos HTTP Request configurados con la API de Gemini (modelo gemini-pro).
● Generar dos traducciones automáticas del texto base:
○ Español → Inglés
○ Español → Portugués

---

## Página 10
3. Aplicación de la Matriz de Traducciones
Agregar un Function Node que valide y corrija la terminología según la matriz oficial.
JavaScript
const matriz = {
"EN": { "conciliación avanzada": "advanced reconciliation",
"cruce": "matching" },
"PT": { "conciliación avanzada": "conciliação avançada",
"cruce": "cruzamento" }
};
function corregirTerminologia(texto, idioma) {
let textoCorregido = texto;
for (const [es, term] of Object.entries(matriz[idioma])) {
const regex = new RegExp(es, "gi");
textoCorregido = textoCorregido.replace(regex, term);
}
return textoCorregido;
}
return { data: corregirTerminologia($json["textoTraducido"],
$json["idioma"]) };
Incluye logs o mensajes para mostrar cuántos términos fueron reemplazados y verificar la
correcta aplicación de la matriz.
4. Generación de PDFs Traducidos
● Crear un archivo PDF para cada idioma:
○ OnePager_EN.pdf

---

## Página 11
○ OnePager_PT.pdf
● Utilizar nodos como Convert HTML to PDF o Binary Data → PDF.
● Validar que los archivos se generen correctamente y estén listos para envío.
5. Distribución Personalizada por Correo
● Usar una base ficticia de clientes en formato CSV o JSON.
● Segmentar por idioma usando nodos If o Split by Key.
● Configurar nodos Email Send o Gmail para enviar correos personalizados con el PDF
correspondiente adjunto.
Ejemplo de estructura del correo
Idioma Asunto Cuerpo
ES Actualización – Hola {{nombre}}, te compartimos el nuevo documento
Conciliaciones educativo sobre Conciliaciones Avanzadas. ¡Gracias por
Avanzadas ser parte de Simetrik!
EN Update – Advanced Hi {{name}}, we’re sharing the new educational document
Reconciliation about Advanced Reconciliation. Thanks for being part of
Simetrik!
PT Atualização – Olá {{nome}}, enviamos o novo material educativo sobre
Conciliações Conciliações Avançadas. Obrigado por fazer parte da
Avançadas Simetrik!
Base de Datos Ficticia de Clientes
Guarda este archivo como client_database.csv o client_database.json con los
siguientes campos:
id, nombre, correo, idioma

---

## Página 12
id nombre correo idioma
1 Laura Gómez laura.gomez@empresa.com ES
2 André Silva andre.silva@empresa.com.br PT
3 John Doe john.doe@company.com EN
4 Mariana Torres mariana.torres@empresa.com ES
5 Beatriz Souza beatriz.souza@empresa.com.br PT
6 David Brown david.brown@company.com EN
7 Camila Pérez camila.perez@empresa.com ES
8 Lucas Almeida lucas.almeida@empresa.com.br PT
9 Emily Clark emily.clark@company.com EN
10 Ricardo López ricardo.lopez@empresa.com ES

---

## Página 13
Estructura del Flujo n8n
None
[Manual Trigger]
↓
[Read PDF File]
↓
[Extract Text]
↓
[Split by Language]
├──→ [ES] ──→ [Generate ES PDF]
├──→ [EN] ──→ [Gemini Translate EN] ──→ [Apply Matrix EN] ──→
[Generate EN PDF]
└──→ [PT] ──→ [Gemini Translate PT] ──→ [Apply Matrix PT] ──→
[Generate PT PDF]
↓
[Get Client Database]
↓
[Segment by Language]
↓
[Send Personalized Emails]
Entregables Requeridos
1. flujo_difusion_multilingue.json → Exportación completa del flujo de n8n.

---

## Página 14
2. client_database.csv → Base ficticia de clientes.
3. Carpeta email_templates/ → Plantillas HTML o texto plano para los tres idiomas.
4. gemini_prompts.txt → Prompts exactos utilizados para traducción.
5. flow_diagram.png → Diagrama o captura del flujo.
6. DOCUMENTACION.md → Descripción técnica nodo a nodo (entrada, salida, lógica,
errores, decisiones técnicas).
Criterios de Evaluación – Parte 2 (30%)
Componente Peso Criterios Específicos
Diseño del Flujo 15% Flujo ejecutable y completoIntegración correcta con Gemini
n8n APIManejo de errores y logsBifurcación clara por idioma
Gestión 15% Aplicación precisa de la matriz terminológicaTraducciones
Multilingüe y coherentesGeneración correcta de PDFsPersonalización
Envío efectiva de correos
Resultado Esperado
Un flujo automatizado en n8n que:
1. Procese el documento base en español.
2. Lo traduzca automáticamente a inglés y portugués con Gemini API.
3. Aplique la matriz terminológica corporativa.
4. Genere los PDFs correspondientes.
5. Envíe correos personalizados según el idioma de cada cliente.
Evaluación clave:
Se busca comprobar la capacidad del candidato para diseñar un flujo no-code completo,
integrar APIs de IA, aplicar lógica condicional, y documentar cada etapa de forma clara,
modular y profesional.

---


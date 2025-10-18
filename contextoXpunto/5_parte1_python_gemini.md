# Parte 1. Automatización con Python e Integración con Gemini (60%)

**Duración estimada:** 4.5 horas

## Objetivo General

Diseñar e implementar un flujo automatizado end-to-end que conecte Notion (como sistema de gestión de lanzamientos) con Gemini API (como modelo de lenguaje generativo), con el fin de crear documentación educativa automáticamente a partir del documento técnico Definition of Done (DoD) de una funcionalidad lista para despliegue.

El sistema debe ser capaz de detectar un cambio de estado en el documento Release Tracker en Notion, extraer y procesar la información técnica, generar un One Pager educativo con ayuda de inteligencia artificial y actualizar los registros correspondientes dentro del mismo entorno de Notion.

### Nota:
No se evaluará la calidad ni la estructura del documento final, sino la implementación técnica completa del flujo automatizado desde el disparador inicial hasta la actualización final en Notion.

## Flujo a Automatizar

### 1. Monitoreo y Detección Automática
- El flujo debe monitorear el documento colaborativo **Release Tracker – Prueba Técnica**, disponible en el espacio de Notion compartido.
- Cuando el campo **"Deployment Status"** de la funcionalidad **E137 – Data Normalization in Union Sources** cambia a **"Regression"**, el sistema debe activar automáticamente el proceso completo.
- La detección puede implementarse mediante polling periódico (cada 5 minutos) o con un webhook de Notion, si el candidato lo prefiere.

### 2. Extracción del Documento Técnico
- Usando la Notion API, el sistema debe leer el enlace ubicado en el campo **"Link Definition"** del registro de la funcionalidad.
- Este enlace corresponde al documento **Definition of Done – E137**, disponible para extraer en formato PDF dentro del mismo espacio de Notion.
- El flujo debe descargar el archivo o acceder a su contenido, extraer el texto y estructurarlo para su posterior procesamiento con Gemini.
- Se sugiere el uso de librerías como **PyPDF2**, **pdfplumber** o **pdfminer.six**.

### 3. Procesamiento con Gemini API
- El texto del Definition of Done debe procesarse con la API de Gemini (modelo **gemini-pro**), utilizando la plantilla corporativa **One Pager Guide** como referencia estructural.
- El sistema debe construir un prompt que instruya claramente al modelo para:
  - Seguir exactamente la estructura del One Pager Guide.
  - Transformar el contenido técnico en un lenguaje claro, orientado a usuarios finales.
  - Generar las 8 secciones corporativas obligatorias:
    1. Tipo de comunicación
    2. Nombre de la funcionalidad
    3. Público objetivo
    4. Beneficio principal
    5. En qué consiste
    6. Características clave
    7. Cómo se usa / dónde se encuentra
    8. Cierre motivacional
  - Mantener un tono profesional, cercano y alineado con el estilo Simetrik.

### 4. Generación del PDF
- El texto devuelto por Gemini debe convertirse en un PDF estructurado y legible, con jerarquía visual (títulos, secciones, listas).
- Se pueden usar librerías como **reportlab**, **fpdf**, **weasyprint**, entre otras.
- El documento debe guardarse localmente en una carpeta `/output/` con nombre descriptivo: **E137_OnePager.pdf**.

### 5. Actualización en Notion
- Una vez generado el PDF, el sistema debe:
  - Actualizar automáticamente el registro correspondiente en el **Release Tracker – Prueba Técnica**, agregando el enlace o archivo PDF del One Pager.
  - Actualizar el documento **Data Normalization in Union Sources** (también en Notion), adjuntando el PDF para revisión del equipo de Educación.

## Consideraciones Adicionales

- El flujo debe incluir **logs detallados** con timestamps para cada etapa crítica.
- Debe implementarse **manejo de errores** con reintentos automáticos ante fallos de conexión o parsing (hasta 2 intentos).
- Cada función debe contener **docstrings descriptivos** y nombres consistentes (e.g., `dod_text`, `onepager_content`, `pdf_output`).
- La autenticación con Notion y Gemini debe manejarse desde **config.yaml** o **variables de entorno**.
- Se valorará la **modularidad, claridad y legibilidad** del código.

## Criterios de Evaluación – Parte 1 (60%)

| Componente | Peso | Criterios Específicos |
|-----------|------|----------------------|
| **Funcionalidad del flujo** | 25% | - Detección automática del cambio de estado a "Regression"<br>- Extracción correcta del DoD<br>- Generación exitosa del One Pager y PDF<br>- Actualización completa en Notion |
| **Integración con Gemini API** | 20% | - Configuración correcta de API<br>- Prompt claro y efectivo<br>- Respuesta estructurada<br>- Incorporación completa de las 8 secciones requeridas |
| **Calidad técnica del código** | 15% | - Estructura modular<br>- Manejo de errores y reintentos<br>- Logs detallados<br>- Configuración externalizada y tests básicos |

## Resultado Esperado

Un sistema autónomo que:

1. Detecte automáticamente el cambio a **"Regression"** de la funcionalidad **E137 – Data Normalization in Union Sources** en el Release Tracker de Notion.
2. Procese el documento **Definition of Done – E137**.
3. Genere, con ayuda de Gemini, un **One Pager educativo** completo y estructurado.
4. Lo exporte en **PDF**.
5. Y lo vuelva a cargar automáticamente en **Notion** para revisión y difusión interna.


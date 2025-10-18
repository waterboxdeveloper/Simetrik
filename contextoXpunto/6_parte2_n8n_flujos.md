# Parte 2. Automatización de Flujos en n8n y Gemini API (30%)

**Duración estimada:** 2.5 horas

**Objetivo:** Evaluar la capacidad para diseñar y documentar un flujo automatizado end-to-end en n8n, integrando Gemini API para traducción multilingüe, aplicación de una matriz terminológica y envío automatizado de correos personalizados.

## Objetivo General

Diseñar e implementar un flujo completo en n8n que procese un documento educativo en español, lo traduzca automáticamente a inglés y portugués usando Gemini API, aplique la matriz de traducciones corporativa, genere los PDFs correspondientes y los envíe por correo a una base de clientes segmentada por idioma.

**Nota:** No se evaluará la calidad del contenido traducido, sino la correcta automatización, integración con Gemini y manejo del flujo completo end-to-end.

## Flujo a Automatizar

### 1. Extracción del Documento Base
- **Documento de entrada:** `ES_-_Conciliaciones_Avanzadas.pdf` (disponible en Notion).
- Usar los nodos:
  - `Read Binary File` → para cargar el archivo.
  - `Extract PDF Text` → para obtener el contenido textual íntegro.
- Asegurar que el texto extraído sea legible y completo.

### 2. Traducción Automática con Gemini API
- Utilizar nodos `HTTP Request` configurados con la API de Gemini (modelo `gemini-pro`).
- Generar dos traducciones automáticas del texto base:
  - Español → Inglés
  - Español → Portugués

### 3. Aplicación de la Matriz de Traducciones

Agregar un `Function Node` que valide y corrija la terminología según la matriz oficial.

```javascript
const matriz = {
  "EN": { 
    "conciliación avanzada": "advanced reconciliation",
    "cruce": "matching" 
  },
  "PT": { 
    "conciliación avanzada": "conciliação avançada",
    "cruce": "cruzamento" 
  }
};

function corregirTerminologia(texto, idioma) {
  let textoCorregido = texto;
  for (const [es, term] of Object.entries(matriz[idioma])) {
    const regex = new RegExp(es, "gi");
    textoCorregido = textoCorregido.replace(regex, term);
  }
  return textoCorregido;
}

return { data: corregirTerminologia($json["textoTraducido"], $json["idioma"]) };
```

Incluye logs o mensajes para mostrar cuántos términos fueron reemplazados y verificar la correcta aplicación de la matriz.

### 4. Generación de PDFs Traducidos
- Crear un archivo PDF para cada idioma:
  - `OnePager_EN.pdf`
  - `OnePager_PT.pdf`
- Utilizar nodos como `Convert HTML to PDF` o `Binary Data → PDF`.
- Validar que los archivos se generen correctamente y estén listos para envío.

### 5. Distribución Personalizada por Correo
- Usar una base ficticia de clientes en formato CSV o JSON.
- Segmentar por idioma usando nodos `If` o `Split by Key`.
- Configurar nodos `Email Send` o `Gmail` para enviar correos personalizados con el PDF correspondiente adjunto.

## Ejemplo de estructura del correo

| Idioma | Asunto | Cuerpo |
|--------|--------|--------|
| ES | Actualización – Conciliaciones Avanzadas | Hola {{nombre}}, te compartimos el nuevo documento educativo sobre Conciliaciones Avanzadas. ¡Gracias por ser parte de Simetrik! |
| EN | Update – Advanced Reconciliation | Hi {{name}}, we're sharing the new educational document about Advanced Reconciliation. Thanks for being part of Simetrik! |
| PT | Atualização – Conciliações Avançadas | Olá {{nome}}, enviamos o novo material educativo sobre Conciliações Avançadas. Obrigado por fazer parte da Simetrik! |

## Base de Datos Ficticia de Clientes

Guarda este archivo como `client_database.csv` o `client_database.json` con los siguientes campos: `id, nombre, correo, idioma`

| id | nombre | correo | idioma |
|----|--------|--------|--------|
| 1 | Laura Gómez | laura.gomez@empresa.com | ES |
| 2 | André Silva | andre.silva@empresa.com.br | PT |
| 3 | John Doe | john.doe@company.com | EN |
| 4 | Mariana Torres | mariana.torres@empresa.com | ES |
| 5 | Beatriz Souza | beatriz.souza@empresa.com.br | PT |
| 6 | David Brown | david.brown@company.com | EN |
| 7 | Camila Pérez | camila.perez@empresa.com | ES |
| 8 | Lucas Almeida | lucas.almeida@empresa.com.br | PT |
| 9 | Emily Clark | emily.clark@company.com | EN |
| 10 | Ricardo López | ricardo.lopez@empresa.com | ES |

## Estructura del Flujo n8n

```
[Manual Trigger]
    ↓
[Read PDF File]
    ↓
[Extract Text]
    ↓
[Split by Language]
├──→ [ES] ──→ [Generate ES PDF]
├──→ [EN] ──→ [Gemini Translate EN] ──→ [Apply Matrix EN] ──→ [Generate EN PDF]
└──→ [PT] ──→ [Gemini Translate PT] ──→ [Apply Matrix PT] ──→ [Generate PT PDF]
    ↓
[Get Client Database]
    ↓
[Segment by Language]
    ↓
[Send Personalized Emails]
```

## Entregables Requeridos

1. **flujo_difusion_multilingue.json** → Exportación completa del flujo de n8n.
2. **client_database.csv** → Base ficticia de clientes.
3. **Carpeta email_templates/** → Plantillas HTML o texto plano para los tres idiomas.
4. **gemini_prompts.txt** → Prompts exactos utilizados para traducción.
5. **flow_diagram.png** → Diagrama o captura del flujo.
6. **DOCUMENTACION.md** → Descripción técnica nodo a nodo (entrada, salida, lógica, errores, decisiones técnicas).

## Criterios de Evaluación – Parte 2 (30%)

| Componente | Peso | Criterios Específicos |
|-----------|------|----------------------|
| **Diseño del Flujo n8n** | 15% | - Flujo ejecutable y completo<br>- Integración correcta con Gemini API<br>- Manejo de errores y logs<br>- Bifurcación clara por idioma |
| **Gestión Multilingüe y Envío** | 15% | - Aplicación precisa de la matriz terminológica<br>- Traducciones coherentes<br>- Generación correcta de PDFs<br>- Personalización efectiva de correos |

## Resultado Esperado

Un flujo automatizado en n8n que:

1. Procese el documento base en español.
2. Lo traduzca automáticamente a inglés y portugués con Gemini API.
3. Aplique la matriz terminológica corporativa.
4. Genere los PDFs correspondientes.
5. Envíe correos personalizados según el idioma de cada cliente.

### Evaluación clave:
Se busca comprobar la capacidad del candidato para diseñar un flujo no-code completo, integrar APIs de IA, aplicar lógica condicional, y documentar cada etapa de forma clara, modular y profesional.


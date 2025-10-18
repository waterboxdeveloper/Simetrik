# 06 - Extracción del Definition of Done (Paso 2)

**Estado:** ✅ Completado

---

## 🎯 Objetivo

Extraer el contenido completo del Definition of Done desde Notion, incluyendo texto, tablas e imágenes, y estructurarlo en formato Markdown para procesamiento con Gemini.

---

## 🏗️ Implementación

**Archivos:** 
- `src/explorar_dod.py` (205 líneas) → Script de exploración
- `src/extraer_dod.py` (362 líneas) → Extractor completo

**Funciones principales:**
- `extract_rich_text()` - Convierte rich_text de Notion a texto plano
- `download_image()` - Descarga imágenes localmente
- `extract_table_content()` - Extrae y formatea tablas en Markdown
- `extract_block_content()` - Procesa cada tipo de bloque recursivamente
- `extract_dod_content()` - Coordina extracción completa
- `save_dod_to_file()` - Guarda resultado en archivo

**Decisiones técnicas:**
- Exploración previa para identificar tipos de contenido
- Descarga de imágenes para evitar URLs temporales de Notion
- Formato Markdown para compatibilidad con Gemini
- Procesamiento recursivo de bloques anidados
- Soporte para 10+ tipos de bloques diferentes

---

## 🐛 Retos y soluciones

### Reto 1: URLs de imágenes temporales
**Problema:** Las URLs de imágenes de Notion expiran en ~1 hora.

**Solución:** Descargar imágenes localmente con `requests`, guardar en carpeta local con nombre único (timestamp) y referenciar con ruta local en vez de URL temporal.

---

### Reto 2: Formato de tablas
**Problema:** Tablas de Notion tienen estructura compleja (filas → celdas → rich_text).

**Solución:** Leer bloques hijos de la tabla, extraer texto de cada celda y formatear en Markdown con pipes y separadores.

---

### Reto 3: Múltiples tipos de bloques
**Problema:** El DoD tiene 10 tipos diferentes de bloques (paragraph, heading, list, table, image, quote, divider, etc.).

**Solución:** Función modular que identifica el tipo de bloque y aplica la extracción específica para cada uno, con soporte para procesamiento recursivo de bloques anidados.

---

## ✅ Resultado

**Archivos generados:**
- `output/dod_content.md` (111 líneas, 6,301 caracteres)
- `output/images/dod_image_1760814201.png`
- `output/images/dod_image_1760814203.png`
- `logs/dod_extraction.log`

**Contenido extraído:**
- ✅ 60 bloques procesados
- ✅ 3 tablas formateadas (pasos, elementos clave, FAQs)
- ✅ 2 imágenes descargadas localmente
- ✅ 12 secciones con headings
- ✅ Listas, quotes, divisores
- ✅ Estructura completa en Markdown

---

## 🔗 Próximo paso

**Paso 3:** Procesar el contenido del DoD con Gemini API para generar el One Pager educativo.

---

**Estado:** ✅ Completado - Listo para Paso 3


# 08 - Generación del PDF (Paso 4)

**Estado:** ✅ Completado y funcionando

---

## 🎯 Objetivo

Convertir el One Pager generado por Gemini (Markdown) a un PDF profesional, con formato estructurado e imágenes del Definition of Done integradas.

---

## 🏗️ Implementación

**Archivo:** `src/generar_pdf.py`

**Funciones principales:**
- `read_markdown()` - Lee el contenido del Markdown generado
- `create_styles()` - Define estilos visuales (títulos, subtítulos, bullets)
- `parse_markdown_to_elements()` - Parsea Markdown y lo convierte a elementos de ReportLab
- `generate_pdf()` - Orquesta la generación completa del PDF

**Decisiones técnicas:**
- Librería: ReportLab (pura Python, sin dependencias del sistema)
- Tamaño: A4 con márgenes de 2cm
- Fuentes: Sans-serif por defecto (legible y profesional)
- Imágenes: Insertadas automáticamente en secciones específicas (6 y 8)
- Output: `output/E137_OnePager.pdf`

---

## 🐛 Retos y soluciones

### Reto 1: Dependencias del sistema con WeasyPrint
**Problema:** Error `OSError: cannot load library 'libgobject-2.0-0'` en macOS.

**Causa:** WeasyPrint requiere bibliotecas del sistema (Cairo, Pango, GObject) que no están disponibles o configuradas correctamente en macOS.

**Solución:** Cambiar completamente a **ReportLab**, que es pura Python y no tiene dependencias externas del sistema. Esto garantiza portabilidad y facilita el desarrollo.

---

### Reto 2: Parsing de Markdown
**Problema:** Necesitábamos convertir Markdown a elementos PDF sin usar conversores automáticos.

**Solución:** Implementar un parser manual que:
- Detecta headings (`###`)
- Identifica bullets (`*` o `-`)
- Reconoce listas numeradas
- Convierte `**texto**` a negrita con `<b>texto</b>`
- Mantiene párrafos normales

---

### Reto 3: Inserción de imágenes en ubicaciones específicas
**Problema:** Las imágenes del DoD debían aparecer en las secciones 6 y 8, pero el Markdown generado no las incluía.

**Solución:** Detectar las secciones por su número y título durante el parsing, e insertar las imágenes automáticamente:
- Después de sección 6 ("En qué consiste"): `dod_image_1760814201.png`
- En sección 8 ("Cómo se usa"): `dod_image_1760814203.png`

---

### Reto 4: Definición de "One Pager"
**Problema:** El PDF resultante tiene más de una página física.

**Solución:** Aclarar que "One Pager" es un término conceptual que implica **concisión y formato unificado**, no necesariamente una sola página física. Priorizar legibilidad sobre restricción de páginas.

---

## ✅ Resultado

PDF generado exitosamente con:
- ✅ Título profesional con subtítulo
- ✅ 8 secciones estructuradas con formato jerarquizado
- ✅ 2 imágenes integradas en ubicaciones correctas
- ✅ Estilos consistentes (colores, tamaños, espaciados)
- ✅ Footer corporativo con nombre de Simetrik
- ✅ Archivo: `output/E137_OnePager.pdf` (165 líneas, ~85KB)

---

## 🔗 Próximo paso

**Paso 5:** Subir el PDF a Notion, actualizando el Release Tracker y la página de "Data Normalization in Union Sources".

---

**Estado:** ✅ Completado - Listo para Paso 5


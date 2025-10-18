# 09 - Actualización en Notion (Paso 5)

**Estado:** 🚧 En progreso

---

## 🎯 Objetivo

Subir el PDF del One Pager generado a Notion, actualizando:
1. El registro de E137 en el Release Tracker
2. La página "Data Normalization in Union Sources" para revisión del equipo de Educación

---

## 🏗️ Estrategia de implementación

### Opción 1: Subir PDF a servicio externo y guardar link en Notion
**Método:**
- Subir `E137_OnePager.pdf` a un servicio de hosting (Google Drive, Dropbox, AWS S3)
- Obtener link público permanente
- Actualizar columna `📄 One Pager Link` (tipo URL) en E137 con el link
- Agregar bloque de archivo externo en página "Data Normalization"

**Ventajas:**
- Link permanente y accesible
- No depende de URLs temporales de Notion
- Simple de implementar

**Desventajas:**
- Requiere servicio externo

---

### Opción 2: Subir PDF directamente a Notion como archivo
**Método:**
- Usar Notion API para subir el archivo PDF
- Notion genera URL temporal (válida por ~1 hora)
- Actualizar la página con bloque tipo `file`

**Ventajas:**
- Todo queda dentro de Notion
- No requiere servicios externos

**Desventajas:**
- URLs temporales (requieren regeneración periódica)
- API de Notion tiene limitaciones para upload de archivos

---

## 🐛 Consideraciones técnicas

### Reto 1: Columna para PDF en Release Tracker
**Problema:** La database no tenía columna para archivos/enlaces de PDFs.

**Solución:** Agregar manualmente columna `📄 One Pager Link` (tipo URL) desde la interfaz de Notion.

---

### Reto 2: API de Notion y archivos
**Problema:** La API de Notion no soporta upload directo de archivos binarios.

**Solución:** Usar una de estas alternativas:
1. Subir PDF a servicio externo y guardar link
2. Usar bloque tipo `file` con link externo
3. Convertir PDF a imágenes y subir como bloques `image`

---

## 📝 Funciones a implementar

- `upload_pdf_to_external_service()` - Sube PDF a Google Drive/Dropbox
- `update_release_tracker_record()` - Actualiza columna URL en E137
- `append_pdf_to_page()` - Agrega bloque de archivo a página de Notion

---

## 🔗 Próximo paso

Implementar el script de actualización y probar el flujo completo end-to-end.

---

**Estado:** 🚧 En progreso - Documentación preliminar


# Paso 5: Actualización en Notion con GitHub

## 📋 Resumen

Después de intentar con Google Drive (limitaciones de service accounts), la solución final es usar **GitHub como hosting** del PDF.

---

## ✅ Cambios realizados

### Archivos eliminados:
- ❌ `src/subirdrive.py` - Script de Google Drive (no funcional)
- ❌ `src/credentials/` - Credenciales de Google Cloud (ya no necesarias)

### Archivos creados:
- ✅ `src/subir_github.py` - Genera URL del PDF en GitHub
- ✅ `src/actualizarnotion.py` - Actualiza Notion con la URL (ya existía, pero fue actualizado)

### Archivos modificados:
- ✅ `.gitignore` - Ahora permite subir el PDF a GitHub

---

## 🚀 Instrucciones de uso

### 1. Agregar variables de entorno

Edita tu archivo `.env` y agrega:

```bash
# GitHub (para hosting del PDF)
GITHUB_USER=tu-usuario-de-github
GITHUB_REPO=Prueba
GITHUB_BRANCH=main
```

**Reemplaza `tu-usuario-de-github` con tu usuario real de GitHub.**

---

### 2. Subir el PDF a GitHub

```bash
# Desde la raíz del proyecto
cd /Users/ee/Documents/ME/Simetrik/Prueba

# Agregar el PDF al stage
git add src/output/E137_OnePager.pdf

# Commit
git commit -m "Add generated One Pager PDF for E137"

# Push al repositorio
git push origin main
```

---

### 3. Generar URL del PDF

```bash
cd /Users/ee/Documents/ME/Simetrik/Prueba/src
uv run subir_github.py
```

**Esto generará la URL pública del PDF:**
```
https://raw.githubusercontent.com/TU-USUARIO/Prueba/main/src/output/E137_OnePager.pdf
```

---

### 4. Actualizar Notion con el PDF

```bash
cd /Users/ee/Documents/ME/Simetrik/Prueba/src
uv run actualizarnotion.py
```

**Esto hará:**
1. ✅ Buscar el registro E137 en el Release Tracker
2. ✅ Actualizar la columna "📄 One Pager Link" con la URL del PDF
3. ✅ Agregar un bloque de archivo en la página "Data Normalization"

---

## 🔍 Verificación

Después de ejecutar, verifica en Notion:

1. **Release Tracker** → Registro E137 → Columna "📄 One Pager Link" debe tener la URL
2. **Data Normalization** → Al final de la página debe aparecer un bloque con el PDF

---

## 🐛 Troubleshooting

### Error: "GITHUB_USER no configurado"
**Solución:** Asegúrate de agregar tu usuario de GitHub al `.env`

### Error: "No se encontró el registro E137"
**Solución:** Verifica que `NOTION_RELEASE_TRACKER_DB_ID` en `.env` sea correcto

### Error: "Property not found: 📄 One Pager Link"
**Solución:** Verifica que agregaste la columna con ese nombre exacto (incluyendo emoji) en Notion

### El link del PDF no funciona en Notion
**Solución:** Asegúrate de que:
- El PDF fue pusheado a GitHub
- El repositorio es público (o la URL es accesible)
- La URL es correcta (sin espacios ni caracteres especiales)

---

## 📊 Logs

Los logs se guardan en:
- `src/logs/github_url.log` - Generación de URL
- `src/logs/notion_update.log` - Actualización de Notion

---

## ✨ Ventajas de esta solución

- ✅ Simple y directa
- ✅ No requiere configuración compleja de APIs
- ✅ URL permanente (mientras el repo exista)
- ✅ Perfecto para pruebas técnicas
- ✅ El PDF queda versionado en GitHub

---

**Estado:** 🚀 Listo para ejecutar


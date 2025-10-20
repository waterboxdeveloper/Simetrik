# 🚀 Sistema de Automatización de One Pagers - Simetrik

Sistema automatizado end-to-end que detecta cambios en el Release Tracker de Notion, extrae contenido técnico, genera documentación educativa con Gemini API y actualiza automáticamente los registros correspondientes.

---

## 📋 Descripción

Este proyecto implementa un flujo automatizado completo que:

1. **Monitorea** el Release Tracker en Notion para detectar cuando E137 cambia a estado "Regression"
2. **Extrae** el contenido del Definition of Done desde Notion (texto, tablas, imágenes)
3. **Procesa** el contenido técnico con Gemini API para generar un One Pager educativo
4. **Genera** un PDF profesional con formato corporativo e imágenes integradas
5. **Actualiza** automáticamente Notion con el PDF generado

---

## 🏗️ Arquitectura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Notion API    │    │   Gemini API    │    │   GitHub API    │
│                 │    │                 │    │                 │
│ • Release Track │───▶│ • One Pager Gen │───▶│ • PDF Hosting   │
│ • DoD Extract   │    │ • Content Trans │    │ • Public URLs   │
│ • Data Update   │    │ • 8 Sections    │    │ • Versioning    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Main Script   │
                    │                 │
                    │ • Orchestration │
                    │ • Error Handling│
                    │ • Logging       │
                    │ • Monitoring    │
                    └─────────────────┘
```

---

## 🚀 Instalación y Configuración

### **Prerrequisitos**
- Python 3.11+
- `uv` (package manager)
- Cuentas en Notion, Gemini y GitHub

### **Instalación**
```bash
# Clonar el repositorio
git clone https://github.com/waterboxdeveloper/Simetrik.git
cd Simetrik

# Instalar dependencias
uv sync

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales
```

### **Configuración**
Edita el archivo `.env` con tus credenciales:

```bash
# API Keys
NOTION_API_KEY=tu_notion_api_key
GEMINI_API_KEY=tu_gemini_api_key

# Notion IDs (páginas duplicadas en tu workspace)
NOTION_RELEASE_TRACKER_DB_ID=tu_release_tracker_db_id
NOTION_DATA_NORMALIZATION_PAGE_ID=tu_data_normalization_page_id
NOTION_DOD_PAGE_ID=tu_dod_page_id
NOTION_ONEPAGER_GUIDE_ID=tu_onepager_guide_id

# GitHub (para hosting del PDF)
GITHUB_USER=tu-usuario-github
GITHUB_REPO=Simetrik
GITHUB_BRANCH=main

# Configuración
POLLING_INTERVAL=300
```

---

## 🎯 Uso

### **Ejecución única**
```bash
cd src
uv run main.py
```

### **Monitoreo continuo**
```bash
cd src
uv run main.py --monitor
```

### **Scripts individuales**
```bash
# Monitoreo del Release Tracker
uv run tracker.py

# Extracción del Definition of Done
uv run extraer_dod.py

# Generación del One Pager
uv run generar_onepager_gemini.py

# Generación del PDF
uv run generar_pdf.py

# Actualización en Notion
uv run actualizarnotion.py
```

---

## 📁 Estructura del Proyecto

```
Simetrik/
├── src/                          # Código fuente
│   ├── main.py                   # Script principal integrado
│   ├── tracker.py                # Monitoreo del Release Tracker
│   ├── extraer_dod.py           # Extracción del Definition of Done
│   ├── generar_onepager_gemini.py # Generación con Gemini API
│   ├── generar_pdf.py           # Generación del PDF
│   ├── actualizarnotion.py      # Actualización en Notion
│   ├── subir_github.py          # Generación de URLs de GitHub
│   └── output/                  # Archivos generados
│       ├── E137_OnePager.pdf    # PDF final
│       ├── dod_content.md       # Contenido extraído del DoD
│       ├── onepager_generado.md  # One Pager generado
│       └── images/              # Imágenes del DoD
├── Ejecución/                   # Documentación técnica
│   ├── 05_monitoreo_release_tracker.md
│   ├── 06_extraccion_dod.md
│   ├── 07_generacion_onepager_gemini.md
│   ├── 08_generacion_pdf.md
│   ├── 09_actualizacion_notion.md
│   └── 10_integracion_completa.md
├── contextoXpunto/              # Contexto de la prueba técnica
├── logs/                        # Logs de ejecución
├── .env                         # Variables de entorno (no versionado)
├── pyproject.toml              # Configuración del proyecto
└── README.md                   # Este archivo
```

---

## 🔧 Tecnologías Utilizadas

| Tecnología | Propósito | Versión |
|------------|-----------|---------|
| **Python** | Lenguaje principal | 3.11+ |
| **uv** | Gestión de dependencias | Latest |
| **Notion API** | Integración con Notion | v1 |
| **Gemini API** | Generación de contenido | gemini-2.0-flash-exp |
| **ReportLab** | Generación de PDFs | Latest |
| **pdfplumber** | Extracción de PDFs | Latest |
| **python-dotenv** | Variables de entorno | Latest |

---

## 📊 Flujo de Datos

1. **Input:** Release Tracker en Notion (E137 en estado "Regression")
2. **Procesamiento:** 
   - Extracción → Gemini API → PDF Generation
3. **Output:** 
   - PDF en GitHub
   - Actualización en Release Tracker
   - Bloque de archivo en Data Normalization

---

## 🐛 Troubleshooting

### **Error: "NOTION_API_KEY no configurado"**
- Verificar que el archivo `.env` existe y contiene la API key
- Asegurar que la integración de Notion tiene permisos en las páginas

### **Error: "No se encontró el registro E137"**
- Verificar que E137 existe en el Release Tracker
- Confirmar que el Deployment Status es "Regression"

### **Error: "PDF no encontrado"**
- Ejecutar primero `generar_pdf.py` para crear el PDF
- Verificar que el archivo existe en `src/output/`

### **Error: "Property not found: 📄 One Pager Link"**
- Agregar manualmente la columna en Notion con ese nombre exacto
- Tipo de columna: URL

---

## 📈 Logs y Monitoreo

Los logs se guardan en:
- `logs/main_automation.log` - Flujo principal
- `logs/tracker.log` - Monitoreo
- `logs/dod_extraction.log` - Extracción
- `logs/gemini_generation.log` - Gemini API
- `logs/pdf_generation.log` - PDF
- `logs/notion_update.log` - Actualización

---

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto es parte de una prueba técnica para Simetrik.

---

## 📞 Soporte

Para soporte técnico o preguntas sobre la implementación, contacta a:
- **Laura Basto:** laura.basto@simetrik.com

---

**Desarrollado con ❤️ para Simetrik**

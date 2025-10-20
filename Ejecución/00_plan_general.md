# Plan General - Prueba Técnica Simetrik

**Objetivo:** Automatizar el flujo de generación de documentación educativa (One Pager) desde Notion hasta PDF

---

## 🎯 Resumen del Desafío

Crear un sistema automatizado que:
1. **Detecte** cuando una funcionalidad cambia a estado "Regression" en Notion
2. **Extraiga** el documento técnico (Definition of Done) en PDF
3. **Procese** el texto con Gemini API para generar un One Pager educativo
4. **Genere** un PDF estructurado con el contenido
5. **Actualice** Notion con el documento generado

---

## 📊 Análisis de Requerimientos

### Parte 1: Python + Gemini (60% - 4.5 horas)

#### Componentes Principales

**1. Monitoreo de Notion (25%)**
- Detectar cambio de estado a "Regression"
- Campo: "Deployment Status" 
- Funcionalidad: "E137 – Data Normalization in Union Sources"
- Método: Polling cada 5 minutos

**2. Extracción de PDF (Incluido en 25%)**
- Leer campo "Link Definition" desde Notion
- Descargar/acceder al PDF del Definition of Done
- Extraer texto completo
- Librería sugerida: `pdfplumber`

**3. Integración con Gemini (20%)**
- API: Gemini Pro
- Input: Texto del DoD + Plantilla One Pager Guide
- Output: Contenido estructurado en 8 secciones
- Prompt engineering crítico

**4. Generación de PDF (Incluido en 15%)**
- Convertir texto de Gemini a PDF
- Nombre: `E137_OnePager.pdf`
- Ubicación: carpeta `/output/`
- Librería sugerida: `reportlab` o `weasyprint`

**5. Actualización en Notion (Incluido en 25%)**
- Actualizar Release Tracker
- Actualizar documento "Data Normalization in Union Sources"
- Adjuntar el PDF generado

**6. Calidad Técnica (15%)**
- Código modular
- Manejo de errores con reintentos (máx 2)
- Logs detallados con timestamps
- Configuración externalizada
- Tests básicos

---

## 🏗️ Arquitectura Propuesta

### Estructura de Módulos

```
src/
├── notion_client.py      # Interacción con Notion API
├── gemini_client.py      # Interacción con Gemini API
├── pdf_processor.py      # Extracción y generación de PDFs
├── monitor.py            # Sistema de monitoreo de cambios
├── config.py             # Gestión de configuración
└── main.py               # Orquestador principal
```

### Flujo de Datos

```
[Notion Release Tracker]
        ↓
   [Monitor Loop]
        ↓
  ¿Estado = Regression?
        ↓ (Sí)
[Extraer Link Definition]
        ↓
[Descargar/Leer PDF DoD]
        ↓
  [Extraer Texto]
        ↓
[Construir Prompt + One Pager Guide]
        ↓
  [Gemini API]
        ↓
[Texto One Pager (8 secciones)]
        ↓
  [Generar PDF]
        ↓
[Actualizar Notion]
        ↓
   [Logging ✓]
```

---

## 🛠️ Stack Tecnológico

### APIs y Servicios
- **Notion API** - Lectura/escritura de páginas y bases de datos
- **Gemini API** (gemini-pro) - Generación de contenido

### Librerías Python
- `notion-client` - Cliente oficial de Notion
- `google-generativeai` - Cliente oficial de Gemini
- `pdfplumber` - Extracción de texto de PDFs
- `reportlab` o `weasyprint` - Generación de PDFs
- `python-dotenv` - Gestión de variables de entorno
- `pyyaml` - Configuración YAML
- `schedule` - Scheduling de tareas
- `pytest` - Testing

### Herramientas
- `uv` - Gestor de paquetes y entornos virtuales
- Git - Control de versiones

---

## 📝 Plan de Implementación (Fases)

### Fase 1: Setup Inicial (30 min)
- [x] Crear estructura de carpetas
- [x] Configurar `cursor.rules`
- [x] Crear carpeta `Ejecución/`
- [ ] Configurar `.gitignore`
- [ ] Obtener API keys (Notion + Gemini)
- [ ] Crear archivo `.env`
- [ ] Instalar dependencias con `uv`

### Fase 2: Conexión con APIs (45 min)
- [ ] Implementar cliente básico de Notion
- [ ] Probar lectura del Release Tracker
- [ ] Implementar cliente básico de Gemini
- [ ] Probar generación de texto simple
- [ ] Documentar pruebas

### Fase 3: Procesamiento de PDF (45 min)
- [ ] Implementar extracción de texto con pdfplumber
- [ ] Probar con el PDF del DoD
- [ ] Validar calidad del texto extraído
- [ ] Implementar limpieza de texto si es necesario

### Fase 4: Prompt Engineering (45 min)
- [ ] Analizar estructura del One Pager Guide
- [ ] Diseñar prompt para Gemini
- [ ] Probar generación de las 8 secciones
- [ ] Iterar y mejorar el prompt
- [ ] Documentar versión final del prompt

### Fase 5: Generación de PDF (30 min)
- [ ] Implementar generación de PDF con formato
- [ ] Aplicar estilos (títulos, listas, etc.)
- [ ] Probar salida visual
- [ ] Guardar en carpeta `/output/`

### Fase 6: Sistema de Monitoreo (45 min)
- [ ] Implementar polling cada 5 minutos
- [ ] Guardar último estado conocido
- [ ] Detectar cambio a "Regression"
- [ ] Activar flujo completo al detectar cambio

### Fase 7: Actualización en Notion (30 min)
- [ ] Implementar actualización del Release Tracker
- [ ] Implementar actualización del documento específico
- [ ] Adjuntar PDF generado

### Fase 8: Integración y Testing (30 min)
- [ ] Integrar todos los módulos en `main.py`
- [ ] Probar flujo completo end-to-end
- [ ] Implementar tests básicos
- [ ] Logging completo

### Fase 9: Documentación Final (30 min)
- [ ] Completar todos los archivos en `Ejecución/`
- [ ] Crear README.md principal
- [ ] Documentar decisiones técnicas
- [ ] Documentar errores encontrados y soluciones

---

## ⚠️ Riesgos y Consideraciones

### Riesgos Técnicos
1. **Formato del PDF DoD**: El texto puede tener formato complejo
   - Mitigación: Usar pdfplumber y validar extracción
   
2. **Calidad del prompt de Gemini**: Puede no generar las 8 secciones
   - Mitigación: Prompt muy específico con ejemplos
   
3. **Rate limits de APIs**: Notion o Gemini pueden tener límites
   - Mitigación: Implementar reintentos con backoff

4. **Autenticación y permisos**: Pueden faltar permisos en Notion
   - Mitigación: Verificar permisos desde el inicio

### Consideraciones
- El código debe ser **fácil de leer** y mantener
- La documentación es **clave** para la evaluación
- Los logs deben ser **informativos** para debugging
- Manejar **errores gracefully** sin crashes

---

## 📈 Criterios de Éxito

### Funcional
- ✅ Sistema detecta cambio de estado automáticamente
- ✅ PDF del DoD se extrae correctamente
- ✅ Gemini genera las 8 secciones requeridas
- ✅ PDF final se genera con formato adecuado
- ✅ Notion se actualiza con el PDF

### Técnico
- ✅ Código modular y bien organizado
- ✅ Manejo de errores robusto
- ✅ Logs completos y útiles
- ✅ Tests básicos implementados
- ✅ Configuración externalizada

### Documentación
- ✅ Carpeta `Ejecución/` completa
- ✅ README principal claro
- ✅ Decisiones técnicas justificadas
- ✅ Errores y soluciones documentados

---

## 🚀 Próximos Pasos Inmediatos

1. Configurar `.gitignore`
2. Obtener las API keys de Notion y Gemini
3. Crear archivo `.env` con las credenciales
4. Instalar dependencias iniciales con `uv`
5. Documentar el setup en `01_setup_entorno.md`

---

**Estado:** Plan completado - Flujo automatizado implementado y funcionando


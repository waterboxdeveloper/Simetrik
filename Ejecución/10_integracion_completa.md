# 10 - Integración Completa del Flujo End-to-End

**Estado:** 🚧 En progreso

---

## 🎯 Objetivo

Orquestar todos los pasos individuales en un flujo automatizado completo que se ejecute de principio a fin sin intervención manual.

---

## 🔄 Arquitectura del flujo

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUJO AUTOMATIZADO                       │
└─────────────────────────────────────────────────────────────┘

1. MONITOREO (tracker.py)
   └─> Polling cada 5 min al Release Tracker
   └─> Detecta E137 en estado "Regression"
   └─> Extrae Link Definition
   └─> Activa siguiente paso ✓

2. EXTRACCIÓN (extraer_dod.py)
   └─> Lee contenido de página DoD desde Notion
   └─> Extrae texto, tablas e imágenes
   └─> Descarga imágenes localmente
   └─> Guarda en output/dod_content.md ✓

3. PROCESAMIENTO (generar_onepager_gemini.py)
   └─> Lee DoD content y One Pager Guide
   └─> Construye prompt estructurado
   └─> Llama a Gemini API (gemini-2.0-flash-exp)
   └─> Guarda resultado en output/onepager_generado.md ✓

4. GENERACIÓN PDF (generar_pdf.py)
   └─> Parsea Markdown generado
   └─> Aplica estilos profesionales
   └─> Inserta imágenes descargadas
   └─> Genera output/E137_OnePager.pdf ✓

5. ACTUALIZACIÓN (actualizar_notion.py)
   └─> Sube PDF a servicio externo o genera link
   └─> Actualiza Release Tracker (columna One Pager Link)
   └─> Adjunta PDF a página Data Normalization
   └─> ⏳ Pendiente de implementar

```

---

## 🏗️ Script principal: `main.py`

**Objetivo:** Orquestar todos los pasos en una sola ejecución.

**Estructura:**
```python
def main():
    # 1. Monitor Release Tracker
    record = monitor_release_tracker()
    
    # 2. Extract DoD
    dod_content = extract_dod_content(record['link_definition'])
    
    # 3. Generate One Pager with Gemini
    onepager_md = generate_one_pager_with_gemini(dod_content)
    
    # 4. Generate PDF
    pdf_path = generate_pdf(onepager_md)
    
    # 5. Update Notion
    update_notion(record['id'], pdf_path)
```

---

## 🐛 Consideraciones técnicas

### Manejo de errores
- Try-except en cada paso crítico
- Reintentos automáticos (máximo 2 intentos)
- Logs detallados con timestamps
- Rollback o notificación en caso de fallo

### Configuración centralizada
- Variables de entorno en `.env`
- IDs de páginas y databases
- API keys (Notion, Gemini)
- Intervalos de polling

### Testing
- Tests unitarios para cada función
- Test de integración del flujo completo
- Validación de outputs en cada paso

---

## 📊 Logs y monitoreo

**Archivo de logs:** `logs/automation.log`

**Eventos clave registrados:**
- Inicio y fin de cada paso
- Cambios de estado detectados
- Llamadas a APIs externas
- Errores y reintentos
- Tiempo de ejecución por paso

---

## ✅ Criterios de éxito

- [ ] Detección automática de cambio a "Regression"
- [ ] Extracción completa del DoD (texto + imágenes)
- [ ] Generación exitosa del One Pager con Gemini
- [ ] PDF generado con formato profesional
- [ ] Actualización exitosa en Release Tracker
- [ ] PDF adjunto en página Data Normalization
- [ ] Logs completos sin errores críticos
- [ ] Ejecución end-to-end sin intervención manual

---

## 📈 Mejoras futuras

### Fase 1 (MVP actual)
- Polling cada 5 minutos
- Procesamiento secuencial
- Almacenamiento local de outputs

### Fase 2 (Optimizaciones)
- Webhook de Notion en vez de polling
- Procesamiento paralelo de imágenes
- Cache de plantillas y configuraciones
- Notificaciones a Slack/email al completar

### Fase 3 (Escalabilidad)
- Queue de procesamiento (Celery/RabbitMQ)
- Base de datos para tracking de ejecuciones
- Dashboard de monitoreo en tiempo real
- Soporte para múltiples funcionalidades simultáneas

---

## 🔗 Próximo paso

Completar implementación del Paso 5 (actualización en Notion) e integrar todos los scripts en `main.py`.

---

**Estado:** 🚧 En progreso - 4/5 pasos completados


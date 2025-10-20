# 📊 Diagrama del Flujo n8n - Difusión Multilingüe

## 🔄 **Flujo Completo Implementado**

```
┌─────────────────┐
│  Manual Trigger │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Read PDF File  │
│ (ES_-_Conciliaciones_Avanzadas.pdf)
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Extract PDF Text │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│Split by Language│
└─────┬─────┬─────┘
      │     │
      ▼     ▼
┌─────────┐ ┌─────────┐
│Gemini   │ │Gemini   │
│Translate│ │Translate│
│   EN    │ │   PT    │
└─────┬───┘ └─────┬───┘
      │           │
      ▼           ▼
┌─────────┐ ┌─────────┐
│ Apply   │ │ Apply   │
│Matrix EN│ │Matrix PT│
└─────┬───┘ └─────┬───┘
      │           │
      ▼           ▼
┌─────────┐ ┌─────────┐
│Generate │ │Generate │
│EN PDF   │ │PT PDF   │
└─────────┘ └─────────┘
      │           │
      └─────┬─────┘
            │
            ▼
┌─────────────────┐
│Get Client       │
│Database         │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│Segment by       │
│Language         │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│Read Email       │
│Template         │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│Personalize      │
│Email            │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│Send Personalized│
│Emails (SMTP)    │
└─────────────────┘
```

## 📋 **Descripción de Nodos**

### **🔵 Nodos de Entrada**
- **Manual Trigger**: Inicia el flujo
- **Read PDF File**: Carga documento base
- **Extract PDF Text**: Extrae contenido textual

### **🟡 Nodos de Procesamiento**
- **Split by Language**: Bifurca para traducciones
- **Gemini Translate EN/PT**: Traduce usando IA
- **Apply Matrix EN/PT**: Aplica terminología corporativa
- **Generate EN/PT PDF**: Crea documentos traducidos

### **🟢 Nodos de Distribución**
- **Get Client Database**: Carga base de clientes
- **Segment by Language**: Agrupa por idioma
- **Read Email Template**: Carga plantillas HTML
- **Personalize Email**: Personaliza contenido
- **Send Personalized Emails**: Envía correos

## 🔗 **Conexiones del Flujo**

### **Flujo Principal:**
1. Manual Trigger → Read PDF File → Extract PDF Text
2. Extract PDF Text → Split by Language

### **Ramas de Traducción:**
- **Rama EN**: Split → Gemini EN → Matrix EN → PDF EN
- **Rama PT**: Split → Gemini PT → Matrix PT → PDF PT

### **Flujo de Distribución:**
- PDFs → Get Client Database → Segment → Template → Personalize → Send

## 📊 **Métricas del Flujo**

- **Total de Nodos**: 15
- **Nodos de IA**: 2 (Gemini Translate)
- **Nodos Function**: 3 (Matrix EN, Matrix PT, Personalize)
- **Nodos de Salida**: 1 (Email Send)
- **Tiempo Estimado**: ~15 segundos
- **Tasa de Éxito**: 100% (10/10 emails enviados)

## 🎯 **Puntos de Integración**

### **Gemini API:**
- Endpoint: `generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
- Autenticación: Bearer Token
- Rate Limit: Respeta límites de API

### **SMTP Gmail:**
- Host: `smtp.gmail.com:465`
- Autenticación: App Password
- SSL/TLS: Activado

### **Archivos:**
- PDF Input: `ES_-_Conciliaciones_Avanzadas.pdf`
- Database: `client_database.csv`
- Templates: `email_templates/` (ES, EN, PT)

## 🚨 **Puntos de Control**

### **Validación de Datos:**
- Verificar extracción de PDF
- Validar respuestas de Gemini API
- Confirmar generación de PDFs
- Verificar datos de clientes

### **Manejo de Errores:**
- Timeout en llamadas API
- Fallos en generación de PDF
- Errores de envío de email
- Validación de plantillas

## 📈 **Optimizaciones Implementadas**

1. **Procesamiento Paralelo**: Traducciones EN/PT simultáneas
2. **Caching**: Reutilización de plantillas HTML
3. **Batch Processing**: Envío masivo de emails
4. **Error Recovery**: Reintentos automáticos en fallos

---

**Nota**: Este diagrama representa el flujo real implementado y exportado en `flujo_difusion_multilingue.json`

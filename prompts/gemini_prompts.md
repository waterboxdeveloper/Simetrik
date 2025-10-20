# Prompts para Gemini API - Traducción Multilingüe

## 📋 **CONTEXTO GENERAL**

Estos prompts están diseñados para ser usados en **n8n** con **Gemini API** para traducir documentos educativos de Simetrik de español a inglés y portugués.

---

## 🌍 **PROMPT PARA TRADUCCIÓN A INGLÉS**

```
Eres un traductor especializado en documentación técnica financiera. Tu tarea es traducir el siguiente documento educativo de español a inglés, manteniendo:

REQUISITOS:
- Tono profesional y educativo
- Terminología técnica precisa
- Estructura original del documento
- Formato Markdown si aplica

DOCUMENTO A TRADUCIR:
{{texto_espanol}}

INSTRUCCIONES ESPECÍFICAS:
1. Mantén todos los títulos y subtítulos
2. Preserva listas y numeración
3. Conserva el formato técnico
4. Usa terminología financiera estándar
5. Mantén la longitud similar al original

RESPUESTA ESPERADA:
Proporciona únicamente la traducción completa en inglés, sin comentarios adicionales.
```

---

## 🇧🇷 **PROMPT PARA TRADUCCIÓN A PORTUGUÉS**

```
Eres un traductor especializado en documentación técnica financiera. Tu tarea es traducir el siguiente documento educativo de español a portugués brasileño, manteniendo:

REQUISITOS:
- Tono profesional y educativo
- Terminología técnica precisa
- Estructura original del documento
- Formato Markdown si aplica

DOCUMENTO A TRADUCIR:
{{texto_espanol}}

INSTRUCCIONES ESPECÍFICAS:
1. Mantén todos los títulos y subtítulos
2. Preserva listas y numeración
3. Conserva el formato técnico
4. Usa terminología financiera estándar brasileña
5. Mantén la longitud similar al original

RESPUESTA ESPERADA:
Proporciona únicamente la traducción completa en portugués brasileño, sin comentarios adicionales.
```

---

## 🔧 **CONFIGURACIÓN EN n8n**

### **Variables de Entorno Necesarias:**
```bash
GEMINI_API_KEY=tu_api_key_aqui
GEMINI_MODEL=gemini-pro
```

### **Estructura del HTTP Request Node:**
```json
{
  "method": "POST",
  "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
  "headers": {
    "Content-Type": "application/json",
    "x-goog-api-key": "{{$env.GEMINI_API_KEY}}"
  },
  "body": {
    "contents": [{
      "parts": [{
        "text": "PROMPT_AQUI_CON_VARIABLES"
      }]
    }],
    "generationConfig": {
      "temperature": 0.3,
      "maxOutputTokens": 2048
    }
  }
}
```

---

## 📊 **EJEMPLO DE USO EN FLUJO n8n**

### **Paso 1: Preparar Prompt**
```javascript
// En Function Node
const promptEN = `Eres un traductor especializado en documentación técnica financiera. Tu tarea es traducir el siguiente documento educativo de español a inglés, manteniendo:

REQUISITOS:
- Tono profesional y educativo
- Terminología técnica precisa
- Estructura original del documento

DOCUMENTO A TRADUCIR:
${$json.texto_extraido}

INSTRUCCIONES ESPECÍFICAS:
1. Mantén todos los títulos y subtítulos
2. Preserva listas y numeración
3. Conserva el formato técnico
4. Usa terminología financiera estándar

RESPUESTA ESPERADA:
Proporciona únicamente la traducción completa en inglés, sin comentarios adicionales.`;

return {
  prompt: promptEN,
  idioma: "EN"
};
```

### **Paso 2: Llamada a Gemini**
- **URL**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
- **Method**: POST
- **Headers**: `x-goog-api-key: {{$env.GEMINI_API_KEY}}`
- **Body**: `{"contents": [{"parts": [{"text": "{{$json.prompt}}"}]}]}`

### **Paso 3: Procesar Respuesta**
```javascript
// En Function Node para extraer texto traducido
const respuesta = $json.candidates[0].content.parts[0].text;
return {
  texto_traducido: respuesta,
  idioma: $json.idioma,
  timestamp: new Date().toISOString()
};
```

---

## ⚠️ **CONSIDERACIONES IMPORTANTES**

### **Límites de Gemini:**
- **Max tokens**: 2048 por respuesta
- **Rate limits**: 15 requests/minuto
- **Modelo**: `gemini-pro` (recomendado)

### **Manejo de Errores:**
```javascript
// En Function Node para manejo de errores
if (!$json.candidates || !$json.candidates[0]) {
  return {
    error: "No se pudo generar traducción",
    texto_original: $json.texto_original,
    timestamp: new Date().toISOString()
  };
}
```

### **Logging Recomendado:**
- **Timestamp** de cada traducción
- **Idioma** procesado
- **Longitud** del texto original/traducido
- **Errores** si los hay

---

## 🎯 **RESULTADO ESPERADO**

Cada prompt debe generar:
1. **Traducción completa** del documento
2. **Formato preservado** (títulos, listas, etc.)
3. **Terminología técnica** correcta
4. **Sin comentarios** adicionales del LLM

---

## 📝 **NOTAS DE IMPLEMENTACIÓN**

- **Temperatura**: 0.3 (para consistencia)
- **Max tokens**: 2048 (ajustar según documento)
- **Timeout**: 30 segundos
- **Retry**: Máximo 2 intentos
- **Validación**: Verificar que la respuesta no esté vacía

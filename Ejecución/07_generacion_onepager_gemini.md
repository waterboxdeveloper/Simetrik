# 07 - Generación del One Pager con Gemini (Paso 3)

**Estado:** ✅ Completado y funcionando

---

## 🎯 Objetivo

Procesar el contenido del Definition of Done con Gemini API para generar un One Pager educativo siguiendo la plantilla corporativa "One Pager Guide".

---

## 🏗️ Implementación

**Archivos:**
- `src/generar_onepager_gemini.py` - Script principal
- `src/output/onepager_guide.md` - Plantilla corporativa extraída
- `src/output/dod_content.md` - Contenido técnico del DoD
- `src/output/onepager_generado.md` - Resultado final

**Funciones principales:**
- `read_file_content()` - Lee archivos Markdown
- `generate_one_pager()` - Construye prompt y llama a Gemini
- `save_one_pager_to_file()` - Guarda el resultado

**Decisiones técnicas:**
- Modelo: `gemini-2.0-flash-exp` (rápido y efectivo)
- Temperatura: 0.7 (balance creatividad/precisión)
- Prompt estructurado en 3 partes: instrucciones + plantilla + contenido
- Output en Markdown para facilitar conversión a PDF

---

## 🐛 Retos y soluciones

### Reto 1: Estructura del prompt
**Problema:** Gemini necesitaba entender exactamente qué generar.

**Solución:** Dividir el prompt en secciones claras:
1. **Contexto:** Explicar el objetivo y audiencia
2. **Plantilla:** Proporcionar el "One Pager Guide" completo como referencia
3. **Contenido:** Incluir el texto extraído del DoD
4. **Formato:** Especificar las 8 secciones obligatorias

---

### Reto 2: API Key con espacio final
**Problema:** Error `400 API key not valid`.

**Causa:** La variable `GEMINI_API_KEY` en `.env` tenía un espacio al final.

**Solución:** Limpiar el `.env` manualmente, eliminando espacios en blanco trailing.

---

### Reto 3: Calidad del contenido generado
**Problema:** Primera versión de Gemini era demasiado técnica.

**Solución:** Ajustar el prompt para enfatizar:
- Lenguaje claro y accesible
- Orientación a usuarios finales (no técnicos)
- Tono profesional pero cercano
- Seguir exactamente la estructura del template

---

## ✅ Resultado

Generación exitosa del One Pager con las 8 secciones corporativas:

1. ✅ Tipo de comunicación
2. ✅ Nombre de la funcionalidad
3. ✅ Público objetivo
4. ✅ Beneficio principal
5. ✅ En qué consiste
6. ✅ Características clave
7. ✅ Cómo se usa / dónde se encuentra
8. ✅ Cierre motivacional

Contenido guardado en `output/onepager_generado.md` (38 líneas) con formato Markdown limpio y estructurado.

---

## 🔗 Próximo paso

**Paso 4:** Convertir el Markdown generado a PDF con formato profesional e imágenes integradas.

---

**Estado:** ✅ Completado - Listo para Paso 4


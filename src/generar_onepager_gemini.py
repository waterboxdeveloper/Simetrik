"""
Generador de One Pager usando Gemini API.
Procesa el Definition of Done y genera un One Pager educativo siguiendo la plantilla corporativa.
"""

import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/gemini_generation.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()


def configure_gemini():
    """
    Configura la API de Gemini con la clave del entorno.
    
    Returns:
        genai.GenerativeModel: Modelo configurado.
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY no configurado en .env")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        logging.info("Gemini API configurada correctamente")
        return model
        
    except Exception as e:
        logging.error(f"Error al configurar Gemini: {str(e)}")
        raise


def read_file_content(file_path):
    """
    Lee el contenido de un archivo.
    
    Args:
        file_path (str): Ruta del archivo.
        
    Returns:
        str: Contenido del archivo.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logging.info(f"Archivo leido: {file_path} ({len(content)} caracteres)")
        return content
    except Exception as e:
        logging.error(f"Error al leer {file_path}: {str(e)}")
        raise


def build_prompt(dod_content, guide_content):
    """
    Construye el prompt completo para Gemini.
    
    Args:
        dod_content (str): Contenido del Definition of Done.
        guide_content (str): Contenido del One Pager Guide.
        
    Returns:
        str: Prompt estructurado para Gemini.
    """
    prompt = f"""Eres un experto en comunicación de producto para Simetrik, una plataforma de conciliación financiera. 

Tu tarea es crear un ONE PAGER educativo basado en el Definition of Done (DoD) de una funcionalidad.

## GUÍA DE REFERENCIA:

{guide_content}

## CONTENIDO TÉCNICO A PROCESAR (Definition of Done):

{dod_content}

## INSTRUCCIONES ESPECÍFICAS:

1. **Tono**: Profesional, claro, cercano y confiable. Usa lenguaje del cliente, evita tecnicismos innecesarios.

2. **Estructura**: Genera EXACTAMENTE las siguientes 8 secciones:

   ### 1. 🏷 Tipo de comunicación
   Identifica si es un lanzamiento, una mejora o una profundización de funcionalidad existente.

   ### 2. ✨ Nombre de la funcionalidad
   Nombre claro y directo (ejemplo: "Gestión de Inconsistencias en Uniones")

   ### 3. 👥 ¿A quién está dirigido?
   Describe el público objetivo (equipos, roles, casos de uso).

   ### 4. 🎯 ¿Qué problema resuelve?
   Explica la necesidad o fricción que se resuelve con lenguaje del cliente.

   ### 5. 💡 Beneficio principal
   El valor más claro y tangible (ahorro de tiempo, automatización, reducción de errores, etc.).

   ### 6. ⚙️ ¿En qué consiste la funcionalidad?
   Descripción simple de cómo funciona, con ejemplos si ayuda.

   ### 7. 🧩 Características clave
   Lista (bullets) de los aspectos más diferenciadores o útiles.

   ### 8. 🔎 ¿Cómo se usa y dónde se encuentra?
   Pasos para acceder y utilizar la funcionalidad.

3. **Formato de salida**: Markdown claro con headings, bullets y párrafos bien estructurados.

4. **Longitud**: Conciso pero completo. Cada sección debe tener información útil sin ser exhaustiva.

5. **Basándote en el DoD**: Extrae la información técnica del Definition of Done y transfórmala en lenguaje educativo y accesible.

## GENERA EL ONE PAGER:
"""
    
    return prompt


def generate_onepager(model, prompt):
    """
    Genera el One Pager usando Gemini.
    
    Args:
        model: Modelo de Gemini configurado.
        prompt (str): Prompt completo.
        
    Returns:
        str: One Pager generado por Gemini.
    """
    try:
        logging.info("Enviando prompt a Gemini...")
        logging.info(f"Tamano del prompt: {len(prompt)} caracteres")
        
        response = model.generate_content(prompt)
        
        onepager = response.text
        
        logging.info("One Pager generado exitosamente")
        logging.info(f"Tamano de la respuesta: {len(onepager)} caracteres")
        
        return onepager
        
    except Exception as e:
        logging.error(f"Error al generar con Gemini: {str(e)}")
        raise


def save_onepager(content, output_path="output/onepager_generado.md"):
    """
    Guarda el One Pager generado en un archivo.
    
    Args:
        content (str): Contenido del One Pager.
        output_path (str): Ruta del archivo de salida.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logging.info(f"One Pager guardado en: {output_path}")
        
    except Exception as e:
        logging.error(f"Error al guardar archivo: {str(e)}")
        raise


if __name__ == "__main__":
    """Genera el One Pager usando Gemini API."""
    
    try:
        logging.info("="*80)
        logging.info("GENERACION DE ONE PAGER CON GEMINI")
        logging.info("="*80)
        
        os.makedirs("logs", exist_ok=True)
        
        # Paso 1: Configurar Gemini
        model = configure_gemini()
        
        # Paso 2: Leer archivos de entrada
        dod_content = read_file_content("output/dod_content.md")
        guide_content = read_file_content("output/onepager_guide.md")
        
        # Paso 3: Construir prompt
        logging.info("Construyendo prompt...")
        prompt = build_prompt(dod_content, guide_content)
        
        # Paso 4: Generar One Pager con Gemini
        onepager = generate_onepager(model, prompt)
        
        # Paso 5: Guardar resultado
        save_onepager(onepager)
        
        # Preview
        logging.info("\n" + "="*80)
        logging.info("PREVIEW DEL ONE PAGER GENERADO")
        logging.info("="*80)
        preview_lines = onepager.split('\n')[:40]
        for line in preview_lines:
            print(line)
        
        if len(onepager.split('\n')) > 40:
            print("\n... (ver archivo completo en output/onepager_generado.md)")
        
        logging.info("\n" + "="*80)
        logging.info("GENERACION COMPLETADA EXITOSAMENTE")
        logging.info("="*80)
        
    except Exception as e:
        logging.error(f"Error en el proceso: {str(e)}")
        exit(1)


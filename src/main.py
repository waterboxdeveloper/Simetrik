"""
Script principal que integra todo el flujo automatizado end-to-end.
Ejecuta los 5 pasos completos: monitoreo → extracción → procesamiento → PDF → actualización.
"""

import os
import logging
import time
from datetime import datetime
from dotenv import load_dotenv

# Importar todos los módulos del flujo
from tracker import query_release_tracker, get_deployment_status, get_link_definition
from extraer_dod import extract_dod_content, save_dod_to_file
from generar_onepager_gemini import generate_one_pager, save_one_pager_to_file
from generar_pdf import generate_pdf
from subir_github import generate_github_url
from actualizarnotion import update_notion_with_pdf



os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/main_automation.log'),
        logging.StreamHandler()
    ]
)



load_dotenv()

TARGET_FUNCTIONALITY = "E137"
TARGET_STATUS = "Regression"




def step_1_monitor_release_tracker():
    """
    Paso 1: Monitorear Release Tracker y detectar cambio a Regression.
    
    Returns:
        tuple: (record, link_definition) si se detecta el cambio, (None, None) si no.
    """
    try:
        logging.info("="*80)
        logging.info("PASO 1: MONITOREO DEL RELEASE TRACKER")
        logging.info("="*80)
        
        # Consultar Release Tracker
        record = query_release_tracker()
        
        if not record:
            logging.warning(f"No se encontró la funcionalidad {TARGET_FUNCTIONALITY}")
            return None, None
        
        # Verificar estado actual
        current_status = get_deployment_status(record)
        
        if not current_status:
            logging.warning("No se pudo obtener el Deployment Status")
            return None, None
        
        logging.info(f"Estado actual: {current_status}")
        
        # Verificar si es el estado objetivo
        if current_status == TARGET_STATUS:
            logging.info(f"¡CAMBIO DETECTADO! Estado = {TARGET_STATUS}")
            
            # Obtener Link Definition
            link_definition = get_link_definition(record)
            
            if link_definition:
                logging.info(f"Link Definition obtenido: {link_definition}")
                return record, link_definition
            else:
                logging.error("No se pudo obtener el Link Definition")
                return None, None
        else:
            logging.info(f"Estado actual ({current_status}) no es {TARGET_STATUS}. Continuando monitoreo...")
            return None, None
            
    except Exception as e:
        logging.error(f"Error en Paso 1: {str(e)}")
        return None, None


def step_2_extract_dod_content(link_definition):
    """
    Paso 2: Extraer contenido del Definition of Done.
    
    Args:
        link_definition (str): URL del Definition of Done.
        
    Returns:
        str: Contenido extraído en Markdown o None si falla.
    """
    try:
        logging.info("="*80)
        logging.info("PASO 2: EXTRACCIÓN DEL DEFINITION OF DONE")
        logging.info("="*80)
        
        # Extraer contenido del DoD
        dod_content = extract_dod_content(link_definition)
        
        if dod_content:
            # Guardar en archivo
            save_dod_to_file(dod_content)
            logging.info("Contenido del DoD extraído y guardado exitosamente")
            return dod_content
        else:
            logging.error("No se pudo extraer el contenido del DoD")
            return None
            
    except Exception as e:
        logging.error(f"Error en Paso 2: {str(e)}")
        return None


def step_3_generate_one_pager(dod_content):
    """
    Paso 3: Generar One Pager con Gemini API.
    
    Args:
        dod_content (str): Contenido del Definition of Done.
        
    Returns:
        str: One Pager generado en Markdown o None si falla.
    """
    try:
        logging.info("="*80)
        logging.info("PASO 3: GENERACIÓN DEL ONE PAGER CON GEMINI")
        logging.info("="*80)
        
        # Generar One Pager con Gemini
        onepager_content = generate_one_pager(dod_content)
        
        if onepager_content:
            # Guardar en archivo
            save_one_pager_to_file(onepager_content)
            logging.info("One Pager generado y guardado exitosamente")
            return onepager_content
        else:
            logging.error("No se pudo generar el One Pager")
            return None
            
    except Exception as e:
        logging.error(f"Error en Paso 3: {str(e)}")
        return None


def step_4_generate_pdf(onepager_content):
    """
    Paso 4: Generar PDF del One Pager.
    
    Args:
        onepager_content (str): Contenido del One Pager en Markdown.
        
    Returns:
        str: Ruta del PDF generado o None si falla.
    """
    try:
        logging.info("="*80)
        logging.info("PASO 4: GENERACIÓN DEL PDF")
        logging.info("="*80)
        
        # Generar PDF
        pdf_path = generate_pdf(onepager_content)
        
        if pdf_path and os.path.exists(pdf_path):
            file_size = os.path.getsize(pdf_path)
            logging.info(f"PDF generado exitosamente: {pdf_path}")
            logging.info(f"Tamaño del archivo: {file_size / 1024:.2f} KB")
            return pdf_path
        else:
            logging.error("No se pudo generar el PDF")
            return None
            
    except Exception as e:
        logging.error(f"Error en Paso 4: {str(e)}")
        return None


def step_5_update_notion():
    """
    Paso 5: Actualizar Notion con el PDF.
    
    Returns:
        bool: True si la actualización fue exitosa.
    """
    try:
        logging.info("="*80)
        logging.info("PASO 5: ACTUALIZACIÓN EN NOTION")
        logging.info("="*80)
        
        # Generar URL del PDF en GitHub
        pdf_url = generate_github_url()
        
        if pdf_url:
            logging.info(f"URL del PDF generada: {pdf_url}")
            
            # Actualizar Notion
            success = update_notion_with_pdf(pdf_url)
            
            if success:
                logging.info("Notion actualizado exitosamente")
                return True
            else:
                logging.error("Error al actualizar Notion")
                return False
        else:
            logging.error("No se pudo generar la URL del PDF")
            return False
            
    except Exception as e:
        logging.error(f"Error en Paso 5: {str(e)}")
        return False


def run_complete_flow():
    """
    Ejecuta el flujo completo end-to-end.
    
    Returns:
        bool: True si todo el flujo se ejecutó exitosamente.
    """
    try:
        logging.info("="*80)
        logging.info("INICIANDO FLUJO AUTOMATIZADO COMPLETO")
        logging.info("="*80)
        logging.info(f"Timestamp: {datetime.now()}")
        logging.info(f"Objetivo: Detectar {TARGET_FUNCTIONALITY} en estado {TARGET_STATUS}")
        logging.info("="*80)
        
        # PASO 1: Monitoreo
        record, link_definition = step_1_monitor_release_tracker()
        
        if not record or not link_definition:
            logging.info("No se detectó el cambio de estado. Flujo detenido.")
            return False
        
        # PASO 2: Extracción del DoD
        dod_content = step_2_extract_dod_content(link_definition)
        
        if not dod_content:
            logging.error("Fallo en extracción del DoD. Flujo detenido.")
            return False
        
        # PASO 3: Generación del One Pager
        onepager_content = step_3_generate_one_pager(dod_content)
        
        if not onepager_content:
            logging.error("Fallo en generación del One Pager. Flujo detenido.")
            return False
        
        # PASO 4: Generación del PDF
        pdf_path = step_4_generate_pdf(onepager_content)
        
        if not pdf_path:
            logging.error("Fallo en generación del PDF. Flujo detenido.")
            return False
        
        # PASO 5: Actualización en Notion
        success = step_5_update_notion()
        
        if not success:
            logging.error("Fallo en actualización de Notion. Flujo detenido.")
            return False
        
        # ÉXITO COMPLETO
        logging.info("\n" + "="*80)
        logging.info("🎉 FLUJO COMPLETO EJECUTADO EXITOSAMENTE")
        logging.info("="*80)
        logging.info("Todos los pasos completados:")
        logging.info("✅ Paso 1: Monitoreo del Release Tracker")
        logging.info("✅ Paso 2: Extracción del Definition of Done")
        logging.info("✅ Paso 3: Generación del One Pager con Gemini")
        logging.info("✅ Paso 4: Generación del PDF")
        logging.info("✅ Paso 5: Actualización en Notion")
        logging.info("="*80)
        logging.info(f"PDF generado: {pdf_path}")
        logging.info("Release Tracker y Data Normalization actualizados")
        logging.info("="*80)
        
        return True
        
    except Exception as e:
        logging.error(f"Error crítico en el flujo completo: {str(e)}")
        return False


def run_monitoring_mode():
    """
    Ejecuta el flujo en modo monitoreo continuo (polling).
    """
    logging.info("="*80)
    logging.info("INICIANDO MODO MONITOREO CONTINUO")
    logging.info("="*80)
    logging.info("Presiona Ctrl+C para detener el monitoreo")
    logging.info("="*80)
    
    check_count = 0
    
    try:
        while True:
            check_count += 1
            logging.info(f"\n--- Verificación #{check_count} - {datetime.now()} ---")
            
            # Intentar ejecutar el flujo completo
            success = run_complete_flow()
            
            if success:
                logging.info("Flujo completado exitosamente. Deteniendo monitoreo.")
                break
            else:
                # Esperar antes de la próxima verificación
                interval = int(os.getenv("POLLING_INTERVAL", 300))
                logging.info(f"Próxima verificación en {interval} segundos...")
                time.sleep(interval)
                
    except KeyboardInterrupt:
        logging.info("\n" + "="*80)
        logging.info("MONITOREO DETENIDO POR EL USUARIO")
        logging.info("="*80)
        logging.info(f"Total de verificaciones realizadas: {check_count}")
    except Exception as e:
        logging.error(f"Error en modo monitoreo: {str(e)}")


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    """Punto de entrada principal."""
    
    # Validar configuración
    required_vars = [
        "NOTION_API_KEY",
        "NOTION_RELEASE_TRACKER_DB_ID", 
        "NOTION_DATA_NORMALIZATION_PAGE_ID",
        "GEMINI_API_KEY",
        "GITHUB_USER",
        "GITHUB_REPO"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        logging.error("ERROR: Variables de entorno faltantes:")
        for var in missing_vars:
            logging.error(f"  - {var}")
        logging.error("Por favor, configura todas las variables en el archivo .env")
        exit(1)
    
    logging.info("Configuración validada correctamente")
    
    # Verificar argumentos de línea de comandos
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--monitor":
        # Modo monitoreo continuo
        run_monitoring_mode()
    else:
        # Modo ejecución única
        logging.info("Modo: Ejecución única")
        logging.info("Para modo monitoreo continuo, usa: python main.py --monitor")
        
        success = run_complete_flow()
        
        if success:
            logging.info("\nFlujo completado exitosamente!")
            exit(0)
        else:
            logging.error("\nFlujo falló. Revisar logs para más detalles.")
            exit(1)


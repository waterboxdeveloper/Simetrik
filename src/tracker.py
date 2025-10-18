"""
Sistema de monitoreo del Release Tracker en Notion.
Detecta cuando el Deployment Status de E137 cambia a "Regression".

Este script implementa polling periódico para monitorear cambios de estado
en el Release Tracker de Notion y activar el flujo de procesamiento automático.
"""

# ============================================================================
# IMPORTS
# ============================================================================

import os
import time
import logging
from datetime import datetime
from dotenv import load_dotenv
from notion_client import Client


# ============================================================================
# CONFIGURACIÓN DE LOGGING
# ============================================================================

# Crear carpeta logs/ si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el sistema de logging
logging.basicConfig(
    level=logging.INFO,  # Nivel de detalle: INFO, WARNING, ERROR
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato: timestamp - nivel - mensaje
    handlers=[
        logging.FileHandler('logs/tracker.log'),  # Guardar en archivo
        logging.StreamHandler()  # Mostrar en consola
    ]
)


# ============================================================================
# CARGAR VARIABLES DE ENTORNO Y CONFIGURACIÓN
# ============================================================================

# Cargar variables desde .env
load_dotenv()

# Inicializar cliente de Notion con API key
notion = Client(auth=os.getenv("NOTION_API_KEY"))

# Configuración del monitoreo
RELEASE_TRACKER_DB_ID = os.getenv("NOTION_RELEASE_TRACKER_DB_ID")  # ID de la database
POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", 300))  # Intervalo en segundos (default: 5 min)
TARGET_FUNCTIONALITY = "E137"  # Funcionalidad a monitorear
TARGET_STATUS = "Regression"  # Estado que dispara el flujo


# ============================================================================
# FUNCIONES
# ============================================================================

def query_release_tracker():
    """
    Consulta el Release Tracker y busca el registro de E137.
    
    Returns:
        dict: Registro de E137 si existe, None si no se encuentra.
    """
    try:
        # Log: Inicio de consulta
        logging.info(f"Consultando Release Tracker (DB ID: {RELEASE_TRACKER_DB_ID})")
        
        # Consultar la database de Notion
        results = notion.databases.query(database_id=RELEASE_TRACKER_DB_ID)
        
        # Log: Cantidad de registros encontrados
        logging.info(f"Registros encontrados: {len(results['results'])}")
        
        # Recorrer cada registro en busca de E137
        for record in results['results']:
            # Obtener las properties (columnas) del registro
            properties = record.get('properties', {})
            
            # Extraer el nombre/título del registro
            name = ""
            for prop_name, prop_data in properties.items():
                # Buscar la property de tipo 'title'
                if prop_data['type'] == 'title' and prop_data.get('title'):
                    # Notion devuelve el título como array de fragmentos de texto
                    # Ejemplo: [{'plain_text': 'E137 - '}, {'plain_text': 'Data...'}]
                    # Los unimos en un solo string
                    name = ''.join([t['plain_text'] for t in prop_data['title']])
                    break  # Ya encontramos el título, salir del loop
            
            # Verificar si este registro es E137
            if TARGET_FUNCTIONALITY in name:
                logging.info(f"Funcionalidad encontrada: {name}")
                return record  # Devolver el registro completo
        
        # Si llegamos aquí, no se encontró E137
        logging.warning(f"No se encontró la funcionalidad {TARGET_FUNCTIONALITY}")
        return None
        
    except Exception as e:
        # Capturar cualquier error y registrarlo
        logging.error(f"Error al consultar Release Tracker: {str(e)}")
        return None


def get_deployment_status(record):
    """
    Extrae el Deployment Status del registro.
    
    Args:
        record (dict): Registro de Notion.
        
    Returns:
        str: Estado actual (ej: "Regression") o None si no se encuentra.
    """
    try:
        properties = record.get('properties', {})
        
        # Buscar específicamente "Deployment Status" (con ambas palabras)
        for prop_name, prop_data in properties.items():
            # Verificar que contenga TANTO "deployment" COMO "status"
            if 'deployment' in prop_name.lower() and 'status' in prop_name.lower():
                prop_type = prop_data['type']
                
                if prop_type == 'status' and prop_data.get('status'):
                    status = prop_data['status'].get('name', '')
                    logging.info(f"Estado encontrado (tipo status): {status}")
                    return status
                    
                elif prop_type == 'select' and prop_data.get('select'):
                    status = prop_data['select'].get('name', '')
                    logging.info(f"Estado encontrado (tipo select): {status}")
                    return status
                
                elif prop_type == 'rich_text' and prop_data.get('rich_text'):
                    status = ''.join([t['plain_text'] for t in prop_data['rich_text']])
                    if status:
                        logging.info(f"Estado encontrado (tipo rich_text): {status}")
                        return status
        
        logging.warning("No se encontró la propiedad 'Deployment Status'")
        return None
        
    except Exception as e:
        logging.error(f"Error al extraer Deployment Status: {str(e)}")
        return None


def get_link_definition(record):
    """
    Extrae el Link Definition (URL del Definition of Done) del registro.
    
    Args:
        record (dict): Registro de Notion.
        
    Returns:
        str: URL del DoD o None si no se encuentra.
    """
    try:
        # Obtener las properties del registro
        properties = record.get('properties', {})
        
        # Buscar la propiedad Link Definition
        # Puede llamarse "Link Definition", "Definition Link", "DoD Link", etc.
        for prop_name, prop_data in properties.items():
            # Verificar si el nombre contiene "link" y "definition"
            if 'link' in prop_name.lower() and 'definition' in prop_name.lower():
                # Verificar que sea tipo URL
                if prop_data['type'] == 'url':
                    url = prop_data.get('url', '')
                    
                    # Verificar que la URL no esté vacía
                    if url:
                        logging.info(f"Link Definition encontrado: {url}")
                        return url
                    else:
                        logging.warning("Link Definition está vacío")
                        return None
        
        # Si llegamos aquí, no se encontró el campo
        logging.warning("No se encontró la propiedad 'Link Definition'")
        return None
        
    except Exception as e:
        # Capturar cualquier error
        logging.error(f"Error al extraer Link Definition: {str(e)}")
        return None


def monitor_release_tracker():
    """
    Monitorea el Release Tracker con polling periódico.
    Detecta cuando E137 cambia a "Regression" y activa el flujo de procesamiento.
    Se detiene con Ctrl+C.
    """
    # Banner inicial con información del monitoreo
    logging.info("="*80)
    logging.info("INICIANDO MONITOREO DEL RELEASE TRACKER")
    logging.info("="*80)
    logging.info(f"Objetivo: Detectar {TARGET_FUNCTIONALITY} en estado {TARGET_STATUS}")
    logging.info(f"Intervalo de polling: {POLLING_INTERVAL} segundos ({POLLING_INTERVAL/60} minutos)")
    logging.info("="*80)
    
    # Variables de control
    last_status = None  # Último estado conocido (para detectar cambios)
    check_count = 0     # Contador de verificaciones realizadas
    
    try:
        # Loop infinito - corre hasta que se detenga manualmente
        while True:
            check_count += 1
            
            # Log del número de verificación y timestamp
            logging.info(f"\n--- Check #{check_count} - {datetime.now()} ---")
            
            # PASO 1: Consultar el Release Tracker y buscar E137
            record = query_release_tracker()
            
            if record:
                # PASO 2: Obtener el estado actual del Deployment Status
                current_status = get_deployment_status(record)
                
                if current_status:
                    # PASO 3: Verificar si es el estado objetivo (Regression)
                    if current_status == TARGET_STATUS:
                        # ¡CAMBIO DETECTADO! Estado objetivo alcanzado
                        logging.info("="*80)
                        logging.info(f"CAMBIO DETECTADO: Estado = {TARGET_STATUS}")
                        logging.info("="*80)
                        
                        # PASO 4: Obtener el Link Definition
                        link_definition = get_link_definition(record)
                        
                        if link_definition:
                            logging.info(f"Link Definition: {link_definition}")
                            logging.info("Activando flujo de procesamiento...")
                            
                            # TODO: Aquí se activaría el flujo completo
                            # Por ahora, solo registramos el evento
                            logging.info("Evento registrado. Flujo de procesamiento pendiente de implementar.")
                            
                            # En las próximas fases, aquí llamaremos a:
                            # from main import process_full_flow
                            # process_full_flow(record, link_definition)
                            
                        else:
                            # Error: No se pudo obtener el Link Definition
                            logging.error("No se pudo obtener el Link Definition")
                        
                        # Opcional: Detener el monitoreo después de detectar el cambio
                        # break
                    
                    else:
                        # Estado actual no es Regression - seguir esperando
                        logging.info(f"Estado actual: {current_status} (esperando {TARGET_STATUS})")
                    
                    # Detectar si hubo un cambio de estado (aunque no sea Regression)
                    if last_status != current_status:
                        logging.info(f"Cambio de estado detectado: {last_status} -> {current_status}")
                    
                    # Guardar el estado actual como "último estado conocido"
                    last_status = current_status
            
            # Esperar el intervalo de polling antes de la próxima verificación
            logging.info(f"Proxima verificacion en {POLLING_INTERVAL} segundos...")
            time.sleep(POLLING_INTERVAL)
            
    except KeyboardInterrupt:
        # Usuario presionó Ctrl+C - detener gracefully
        logging.info("\n" + "="*80)
        logging.info("MONITOREO DETENIDO POR EL USUARIO")
        logging.info("="*80)
        logging.info(f"Total de verificaciones realizadas: {check_count}")
    
    except Exception as e:
        # Error crítico inesperado
        logging.error(f"Error critico en el monitoreo: {str(e)}")
        raise  # Re-lanzar la excepción para que se vea el traceback completo


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    """Punto de entrada. Valida configuración e inicia el monitoreo."""
    
    # Validación 1: Verificar que NOTION_API_KEY existe
    if not os.getenv("NOTION_API_KEY"):
        logging.error("ERROR: NOTION_API_KEY no esta configurado en .env")
        logging.error("Por favor, agrega tu API key en el archivo .env")
        exit(1)
    
    # Validación 2: Verificar que NOTION_RELEASE_TRACKER_DB_ID existe
    if not RELEASE_TRACKER_DB_ID:
        logging.error("ERROR: NOTION_RELEASE_TRACKER_DB_ID no esta configurado en .env")
        logging.error("Por favor, agrega el ID de la database del Release Tracker en .env")
        exit(1)
    
    # Validaciones OK - Iniciar monitoreo
    logging.info("Configuracion validada correctamente")
    logging.info(f"API Key: {'*' * 20}{os.getenv('NOTION_API_KEY')[-4:]}")  # Mostrar solo últimos 4 caracteres
    logging.info(f"Database ID: {RELEASE_TRACKER_DB_ID}")
    
    # Iniciar el monitoreo
    monitor_release_tracker()
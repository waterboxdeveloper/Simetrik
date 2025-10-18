"""
Script para actualizar Notion con el PDF del One Pager.
Actualiza Release Tracker y pagina Data Normalization.
"""

import os
import logging
from dotenv import load_dotenv
from notion_client import Client


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/notion_update.log'),
        logging.StreamHandler()
    ]
)


load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))

RELEASE_TRACKER_DB_ID = os.getenv("NOTION_RELEASE_TRACKER_DB_ID")
DATA_NORMALIZATION_PAGE_ID = os.getenv("NOTION_DATA_NORMALIZATION_PAGE_ID")
TARGET_FUNCTIONALITY = "E137"


def get_e137_record():
    """
    Busca y retorna el registro de E137 en el Release Tracker.
    
    Returns:
        dict: Registro de E137 o None si no se encuentra.
    """
    try:
        logging.info(f"Buscando registro {TARGET_FUNCTIONALITY}...")
        
        results = notion.databases.query(
            database_id=RELEASE_TRACKER_DB_ID,
            filter={
                "property": "Name",
                "rich_text": {
                    "contains": TARGET_FUNCTIONALITY
                }
            }
        )
        
        if results['results']:
            record = results['results'][0]
            logging.info(f"Registro encontrado: {record['id']}")
            return record
        else:
            logging.warning(f"No se encontro el registro {TARGET_FUNCTIONALITY}")
            return None
            
    except Exception as e:
        logging.error(f"Error al buscar registro E137: {str(e)}")
        return None


def update_release_tracker(record_id, pdf_url):
    """
    Actualiza la columna 'One Pager Link' en el Release Tracker.
    
    Args:
        record_id (str): ID del registro de E137.
        pdf_url (str): URL publica del PDF.
        
    Returns:
        bool: True si la actualizacion fue exitosa.
    """
    try:
        logging.info(f"Actualizando Release Tracker con URL del PDF...")
        
        notion.pages.update(
            page_id=record_id,
            properties={
                "📄 One Pager Link": {
                    "url": pdf_url
                }
            }
        )
        
        logging.info("Release Tracker actualizado exitosamente")
        return True
        
    except Exception as e:
        logging.error(f"Error al actualizar Release Tracker: {str(e)}")
        return False


def append_pdf_to_page(page_id, pdf_url, pdf_name="E137_OnePager.pdf"):
    """
    Agrega un bloque de archivo con el PDF a una pagina de Notion.
    
    Args:
        page_id (str): ID de la pagina de Notion.
        pdf_url (str): URL publica del PDF.
        pdf_name (str): Nombre del archivo para mostrar.
        
    Returns:
        bool: True si se agrego exitosamente.
    """
    try:
        logging.info(f"Agregando PDF a pagina {page_id}...")
        
        notion.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": "📄 One Pager Generado"}
                        }]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {
                                "content": "One Pager educativo generado automaticamente con Gemini API:"
                            }
                        }]
                    }
                },
                {
                    "object": "block",
                    "type": "file",
                    "file": {
                        "type": "external",
                        "external": {
                            "url": pdf_url
                        },
                        "caption": [{
                            "type": "text",
                            "text": {"content": pdf_name}
                        }]
                    }
                }
            ]
        )
        
        logging.info("PDF agregado exitosamente a la pagina")
        return True
        
    except Exception as e:
        logging.error(f"Error al agregar PDF a pagina: {str(e)}")
        return False


def update_notion_with_pdf(pdf_url):
    """
    Actualiza tanto el Release Tracker como la pagina Data Normalization.
    
    Args:
        pdf_url (str): URL publica del PDF.
        
    Returns:
        bool: True si ambas actualizaciones fueron exitosas.
    """
    try:
        logging.info("="*80)
        logging.info("ACTUALIZANDO NOTION CON PDF")
        logging.info("="*80)
        
        record = get_e137_record()
        if not record:
            logging.error("No se pudo obtener el registro E137")
            return False
        
        record_id = record['id']
        
        success_tracker = update_release_tracker(record_id, pdf_url)
        
        success_page = append_pdf_to_page(DATA_NORMALIZATION_PAGE_ID, pdf_url)
        
        if success_tracker and success_page:
            logging.info("\n" + "="*80)
            logging.info("ACTUALIZACION COMPLETA EXITOSA")
            logging.info("="*80)
            logging.info(f"Release Tracker actualizado: SI")
            logging.info(f"Pagina Data Normalization actualizada: SI")
            logging.info("="*80)
            return True
        else:
            logging.warning("Actualizacion parcial. Revisar logs.")
            return False
            
    except Exception as e:
        logging.error(f"Error en actualizacion de Notion: {str(e)}")
        return False


if __name__ == "__main__":
    """Actualiza Notion con la URL del PDF."""
    
    os.makedirs("logs", exist_ok=True)
    
    if not os.getenv("NOTION_API_KEY"):
        logging.error("ERROR: NOTION_API_KEY no configurado en .env")
        exit(1)
    
    if not RELEASE_TRACKER_DB_ID:
        logging.error("ERROR: NOTION_RELEASE_TRACKER_DB_ID no configurado en .env")
        exit(1)
    
    if not DATA_NORMALIZATION_PAGE_ID:
        logging.error("ERROR: NOTION_DATA_NORMALIZATION_PAGE_ID no configurado en .env")
        exit(1)
    
    # Obtener URL de GitHub desde variables de entorno
    github_user = os.getenv("GITHUB_USER", "tu-usuario")
    github_repo = os.getenv("GITHUB_REPO", "Prueba")
    github_branch = os.getenv("GITHUB_BRANCH", "main")
    pdf_path = "src/output/E137_OnePager.pdf"
    
    pdf_url = f"https://raw.githubusercontent.com/{github_user}/{github_repo}/{github_branch}/{pdf_path}"
    
    logging.info("Actualizando Notion con URL del PDF...")
    logging.info(f"URL: {pdf_url}")
    
    success = update_notion_with_pdf(pdf_url)
    
    if success:
        logging.info("\nActualizacion completada exitosamente")
    else:
        logging.error("\nActualizacion fallida. Revisar logs.")
        exit(1)
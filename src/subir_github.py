"""
Script para generar URL publica del PDF usando GitHub.
Asume que el PDF ya esta en el repositorio.
"""

import os
import logging
from dotenv import load_dotenv


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/github_url.log'),
        logging.StreamHandler()
    ]
)


load_dotenv()

GITHUB_USER = os.getenv('GITHUB_USER', 'tu-usuario')
GITHUB_REPO = os.getenv('GITHUB_REPO', 'Prueba')
GITHUB_BRANCH = os.getenv('GITHUB_BRANCH', 'main')


def generate_github_url(pdf_path="src/output/E137_OnePager.pdf"):
    """
    Genera la URL publica del PDF en GitHub.
    
    Args:
        pdf_path (str): Ruta del PDF en el repositorio.
        
    Returns:
        str: URL publica del archivo en GitHub.
    """
    try:
        logging.info("Generando URL de GitHub para el PDF...")
        
        # URL para acceso directo (raw)
        github_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{pdf_path}"
        
        logging.info(f"URL generada: {github_url}")
        return github_url
        
    except Exception as e:
        logging.error(f"Error al generar URL de GitHub: {str(e)}")
        raise


def verify_pdf_exists(pdf_path="src/output/E137_OnePager.pdf"):
    """
    Verifica que el PDF existe localmente.
    
    Args:
        pdf_path (str): Ruta local del PDF.
        
    Returns:
        bool: True si el archivo existe.
    """
    # Ajustar ruta segun donde se ejecute el script
    if not os.path.exists(pdf_path):
        pdf_path = pdf_path.replace("src/", "", 1)
    
    if os.path.exists(pdf_path):
        logging.info(f"PDF encontrado: {pdf_path}")
        file_size = os.path.getsize(pdf_path)
        logging.info(f"Tamano del archivo: {file_size / 1024:.2f} KB")
        return True
    else:
        logging.error(f"PDF no encontrado: {pdf_path}")
        return False


if __name__ == "__main__":
    """Genera la URL del PDF en GitHub."""
    
    os.makedirs("logs", exist_ok=True)
    
    logging.info("="*80)
    logging.info("GENERACION DE URL DE GITHUB")
    logging.info("="*80)
    
    pdf_path = "src/output/E137_OnePager.pdf"
    
    if verify_pdf_exists(pdf_path):
        url = generate_github_url(pdf_path)
        
        logging.info("\n" + "="*80)
        logging.info("URL GENERADA EXITOSAMENTE")
        logging.info("="*80)
        logging.info(f"URL publica: {url}")
        logging.info("="*80)
        logging.info("\nPROXIMOS PASOS:")
        logging.info("1. Commit y push del PDF al repositorio:")
        logging.info("   git add src/output/E137_OnePager.pdf")
        logging.info("   git commit -m 'Add generated One Pager PDF'")
        logging.info("   git push origin main")
        logging.info("2. Actualizar Notion con esta URL")
        logging.info("="*80)
    else:
        logging.error("No se pudo generar la URL. PDF no encontrado.")
        exit(1)


"""
Extractor del Definition of Done desde Notion.
Lee todos los bloques y estructura el contenido en formato Markdown.
"""

import os
import logging
import requests
from dotenv import load_dotenv
from notion_client import Client


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/dod_extraction.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))

DOD_PAGE_ID = os.getenv("NOTION_DOD_PAGE_ID")


def extract_rich_text(rich_text_array):
    """
    Extrae texto plano de un array de rich_text de Notion.
    
    Args:
        rich_text_array (list): Array de objetos rich_text de Notion.
        
    Returns:
        str: Texto plano concatenado.
    """
    if not rich_text_array:
        return ""
    return ''.join([text['plain_text'] for text in rich_text_array])


def download_image(image_url, output_dir="output/images/", filename=None):
    """
    Descarga una imagen desde una URL y la guarda localmente.
    
    Args:
        image_url (str): URL de la imagen a descargar.
        output_dir (str): Directorio donde guardar la imagen.
        filename (str): Nombre del archivo (opcional, se genera automáticamente).
        
    Returns:
        str: Ruta local de la imagen descargada o None si falla.
    """
    try:
        # Crear directorio si no existe
        os.makedirs(output_dir, exist_ok=True)
        
        # Generar nombre de archivo si no se proporciona
        if not filename:
            # Usar timestamp para nombres únicos
            import time
            timestamp = int(time.time())
            extension = image_url.split('.')[-1].split('?')[0]  # Extraer extensión
            if extension not in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
                extension = 'png'  # Default
            filename = f"dod_image_{timestamp}.{extension}"
        
        # Ruta completa del archivo
        filepath = os.path.join(output_dir, filename)
        
        # Descargar imagen
        logging.info(f"Descargando imagen: {filename}")
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        # Guardar imagen
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        logging.info(f"Imagen guardada en: {filepath}")
        return filepath
        
    except Exception as e:
        logging.error(f"Error al descargar imagen: {str(e)}")
        return None


def extract_table_content(table_block_id):
    """
    Extrae el contenido de una tabla de Notion.
    
    Args:
        table_block_id (str): ID del bloque de tabla.
        
    Returns:
        str: Contenido de la tabla en formato Markdown.
    """
    try:
        # Obtener las filas de la tabla (son bloques hijos)
        table_rows = notion.blocks.children.list(block_id=table_block_id)
        
        markdown_table = []
        
        for row_index, row_block in enumerate(table_rows['results']):
            if row_block['type'] == 'table_row':
                cells = row_block['table_row']['cells']
                
                # Extraer texto de cada celda
                row_content = []
                for cell in cells:
                    cell_text = extract_rich_text(cell)
                    row_content.append(cell_text)
                
                # Formatear como fila de Markdown
                markdown_table.append("| " + " | ".join(row_content) + " |")
                
                # Agregar separador después de la primera fila (header)
                if row_index == 0:
                    separator = "| " + " | ".join(["---"] * len(row_content)) + " |"
                    markdown_table.append(separator)
        
        return "\n".join(markdown_table)
        
    except Exception as e:
        logging.error(f"Error al extraer tabla: {str(e)}")
        return "[Error al extraer tabla]"


def extract_block_content(block, indent_level=0):
    """
    Extrae el contenido de un bloque de Notion y lo convierte a Markdown.
    
    Args:
        block (dict): Bloque de Notion.
        indent_level (int): Nivel de indentación para bloques anidados.
        
    Returns:
        str: Contenido del bloque en formato Markdown.
    """
    block_type = block['type']
    content = ""
    indent = "  " * indent_level
    
    try:
        if block_type == 'paragraph':
            text = extract_rich_text(block['paragraph'].get('rich_text', []))
            if text:
                content = f"{indent}{text}\n\n"
        
        elif block_type == 'heading_1':
            text = extract_rich_text(block['heading_1'].get('rich_text', []))
            content = f"{indent}# {text}\n\n"
        
        elif block_type == 'heading_2':
            text = extract_rich_text(block['heading_2'].get('rich_text', []))
            content = f"{indent}## {text}\n\n"
        
        elif block_type == 'heading_3':
            text = extract_rich_text(block['heading_3'].get('rich_text', []))
            content = f"{indent}### {text}\n\n"
        
        elif block_type == 'bulleted_list_item':
            text = extract_rich_text(block['bulleted_list_item'].get('rich_text', []))
            content = f"{indent}- {text}\n"
        
        elif block_type == 'numbered_list_item':
            text = extract_rich_text(block['numbered_list_item'].get('rich_text', []))
            content = f"{indent}1. {text}\n"
        
        elif block_type == 'quote':
            text = extract_rich_text(block['quote'].get('rich_text', []))
            content = f"{indent}> {text}\n\n"
        
        elif block_type == 'code':
            text = extract_rich_text(block['code'].get('rich_text', []))
            language = block['code'].get('language', '')
            content = f"{indent}```{language}\n{text}\n```\n\n"
        
        elif block_type == 'divider':
            content = f"{indent}---\n\n"
        
        elif block_type == 'table':
            table_content = extract_table_content(block['id'])
            content = f"{indent}{table_content}\n\n"
        
        elif block_type == 'image':
            # Intentar obtener URL de la imagen
            image_data = block['image']
            if image_data['type'] == 'external':
                image_url = image_data['external']['url']
            elif image_data['type'] == 'file':
                image_url = image_data['file']['url']
            else:
                image_url = ''
            
            caption = extract_rich_text(image_data.get('caption', []))
            
            # Descargar imagen localmente
            if image_url:
                local_path = download_image(image_url)
                if local_path:
                    content = f"{indent}![{caption}]({local_path})\n\n"
                else:
                    # Si falla la descarga, usar descripción solamente
                    content = f"{indent}[Imagen: {caption if caption else 'sin descripción'}]\n\n"
            else:
                content = f"{indent}[Imagen sin URL disponible]\n\n"
        
        elif block_type == 'file':
            file_data = block['file']
            file_name = file_data.get('name', 'archivo')
            
            if file_data['type'] == 'external':
                file_url = file_data['external']['url']
            elif file_data['type'] == 'file':
                file_url = file_data['file']['url']
            else:
                file_url = ''
            
            content = f"{indent}[📎 {file_name}]({file_url})\n\n"
        
        elif block_type == 'pdf':
            pdf_data = block['pdf']
            
            if pdf_data['type'] == 'external':
                pdf_url = pdf_data['external']['url']
            elif pdf_data['type'] == 'file':
                pdf_url = pdf_data['file']['url']
            else:
                pdf_url = ''
            
            content = f"{indent}[📄 PDF]({pdf_url})\n\n"
        
        # Procesar bloques hijos si existen
        if block.get('has_children', False):
            try:
                children = notion.blocks.children.list(block_id=block['id'])
                for child in children['results']:
                    content += extract_block_content(child, indent_level + 1)
            except Exception as e:
                logging.warning(f"Error al leer bloques hijos de {block_type}: {str(e)}")
        
    except Exception as e:
        logging.error(f"Error al procesar bloque tipo {block_type}: {str(e)}")
        content = f"{indent}[Error al extraer contenido de tipo {block_type}]\n\n"
    
    return content


def extract_dod_content(page_id):
    """
    Extrae todo el contenido del Definition of Done.
    
    Args:
        page_id (str): ID de la página del DoD.
        
    Returns:
        str: Contenido completo en formato Markdown.
    """
    try:
        logging.info("="*80)
        logging.info("EXTRAYENDO DEFINITION OF DONE")
        logging.info("="*80)
        
        # Obtener información de la página
        page = notion.pages.retrieve(page_id=page_id)
        
        # Extraer título
        title = "Definition of Done"
        if 'properties' in page:
            for prop_name, prop_data in page['properties'].items():
                if prop_data['type'] == 'title' and prop_data.get('title'):
                    title = extract_rich_text(prop_data['title'])
                    break
        
        logging.info(f"Titulo: {title}")
        
        # Iniciar con el título en Markdown
        markdown_content = f"# {title}\n\n"
        
        # Obtener todos los bloques de la página
        blocks = notion.blocks.children.list(block_id=page_id)
        
        logging.info(f"Total de bloques a procesar: {len(blocks['results'])}")
        
        # Procesar cada bloque
        for i, block in enumerate(blocks['results'], 1):
            block_type = block['type']
            logging.info(f"Procesando bloque {i}/{len(blocks['results'])}: {block_type}")
            
            block_content = extract_block_content(block)
            markdown_content += block_content
        
        logging.info("Extraccion completada exitosamente")
        logging.info("="*80)
        
        return markdown_content
        
    except Exception as e:
        logging.error(f"Error al extraer DoD: {str(e)}")
        raise


def save_dod_to_file(content, output_path="output/dod_content.md"):
    """
    Guarda el contenido extraído en un archivo.
    
    Args:
        content (str): Contenido a guardar.
        output_path (str): Ruta del archivo de salida.
    """
    try:
        # Crear directorio output si no existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logging.info(f"Contenido guardado en: {output_path}")
        logging.info(f"Tamano del contenido: {len(content)} caracteres")
        
    except Exception as e:
        logging.error(f"Error al guardar archivo: {str(e)}")
        raise


if __name__ == "__main__":
    """Extrae y guarda el contenido del Definition of Done."""
    
    # Validaciones
    if not os.getenv("NOTION_API_KEY"):
        logging.error("ERROR: NOTION_API_KEY no configurado en .env")
        exit(1)
    
    if not DOD_PAGE_ID:
        logging.error("ERROR: NOTION_DOD_PAGE_ID no configurado en .env")
        exit(1)
    
    # Crear carpeta logs si no existe
    os.makedirs("logs", exist_ok=True)
    
    # Extraer contenido
    dod_content = extract_dod_content(DOD_PAGE_ID)
    
    # Guardar en archivo
    save_dod_to_file(dod_content)
    
    # Mostrar preview
    logging.info("\n" + "="*80)
    logging.info("PREVIEW DEL CONTENIDO EXTRAIDO")
    logging.info("="*80)
    preview_lines = dod_content.split('\n')[:20]
    for line in preview_lines:
        print(line)
    
    if len(dod_content.split('\n')) > 20:
        print("\n... (ver archivo completo en output/dod_content.md)")
    
    logging.info("="*80)


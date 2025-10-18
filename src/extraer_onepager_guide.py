"""
Extractor del One Pager Guide desde Notion.
Lee todos los bloques y extrae especialmente el prompt sugerido.
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
        logging.FileHandler('logs/onepager_extraction.log'),
        logging.StreamHandler()
    ]
)

load_dotenv()
notion = Client(auth=os.getenv("NOTION_API_KEY"))

ONEPAGER_GUIDE_ID = os.getenv("NOTION_ONEPAGER_GUIDE_ID")


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


def extract_table_content(table_block_id):
    """
    Extrae el contenido de una tabla de Notion.
    
    Args:
        table_block_id (str): ID del bloque de tabla.
        
    Returns:
        str: Contenido de la tabla en formato Markdown.
    """
    try:
        table_rows = notion.blocks.children.list(block_id=table_block_id)
        
        markdown_table = []
        
        for row_index, row_block in enumerate(table_rows['results']):
            if row_block['type'] == 'table_row':
                cells = row_block['table_row']['cells']
                
                row_content = []
                for cell in cells:
                    cell_text = extract_rich_text(cell)
                    row_content.append(cell_text)
                
                markdown_table.append("| " + " | ".join(row_content) + " |")
                
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
        
        elif block_type == 'callout':
            text = extract_rich_text(block['callout'].get('rich_text', []))
            content = f"{indent}💡 {text}\n\n"
        
        elif block_type == 'code':
            text = extract_rich_text(block['code'].get('rich_text', []))
            language = block['code'].get('language', '')
            content = f"{indent}```{language}\n{text}\n```\n\n"
        
        elif block_type == 'divider':
            content = f"{indent}---\n\n"
        
        elif block_type == 'table':
            table_content = extract_table_content(block['id'])
            content = f"{indent}{table_content}\n\n"
        
        elif block_type == 'file':
            file_data = block['file']
            file_name = file_data.get('name', 'archivo')
            content = f"{indent}[📎 Archivo: {file_name}]\n\n"
        
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


def extract_onepager_guide(page_id):
    """
    Extrae todo el contenido del One Pager Guide.
    
    Args:
        page_id (str): ID de la página del One Pager Guide.
        
    Returns:
        str: Contenido completo en formato Markdown.
    """
    try:
        logging.info("="*80)
        logging.info("EXTRAYENDO ONE PAGER GUIDE")
        logging.info("="*80)
        
        page = notion.pages.retrieve(page_id=page_id)
        
        title = "One Pager Guide"
        if 'properties' in page:
            for prop_name, prop_data in page['properties'].items():
                if prop_data['type'] == 'title' and prop_data.get('title'):
                    title = extract_rich_text(prop_data['title'])
                    break
        
        logging.info(f"Titulo: {title}")
        
        markdown_content = f"# {title}\n\n"
        
        blocks = notion.blocks.children.list(block_id=page_id)
        
        logging.info(f"Total de bloques a procesar: {len(blocks['results'])}")
        
        for i, block in enumerate(blocks['results'], 1):
            block_type = block['type']
            logging.info(f"Procesando bloque {i}/{len(blocks['results'])}: {block_type}")
            
            block_content = extract_block_content(block)
            markdown_content += block_content
        
        logging.info("Extraccion completada exitosamente")
        logging.info("="*80)
        
        return markdown_content
        
    except Exception as e:
        logging.error(f"Error al extraer One Pager Guide: {str(e)}")
        raise


def save_to_file(content, output_path="output/onepager_guide.md"):
    """
    Guarda el contenido extraído en un archivo.
    
    Args:
        content (str): Contenido a guardar.
        output_path (str): Ruta del archivo de salida.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logging.info(f"Contenido guardado en: {output_path}")
        logging.info(f"Tamano del contenido: {len(content)} caracteres")
        
    except Exception as e:
        logging.error(f"Error al guardar archivo: {str(e)}")
        raise


if __name__ == "__main__":
    """Extrae y guarda el contenido del One Pager Guide."""
    
    if not os.getenv("NOTION_API_KEY"):
        logging.error("ERROR: NOTION_API_KEY no configurado en .env")
        exit(1)
    
    if not ONEPAGER_GUIDE_ID:
        logging.error("ERROR: NOTION_ONEPAGER_GUIDE_ID no configurado en .env")
        exit(1)
    
    os.makedirs("logs", exist_ok=True)
    
    guide_content = extract_onepager_guide(ONEPAGER_GUIDE_ID)
    
    save_to_file(guide_content)
    
    logging.info("\n" + "="*80)
    logging.info("PREVIEW DEL CONTENIDO EXTRAIDO")
    logging.info("="*80)
    preview_lines = guide_content.split('\n')[:30]
    for line in preview_lines:
        print(line)
    
    if len(guide_content.split('\n')) > 30:
        print("\n... (ver archivo completo en output/onepager_guide.md)")
    
    logging.info("="*80)


"""
Generador de PDF del One Pager usando ReportLab.
Convierte Markdown a PDF profesional con imágenes integradas.
"""

import os
import logging
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/pdf_generation.log'),
        logging.StreamHandler()
    ]
)


def read_markdown(file_path):
    """
    Lee el contenido del archivo Markdown.
    
    Args:
        file_path (str): Ruta del archivo Markdown.
        
    Returns:
        str: Contenido del archivo.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        logging.info(f"Archivo Markdown leido: {file_path}")
        logging.info(f"Tamano del contenido: {len(content)} caracteres")
        
        return content
        
    except Exception as e:
        logging.error(f"Error al leer archivo Markdown: {str(e)}")
        raise


def create_styles():
    """
    Crea estilos personalizados para el PDF.
    
    Returns:
        dict: Diccionario con estilos personalizados.
    """
    styles = getSampleStyleSheet()
    
    # Estilos personalizados
    custom_styles = {
        'CustomTitle': ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            fontSize=24,
            spaceAfter=12,
            alignment=TA_CENTER,
            textColor=HexColor('#2E86AB')
        ),
        'CustomSubtitle': ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            alignment=TA_CENTER,
            textColor=HexColor('#A23B72')
        ),
        'CustomHeading': ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=8,
            spaceBefore=12,
            textColor=HexColor('#2E86AB')
        ),
        'CustomBullet': ParagraphStyle(
            'CustomBullet',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            leftIndent=20,
            bulletIndent=10
        ),
        'CustomNormal': ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=8,
            alignment=TA_LEFT
        )
    }
    
    logging.info("Estilos personalizados creados")
    return custom_styles


def convert_bold_formatting(text):
    """
    Convierte **texto** a <b>texto</b> de forma segura.
    
    Args:
        text (str): Texto con formato **bold**.
        
    Returns:
        str: Texto con formato HTML <b>bold</b>.
    """
    import re
    
    # Usar regex para encontrar **texto** y reemplazarlo correctamente
    def replace_bold(match):
        content = match.group(1)
        return f"<b>{content}</b>"
    
    # Patrón para encontrar **texto** (no anidado)
    pattern = r'\*\*(.*?)\*\*'
    result = re.sub(pattern, replace_bold, text)
    
    return result


def parse_markdown_to_elements(markdown_content, styles):
    """
    Parsea el contenido Markdown y lo convierte a elementos de ReportLab.
    
    Args:
        markdown_content (str): Contenido Markdown.
        styles (dict): Estilos personalizados.
        
    Returns:
        list: Lista de elementos para el PDF.
    """
    elements = []
    lines = markdown_content.split('\n')
    
    image_count = 0
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
            
        # Headings (###)
        if line.startswith('### '):
            title = line[4:].strip()
            elements.append(Paragraph(title, styles['CustomHeading']))
            
            # Insertar imagen después de sección 6
            if "6" in title and "En qué consiste" in title:
                image_count += 1
                image_path = f"output/images/dod_image_1760820189.png"
                if os.path.exists(image_path):
                    elements.append(Spacer(1, 0.3*cm))
                    elements.append(Image(image_path, width=15*cm, height=10*cm))
                    elements.append(Spacer(1, 0.3*cm))
                    logging.info(f"Imagen {image_count} insertada después de sección 6")
            
            # Insertar imagen en sección 8
            elif "8" in title and "Cómo se usa" in title:
                image_count += 1
                image_path = f"output/images/dod_image_1760820190.png"
                if os.path.exists(image_path):
                    elements.append(Spacer(1, 0.3*cm))
                    elements.append(Image(image_path, width=15*cm, height=10*cm))
                    elements.append(Spacer(1, 0.3*cm))
                    logging.info(f"Imagen {image_count} insertada en sección 8")
        
        # Bullet points
        elif line.startswith('* ') or line.startswith('- '):
            text = line[2:].strip()
            # Convertir **texto** a <b>texto</b> correctamente
            text = convert_bold_formatting(text)
            elements.append(Paragraph(f"• {text}", styles['CustomBullet']))
        
        # Lista numerada
        elif line[0].isdigit() and '. ' in line:
            text = line.split('. ', 1)[1].strip()
            text = convert_bold_formatting(text)
            elements.append(Paragraph(f"• {text}", styles['CustomBullet']))
        
        # Párrafos normales
        else:
            if line:
                text = convert_bold_formatting(line)
                elements.append(Paragraph(text, styles['CustomNormal']))
    
    logging.info(f"{len(elements)} elementos creados para el PDF")
    return elements


def generate_pdf(markdown_content, output_path="output/E137_OnePager.pdf"):
    """
    Genera el PDF desde el contenido Markdown.
    
    Args:
        markdown_content (str): Contenido Markdown.
        output_path (str): Ruta del archivo PDF de salida.
        
    Returns:
        str: Ruta del archivo PDF generado.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        logging.info("Generando PDF con ReportLab...")
        
        # Crear documento
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        
        # Crear estilos
        styles = create_styles()
        
        # Construir elementos
        elements = []
        
        # Header
        elements.append(Paragraph("One Pager", styles['CustomTitle']))
        elements.append(Paragraph("E137 - Data Normalization in Unions", styles['CustomSubtitle']))
        elements.append(Spacer(1, 0.5*cm))
        
        # Contenido
        content_elements = parse_markdown_to_elements(markdown_content, styles)
        elements.extend(content_elements)
        
        # Footer
        elements.append(Spacer(1, 1*cm))
        elements.append(Paragraph(
            "<i>Simetrik - Plataforma de Conciliación Financiera</i>",
            styles['CustomSubtitle']
        ))
        
        # Generar PDF
        doc.build(elements)
        
        logging.info(f"PDF generado exitosamente: {output_path}")
        
        # Verificar tamaño del archivo
        file_size = os.path.getsize(output_path)
        logging.info(f"Tamano del PDF: {file_size / 1024:.2f} KB")
        
        return output_path
        
    except Exception as e:
        logging.error(f"Error al generar PDF: {str(e)}")
        raise


if __name__ == "__main__":
    """Genera el PDF del One Pager con imágenes."""
    
    try:
        logging.info("="*80)
        logging.info("GENERACION DE PDF DEL ONE PAGER")
        logging.info("="*80)
        
        os.makedirs("logs", exist_ok=True)
        
        # Paso 1: Leer Markdown
        markdown_content = read_markdown("output/onepager_generado.md")
        
        # Paso 2: Generar PDF con imágenes integradas
        generate_pdf(markdown_content)
        
        logging.info("\n" + "="*80)
        logging.info("PDF GENERADO EXITOSAMENTE")
        logging.info("="*80)
        logging.info("Archivo: output/E137_OnePager.pdf")
        logging.info("Contenido:")
        logging.info("  - Texto del One Pager generado por Gemini")
        logging.info("  - 2 imagenes del Definition of Done")
        logging.info("  - Formato profesional con ReportLab")
        logging.info("="*80)
        
    except Exception as e:
        logging.error(f"Error en el proceso: {str(e)}")
        exit(1)

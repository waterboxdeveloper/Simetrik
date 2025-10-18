"""
Generador de PDF del One Pager con imágenes.
Convierte el Markdown generado por Gemini a PDF con formato profesional usando ReportLab.
"""

import os
import logging
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
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
        
        # Limpiar bloques de código si existen
        if content.startswith('```markdown'):
            content = content.replace('```markdown', '').replace('```', '')
        
        logging.info(f"Markdown leido: {file_path} ({len(content)} caracteres)")
        return content.strip()
    except Exception as e:
        logging.error(f"Error al leer {file_path}: {str(e)}")
        raise


def create_styles():
    """
    Crea estilos personalizados para el PDF.
    
    Returns:
        dict: Diccionario de estilos.
    """
    styles = getSampleStyleSheet()
    
    # Estilo para título principal
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#3498db'),
        spaceAfter=30,
        alignment=TA_LEFT
    ))
    
    # Estilo para subtítulo
    styles.add(ParagraphStyle(
        name='CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#7f8c8d'),
        spaceAfter=20,
        alignment=TA_LEFT
    ))
    
    # Estilo para secciones
    styles.add(ParagraphStyle(
        name='SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#2c3e50'),
        spaceBefore=15,
        spaceAfter=10,
        leftIndent=0
    ))
    
    # Estilo para texto normal
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=16
    ))
    
    # Estilo para bullets
    styles.add(ParagraphStyle(
        name='CustomBullet',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=8,
        leading=14
    ))
    
    logging.info("Estilos personalizados creados")
    return styles


def parse_markdown_to_elements(markdown_content, styles):
    """
    Parsea el contenido Markdown y lo convierte en elementos de ReportLab.
    
    Args:
        markdown_content (str): Contenido en formato Markdown.
        styles: Estilos de ReportLab.
        
    Returns:
        list: Lista de elementos para el PDF.
    """
    elements = []
    lines = markdown_content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Saltar líneas vacías
        if not line:
            i += 1
            continue
        
        # Detectar secciones (### título)
        if line.startswith('###'):
            title_text = line.replace('###', '').strip()
            elements.append(Paragraph(title_text, styles['SectionHeading']))
            elements.append(Spacer(1, 0.2*cm))
            
            # Insertar imágenes después de secciones específicas
            if '6.' in title_text and 'consiste' in title_text.lower():
                # Imagen después de sección 6
                try:
                    img = Image('output/images/dod_image_1760814201.png', width=15*cm, height=10*cm)
                    elements.append(Spacer(1, 0.3*cm))
                    elements.append(img)
                    elements.append(Spacer(1, 0.3*cm))
                    logging.info("Imagen 1 insertada después de sección 6")
                except:
                    logging.warning("No se pudo cargar imagen 1")
            
            elif '8.' in title_text:
                # Imagen en sección 8
                try:
                    img = Image('output/images/dod_image_1760814203.png', width=15*cm, height=10*cm)
                    elements.append(Spacer(1, 0.3*cm))
                    elements.append(img)
                    elements.append(Spacer(1, 0.3*cm))
                    logging.info("Imagen 2 insertada en sección 8")
                except:
                    logging.warning("No se pudo cargar imagen 2")
        
        # Detectar bullets con * o -
        elif line.startswith('*') or line.startswith('-'):
            bullet_text = line[1:].strip()
            # Convertir **texto** a <b>texto</b> para negrita
            bullet_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', bullet_text)
            elements.append(Paragraph(f"• {bullet_text}", styles['CustomBullet']))
        
        # Detectar listas numeradas
        elif re.match(r'^\d+\.', line):
            number_text = re.sub(r'^\d+\.\s*', '', line)
            # Convertir **texto** a <b>texto</b>
            number_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', number_text)
            elements.append(Paragraph(number_text, styles['CustomBullet']))
        
        # Texto normal (párrafos)
        else:
            # Convertir **texto** a <b>texto</b>
            paragraph_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            elements.append(Paragraph(paragraph_text, styles['CustomBody']))
        
        i += 1
    
    logging.info(f"{len(elements)} elementos creados para el PDF")
    return elements


def generate_pdf(markdown_content, output_path="output/E137_OnePager.pdf"):
    """
    Genera el PDF desde el contenido Markdown.
    
    Args:
        markdown_content (str): Contenido Markdown.
        output_path (str): Ruta del archivo PDF de salida.
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


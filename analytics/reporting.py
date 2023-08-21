from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(data):
    """
    Generate a report based on the processed data.
    """
    # Implementation to generate a report using the reportlab library
    doc = SimpleDocTemplate("data_report.pdf", pagesize=landscape(letter))
    elements = []

    # Create a table for data summary
    table_data = [["Data Summary"]]
    table_data.extend([["Data Column", "Mean", "Std Deviation"],
                       ["Column 1", "123.45", "23.67"],
                       ["Column 2", "67.89", "15.43"],
                       ["Column 3", "234.56", "45.21"]])

    table = Table(table_data, colWidths=100, rowHeights=30)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # Add paragraphs
    styles = getSampleStyleSheet()
    p = Paragraph("This report provides a summary of the processed data.", styles["Normal"])
    elements.append(p)

    doc.build(elements)
    return "data_report.pdf"



def create_pdf(Number, date, products):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, Flowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.utils import ImageReader
    from reportlab.lib.colors import HexColor
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    # Register a custom font
    font_path = "billy_argel_font_regular/Billy Argel Font___.ttf"  # Update with the path to your font file
    pdfmetrics.registerFont(TTFont('CustomFont', font_path))

    # Set up document
    pdf_path = "nota_de_encomenda.pdf"
    document = SimpleDocTemplate(pdf_path, pagesize=A4)
    elements = []


    # Set up document
    pdf_path = "nota_de_encomenda_with_image_header.pdf"
    document = SimpleDocTemplate(pdf_path, pagesize=A4)
    elements = []

    # Load basic styles and add custom styles
    styles = getSampleStyleSheet()

    # Custom title style
    title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.black,
    spaceAfter=10,
    fontName="Helvetica-Bold"
    )
    image_text_style = ParagraphStyle(
    'ImageTextStyle',
    parent=styles['Normal'],
    fontSize=10,
    textColor=HexColor("#333333"),
    spaceAfter=8,
    )

    # Custom subheader and bold styles
    subheader_style = ParagraphStyle(
    'SubHeaderStyle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=HexColor("#333333"),
    spaceAfter=8,
    )
    bold_style = ParagraphStyle(
    'BoldStyle',
    parent=styles['Normal'],
    fontSize=15,
    textColor=HexColor("#333333"),
    spaceAfter=6,
    fontName="Helvetica-Bold"
    )
    centered_bold_style = ParagraphStyle(
    'BoldStyle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=HexColor("#333333"),
    spaceAfter=6,
    fontName="Helvetica-Bold",
    alignment=1
    )
    # Custom subheader and bold styles
    text_style = ParagraphStyle(
    'SubHeaderStyle',
    parent=styles['Normal'],
    fontSize=15,
    textColor=HexColor("#333333"),
    spaceAfter=8,
    )


    centered_text_style = ParagraphStyle(
    'SubHeaderStyle',
    parent=styles['Normal'],
    fontSize=15,
    textColor=HexColor("#333333"),
    spaceAfter=8,
    alignment= 1,
    )

    # Title with text
    title = Paragraph("SciTeCh'24", title_style)
    elements.append(title)



    # Define custom Flowable to combine image and paragraph in a line
    from reportlab.lib.utils import ImageReader
    from reportlab.platypus import Flowable, Paragraph

    class ImageParagraph(Flowable):
        def __init__(self, img_path, text, style):
            Flowable.__init__(self)

            # Load the image using ImageReader
            self.img = ImageReader(img_path)

            # Set up the Paragraph for the text
            self.text = Paragraph(text, style)

            # Immediately get image dimensions
            self.img_width, self.img_height = self.img.getSize()

            self.img_width = self.img_width * 0.07
            self.img_height = self.img_height * 0.07

        def wrap(self, availWidth, availHeight):
            # Wrap the text to get its dimensions
            text_width, text_height = self.text.wrap(availWidth, availHeight)

            # Calculate total width and maximum height
            width = self.img_width + 5 + text_width  # 5 is the space between image and text
            height = max(self.img_height, text_height)  # Maximum height to accommodate both

            return width, height

        def draw(self):
            # Draw the image at the bottom left corner (0,0)
            # Using drawImage from the canvas
            self.canv.drawImage(self.img, 0, 0, width=self.img_width, height=self.img_height)

            # Calculate the position for the text
            text_x = self.img_width + 5  # Space between image and text

            # Center the text vertically with respect to the image
            text_y = (self.img_height - self.text.height) / 2  # Center vertically

            # Draw the text at the calculated position
            self.text.drawOn(self.canv, text_x, text_y)



    # Subheader Information
    subheader1 = Paragraph("Rua Dr. Roberto Frias s/n, 4200-465 Porto", subheader_style)

    # Add phone and website icons with text
    logo_phone_path = "IMG_3177.jpg"
    logo_phone = Image(logo_phone_path, width=1.0 * cm, height=1.0 * cm)  # Adjust image size as needed
    subheader2 = ImageParagraph(logo_phone_path, "+351 912345678", subheader_style)

    logo_web_path = "IMG_3178.jpg"
    logo_web = Image(logo_web_path, width=1.0 * cm, height=1.0 * cm)
    subheader3 = ImageParagraph(logo_web_path, "scitech.bestporto.org", subheader_style)

    # Add subheaders to elements
    elements.append(subheader1)
    elements.append(subheader2)
    elements.append(subheader3)
    elements.append(Spacer(1, 0.5 * cm))
    class HorizontalLine(Flowable):
        def __init__(self, y_position):
            Flowable.__init__(self)
            self.y_position = y_position

        def wrap(self, availWidth, availHeight):
            return availWidth, 0  # No height, since we're only drawing a line

        def draw(self):
            self.canv.setStrokeColorRGB(0, 0, 0)  # Set the stroke color to black
            self.canv.setLineWidth(3)  # Set the line width
            self.canv.line(0, self.y_position, self.canv._pagesize[0], self.y_position)  # Draw line across the page


    # Add a horizontal line below the ImageParagraph
    line_y_position = -1 # Position for the line, adjust as needed
    horizontal_line = HorizontalLine(line_y_position)
    elements.append(horizontal_line)
    # Create content for the left column (address information)
    left_column_content = [
    Paragraph("Nota de Encomenda para:", text_style),
    Paragraph("SciTeCh Textile Engineering", bold_style),
    Paragraph("Avenida dos Tecidos Nº42", text_style),
    Paragraph("Espaço Industrial Marciano", text_style)
    ]

    # Create content for the right column (order details)
    right_column_content = [
    Paragraph("Encomenda Nº:", bold_style),
    Paragraph(Number, centered_text_style),
    Paragraph("Data:", centered_bold_style),
    Paragraph(date, centered_text_style)
    ]

    # Combine the left and right column contents into a table
    data = [
    [left_column_content, '', right_column_content]
    ]

    # Create a table with two columns
    column_table = Table(data, colWidths=[8 * cm, 3 * cm, 5 * cm])  # Adjust the column widths as needed
    column_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ALIGN', (0, 0), (0, -1), 'LEFT'),  # Left-align the first column
    ('ALIGN', (1, 0), (1, -1), 'CENTER'), # Center-align the second column (empty column)
    ('ALIGN', (2, 0), (2, -1), 'CENTER'), # Center-align the third column
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    # Add the table to the elements
    elements.append(column_table)
    elements.append(Spacer(1, 1 * cm))

    # Item Table Header
    item_data = [
    ["Artigo", "Preço", "Quantidade", "Subtotal"]
    ] + products
    item_table = Table(item_data, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
    item_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor("#b91200")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 16),
    ('FONTSIZE', (0, 1), (-1, 1), 13),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), HexColor("#f7f8f2")),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 15),

    ]))
    elements.append(item_table)
    elements.append(Spacer(1, 0.5 * cm))

    # Total Section
    total_section = [
    ["Total:", "€100"]
    ]
    total_table = Table(total_section, colWidths=[13 * cm, 3 * cm])
    total_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor("#b91200")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 15),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(total_table)
    elements.append(Spacer(1, 0.5 * cm))

    box_style = ParagraphStyle(
    'SubHeaderStyle',
    parent=styles['Normal'],
    fontSize = 16,
    textColor = colors.white,
    spaceAfter = 8,
    alignment=1,  # 1 corresponds to 'CENTER'
    fontName="Helvetica-Bold"

    )
    underlined_style = ParagraphStyle(
    'SubHeaderStyle',
    parent=styles['Normal'],
    fontSize = 40,
    textColor = colors.black,
    spaceAfter = 8,
    alignment=1,  # 1 corresponds to 'CENTER'
    fontName="CustomFont",
    underline=True

    )


    footer_section = [
    [
    Paragraph("Método de Pagamento", box_style),
    Paragraph("", box_style),          # Empty cell for the second column
    Paragraph("", text_style)        # "hi" for the third column
    ],
    [
    Paragraph("Transferência Bancária", text_style),
    Paragraph("", box_style),          # Empty cell for the second column
    Paragraph("", text_style)        # "hi" for the third column
    ],
    [
    Paragraph(" ", bold_style),
    Paragraph("", box_style),          # Empty cell for the second column
    Paragraph("", text_style)        # "hi" for the third column
    ],
    [
    Paragraph("Termos e condições", box_style),
    Paragraph("", box_style),          # Empty cell for the second column
    Paragraph("<u>Overflowers</u>", underlined_style)        # "hi" for the third column
    ],
    [
    Paragraph("Sujeita a confirmação e disponibilidade de stock.", text_style),
    Paragraph("", box_style),          # Empty cell for the second column
    Paragraph("", underlined_style)        # "hi" for the third column
    ]
    ]



    # Create a footer table
    footer_table = Table(footer_section, colWidths=[7 * cm, 5* cm, 4*cm])

    # Set the style for the footer table
    footer_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), HexColor("#b91200")),   # First line background red
    ('BACKGROUND', (0, 1), (0, 1), colors.white),  # Second line background white
    ('BACKGROUND', (0, 2), (0, 2), colors.white),  # Third line background white
    ('BACKGROUND', (0, 3), (0, 3), HexColor("#b91200")),    # Fourth line background red
    ('BACKGROUND', (0, 4), (0, 4), colors.white),  # Fifth line background whit
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all contents
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # Set font for all cells
    ('BOTTOMPADDING', (0, 0), (-1, -1), 15),  # Add padding to all cells
    ]))
    elements.append(footer_table)
    elements.append(Spacer(1, 0.5 * cm))


    # Build PDF
    document.build(elements)


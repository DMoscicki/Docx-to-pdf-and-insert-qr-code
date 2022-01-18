import qrcode
from docx2pdf import convert
import qrcode.image.svg
import PyPDF2 as pypdf
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg


#function creation of QR-Code

def qr_img():

    data = "https://github.com/DMoscicki" #data of qr-code
    method = 'basic'
    if method == 'basic':
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        factory = qrcode.image.svg.SvgFragmentImage
    elif method == 'path':
        factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(data, image_factory=factory)

    img.save("qrcode.svg")
    saved_qr = "qrcode.svg"
    return saved_qr


#convertation

def conv_pdf():
    pppdddfff = convert("Test1.docx")
    return pppdddfff


def insert_to_pdf():
    image_path = "qrcode.svg" #
    filename = "file_for_svg.pdf" # input file
    my_pdf = canvas.Canvas(filename)
    drawing = svg2rlg(image_path)
    renderPDF.draw(drawing, my_pdf, 240, 30)
    my_pdf.save()



    with open("Test1.pdf",  "rb") as inFile, open("file_for_svg.pdf", "rb") as overlay:
        original = pypdf.PdfFileReader(inFile)

        writer = pypdf.PdfFileWriter()


        for i in range(original.getNumPages()):
            background = original.getPage(i)
            foreground = pypdf.PdfFileReader(overlay).getPage(0)
            background.mergePage(foreground)
            page = original.getPage(i)
            writer.addPage(page)

    with open("test_svg_file.pdf", "wb") as outFile:
        writer.write(outFile)

qr_img()
conv_pdf()
insert_to_pdf()

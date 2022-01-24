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
    saved_qr = "qrcode.svg" #saved qr-code
    return saved_qr


#convertation

def conv_pdf():
    pppdddfff = convert("Cover Letter.docx") #main docx file
    return pppdddfff

#insert svg to pdf

def insert_to_pdf():
    image_path = "qrcode.svg" #
    filename = "file_for_svg.pdf" # input file
    my_pdf = canvas.Canvas(filename)
    drawing = svg2rlg(image_path)
    renderPDF.draw(drawing, my_pdf, 265, 30) #coordinates where the image will be
    my_pdf.save() #save the new file with image (.pdf)

#merge 2 pdf

    with open("Cover Letter.pdf",  "rb") as inFile, open("file_for_svg.pdf", "rb") as overlay: #open 2 files
        original = pypdf.PdfFileReader(inFile)

        writer = pypdf.PdfFileWriter()


        for current_page in range(original.getNumPages()): #cicle for taking the pages
            background = original.getPage(current_page) #taking the pages from the main document
            foreground = pypdf.PdfFileReader(overlay).getPage(0) #read the overlay
            background.mergePage(foreground)
            page = original.getPage(current_page)
            writer.addPage(page)
            with open("test_svg_file.pdf", "wb") as outFile:
                writer.write(outFile) #output file

qr_img()
conv_pdf()
insert_to_pdf()

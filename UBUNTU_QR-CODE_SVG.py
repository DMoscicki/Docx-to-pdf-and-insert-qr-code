import qrcode
import qrcode.image.svg
import PyPDF2 as pypdf
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
import fitz
from docx2pdf import convert # is not working on Linux systems
import qrcode.image.svg
from subprocess import Popen


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

libre_office_exe = r"soffice"  # calling the libreoffice
sample_doc = 'Cover Letter1.docx'  # input_docx
# docx_input = 'file_for_svg.docx' # second file for svg
out_folder = '/home/dmitrii/PycharmProjects/pythonProject/'  # output folder
new_folder = '/home/dmitrii/PycharmProjects/pythonProject/'

def convert_to_pdf_1(input_docx, out_folder):
    p = Popen([libre_office_exe, '--headless', '--convert-to', 'pdf', '--outdir',
                out_folder, input_docx])  # command
    print([libre_office_exe, '--convert-to', 'pdf', input_docx])
    p.communicate()

# def convert_to_pdf_2(docx_input, out_folder):
#     s = Popen([libre_office_exe, '--headless', '--convert-to', 'pdf', '--outdir',
#                out_folder, docx_input])
#     print([libre_office_exe, '--convert-to', 'pdf', docx_input])
#     s.communicate()


def insert_to_pdf():
    image_path = "qrcode.svg" #
    filename = "file_for_svg.pdf" # input file
    my_pdf = canvas.Canvas(filename)
    drawing = svg2rlg(image_path)
    renderPDF.draw(drawing, my_pdf, 240, 30)
    my_pdf.save()


    with open("Cover Letter1.pdf",  "rb") as inFile, open("file_for_svg.pdf", "rb") as overlay: # open 2 files
        original = pypdf.PdfFileReader(inFile)

        writer = pypdf.PdfFileWriter()


        for current_page in range(original.getNumPages()): #cicle for taking the pages
            background = original.getPage(current_page) #taking the pages from the main document
            foreground = pypdf.PdfFileReader(overlay).getPage(0) #read the overlay
            background.mergePage(foreground)
            writer.addPage(background)
            with open("test_svg_file.pdf", "wb") as outFile:
                writer.write(outFile)

qr_img()
convert_to_pdf_1(sample_doc, out_folder)
# convert_to_pdf_2(docx_input, out_folder)
insert_to_pdf()
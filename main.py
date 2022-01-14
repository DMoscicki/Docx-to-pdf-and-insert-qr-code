import pdfrw
import qrcode
from docx2pdf import convert
import fitz
from fitz import Rect
import qrcode.image.svg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import PyPDF2 as pypdf
from PyPDF2.pdf import PageObject


#function creation of QR-Code

def qr_img():
    # qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5,
    #                     border=5)
    data = "https://iac.spb.ru/" #data of qr-code
    # qr.add_data(data)
    # qr.make(fit=True)
    # img2 = qr.make_image(fill_color='black', back_color='white') #parameters
    # img2.save('qr.png') #save the qr code as png
    # saved_qr = 'qr.png'
    # return saved_qr
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
    print(f"Put the direction of the .docx file:")
    pppdddfff = convert(str(input()))
    drawning = svg2rlg(qr_img())
    renderPDF.drawToFile(drawning, "file_svg.pdf")
    return pppdddfff


def insert_to_pdf():
    # image_path = qr_img() #
    # image_rectangle = fitz.Rect(0, 0, 450, 20) #upper right-corner
    # image_rectangle1 = fitz.Rect(600, 600, 700, 700)
    # image_rectangle2 = Rect(0, 0, 842, 575) #right-bottom
    # image_rectangle3 = Rect(600, 730, 610, 800)
    # filename = str(input()) # input file
    # if filename.endswith(".docx"): # check the type of file
    #     print("Bad format") #attention



    with open("C:/Users/d.mastitskiy/Downloads/Cover Letter.pdf",  "rb") as inFile, open("file_svg.pdf", "rb") as overlay:
        original = pypdf.PdfFileReader(inFile)
        # background = original.getPage(0)
        # foreground = pypdf.PdfFileReader(overlay).getPage(0)
        #
        # background.mergePage(foreground)


        writer = pypdf.PdfFileWriter()


        for i in range(original.getNumPages()):
            background = original.getPage(i)
            foreground = pypdf.PdfFileReader(overlay).getPage(0)
            background.mergePage(foreground)
            page = original.getPage(i)
            writer.addPage(page)

    with open("test_svg_file.pdf", "wb") as outFile:
        writer.write(outFile)



    #
    # merger.close()
    # pdf1 = fitz.open("file_svg.pdf")
    # pdf2 = fitz.open("new.pdf")
    # pdf2.insert_pdf(pdf1)
    # pdf2.save("test_svg_file.pdf")
    # for current_page in range(len(pdf2)): #check each page
    #     if current_page >= 0:
    #         # page = pdf_document[current_page] #page
    #         pdf1.insert_pdf(pdf2[current_page]) #insert pic to the page
    #         pdf1.save("test_svg_file.pdf")
    #         print("QR-code inserted") #checked
    #     if current_page == 0:
    #         ValueError("File wasn't send")

    # output_doc = pdf_document.save(output_file) #save the output file
    # return output_doc



# qr_img()
conv_pdf()
insert_to_pdf()
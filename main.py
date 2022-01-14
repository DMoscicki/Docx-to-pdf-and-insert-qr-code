import qrcode
from docx2pdf import convert
import fitz
from fitz import Rect


#function creation of QR-Code

def qr_img():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5,
                        border=5)
    data = "https://github.com/DMoscicki" #data of qr-code
    qr.add_data(data)
    qr.make(fit=True)
    img2 = qr.make_image(fill_color='black', back_color='white') #parameters
    saved_qr = img2.save('qr.png') #save the qr code as png
    return saved_qr


#convertation

def conv_pdf():
    pppdddfff = convert("img_test1.docx")
    return pppdddfff


def insert_to_pdf():
    image_path = 'hello.png'
    # image_rectangle = fitz.Rect(0, 0, 450, 20) #upper right-corner
    # image_rectangle1 = fitz.Rect(600, 600, 700, 700)
    image_rectangle2 = Rect(510, 760, 590, 835) #right-bottom
    filename = "img_test1" + ".pdf" # input file
    if filename.endswith(".docx"): # check the type of file
        print("Bad format") #attention
    output_file = "test1.pdf" #output file
    pdf_document = fitz.open(filename)
    for current_page in range(len(pdf_document)): #check each page
        if current_page >= 0:
            page = pdf_document[current_page] #page
            page.insert_image(image_rectangle2, filename=image_path) #insert pic to the page
            print("QR-code inserted") #checked
        if current_page == 0:
            ValueError("File wasn't send")

    output_doc = pdf_document.save(output_file) #save the output file
    return output_doc


qr_img()
conv_pdf()
insert_to_pdf()
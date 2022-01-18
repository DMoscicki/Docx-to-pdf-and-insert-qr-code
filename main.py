import fitz
import qrcode
from docx2pdf import convert
import qrcode.image.svg

# step - 1 (creation QR-Code)

def qr_img():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5,
                      border=5) #parameters of qr-code
    data = "https://github.com/DMoscicki" #data of qr-code
    qr.add_data(data) #insert data to qr-code
    qr.make(fit=True)
    img2 = qr.make_image(fill_color='black', back_color='white')  # parameters
    saved_qr = img2.save('qr.png')  # save the qr code as png
    return saved_qr

# step - 2 (convertation)

def conv_pdf():
    pppdddfff = convert("Test1.docx") #covertation
    return pppdddfff

# step - 3 (insert png to pdf)

def insert_to_pdf():
    image_path = "qr.png" # image svg
    img_rect = fitz.Rect(510, 760, 590, 835)
    doc = fitz.open("Test1.pdf") #converted .docx
    for page_doc in range(len(doc)): # cicle for pages
        page = doc[page_doc]
        page.insert_image(img_rect, filename=image_path) #parameters of image
        doc.save("test_fitz_output.pdf") #output document
    doc.close() #close document

qr_img()
conv_pdf()
insert_to_pdf()
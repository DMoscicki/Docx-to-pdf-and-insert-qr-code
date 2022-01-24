import fitz
import qrcode
from docx2pdf import convert # is not working on Linux systems
import qrcode.image.svg
from subprocess import Popen


# step - 1 (creation QR-Code)

def qr_img():
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5,
                      border=5)
    data = "https://github.com/DMoscicki" #data of qr-code
    qr.add_data(data)
    qr.make(fit=True)
    img2 = qr.make_image(fill_color='black', back_color='white')  # parameters
    saved_qr = img2.save('qr.png')  # save the qr code as png
    return saved_qr


# step - 2 (convertation)

libre_office_exe = r"soffice" #calling the libreoffice
sample_doc = 'Cover Letter.docx' # input_docx
out_folder = '/home/dmitrii/PycharmProjects/pythonProject/' # output folder

def convert_to_pdf(input_docx, out_folder):
    p = Popen([libre_office_exe, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx]) #command
    print([libre_office_exe, '--convert-to', 'pdf', input_docx])
    p.communicate()

# step - 3 (merge 2 PDF docs into the 1 file)

def insert_to_pdf():
    image_path = "qr.png" # image svg
    img_rect = fitz.Rect(510, 690, 600, 790)
    file_without_docx = "Cover Letter"
    doc = fitz.open(file_without_docx + ".pdf")
    for page_doc in range(len(doc)):
        page = doc[page_doc]
        page.insert_image(img_rect, filename=image_path)
        doc.save("test_fitz_output.pdf")
    doc.close()

qr_img()
convert_to_pdf(sample_doc, out_folder)
insert_to_pdf()
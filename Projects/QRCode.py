# pip install qrcode
import qrcode as qr

def create_normal_qr_code():
    img = qr.make('https://chatgpt.com/')
    img.save('QRCodes/qrcode-example.png')

def create_customized_qr_code():
    qr_code = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=5)
    qr_code.add_data('https://chatgpt.com/')
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color='white', back_color='blue')
    img.save('QRCodes/qrcode-example-2.png')

if __name__ == "__main__":
    create_normal_qr_code()
    create_customized_qr_code()

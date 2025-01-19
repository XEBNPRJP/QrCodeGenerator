import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)  
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

print("Welcome to Eloy's QR Code Generator,")
text= input("Write the website you want to generate a QR code for: ")
file_name="qr_code.png"
generate_qr_code(text, file_name)
print(f"QR code generated and saved as {file_name}")

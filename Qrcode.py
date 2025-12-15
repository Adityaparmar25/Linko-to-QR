import qrcode

link = input('Enter the link: ')
qr_img = qrcode.make(link)

qr_img.save("qr_code.png")
print("QR code generated and saved as qr_code.png")

print(qr_img)
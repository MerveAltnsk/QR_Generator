import pyqrcode

url = input("Enter the URL to generate QR code: ")

qr_code = pyqrcode.create(url)
qr_code.png('QR_Code.png', scale=5)
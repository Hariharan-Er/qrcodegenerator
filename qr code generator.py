import pyqrcode
import png
print("                   QR CODE GENERATOR                             ")
print("-----------------------------------------------------------------")
data = input("Enter text to generate qr code :")
img = pyqrcode.create(data)
img.show()


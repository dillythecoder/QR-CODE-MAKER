import qrcode
a = input("Link: ")
image = qrcode.make(a)
image.save("qr.png","PNG")

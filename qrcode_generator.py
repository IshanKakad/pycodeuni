#Install the pip install qrcode in your terminal window

import qrcode

# get text to encode in the QR code from user input
text = input("Enter text to encode in QR code: ")

# create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# add data to the QR code
qr.add_data(text)

# compile the QR code
qr.make(fit=True)

# create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# save the image to a file
img.save("qrcode.png")

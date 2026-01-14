import qrcode
data=input('Enter the Text or Url:  ').strip()
filename=input('Enter The filename:   ').strip()
qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image=qr.make_image(fill_colour="black",back_color="white")
image.save(filename)
print(f"qr code successfully add as {filename}")
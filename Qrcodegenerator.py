import qrcode
import image
qr = qrcode.QRCode(
    version= 15,  #15 means the version of the qrcode
    box_size= 10,  #size of the box where qr code will be displayed
    border = 5    #white part of the image -- border in all 4 sides with white color

)

data = "http://www.tridonsolar.in/"     #Example

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")
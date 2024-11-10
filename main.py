import qrcode
import cv2

def encode_qr():
    qr=qrcode.make("6543322112@ybi")
    qr.save('upi.jpg')
encode_qr()

def decode_qr(image):
    detector=cv2.QRCodeDetector()
    data=detector.detectAndDecode(cv2.imread(image))

    return data
upicode=decode_qr("upi.jpg")
print(upicode)
#decode_qr("upi.jpg")


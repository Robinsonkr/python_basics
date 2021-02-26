#install,pyqrcode,pypng
import pyqrcode as qrcode

my_text ="https://www.youtube.com/c/Learn2Hack"

my_qr = qrcode.create(my_text)

#output
my_qr.png("test.png")
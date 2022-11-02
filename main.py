#you need to import qr code library (pip install qrcode)
import qrcode

#for basic qr code
img = qrcode.make('https://github.com/random-cell')
type(img) 
img.save("My Link")

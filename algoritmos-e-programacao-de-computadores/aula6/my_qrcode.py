import qrcode
img = qrcode.make('SAGFCGA')
type(img) 
img.save("js.png")
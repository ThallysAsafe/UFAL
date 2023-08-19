import qrcode
img = qrcode.make('Thallis é um medico')
type(img) 
img.save("j.png")
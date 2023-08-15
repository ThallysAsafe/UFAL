import qrcode
img = qrcode.make('Bom Soninho!')
type(img)  # qrcode.image.pil.PilImage
img.save("Nogueira.png")
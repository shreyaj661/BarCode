import qrcode.image.svg

def func_img(arg_link):
    print('')
    img = qrcode.make(arg_link,image_factory=qrcode.image.svg.SvgImage)

img_linkedin = qrcode.make('https://www.linkedin.com/in/shreyaj661/', image_factory=qrcode.image.svg.SvgImage)

with open('LinkedIn.svg','wb') as qr_linkedin:
    img_linkedin.save(qr_linkedin)


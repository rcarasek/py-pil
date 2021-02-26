from PILLOW import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps
import PILLOW 

iii= PILLOW.Image.open('PequenoDatilo.jpg')

draw = ImageDraw(iii)
font = ImageFont.truetype('arial.fft', size = 80)
draw.text((50,50), 'hello world', fill = 'rgb(0,0,0) ', font=font)
iii.save('PequenoDatilo_Draw.jpg')


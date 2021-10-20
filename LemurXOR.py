
from PIL import Image, ImageChops

pic1 = Image.open('flag.png')
pic2 = Image.open('lemur.png')

FLG = ImageChops.add(ImageChops.subtract(pic2, pic1), ImageChops.subtract(pic1, pic2))
FLG.save('FLG.png')


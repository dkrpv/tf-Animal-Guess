from PIL import Image
from collections import defaultdict

pug = Image.open('pug.jpg')
dd = defaultdict
color = dd(int)
for pixel in pug.getdata():
    color[pixel] += 1

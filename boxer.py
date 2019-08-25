from PIL import Image
from collections import defaultdict

boxer = Image.open('boxer.jpg')
dd = defaultdict
color = dd(int)
for pixel in boxer.getdata():
    color[pixel] += 1

from PIL import Image
from collections import defaultdict

germanshepherd = Image.open('germanshepherd.jpg')
dd = defaultdict
color = dd(int)
for pixel in germanshepherd.getdata():
    color[pixel] += 1

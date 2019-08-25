from PIL import Image
from collections import defaultdict

basset = Image.open('basset.jpg')
dd = defaultdict
color = dd(int)
for pixel in basset.getdata():
    color[pixel] += 1

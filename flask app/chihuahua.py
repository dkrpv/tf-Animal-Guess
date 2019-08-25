from PIL import Image
from collections import defaultdict

chihuahua = Image.open('chihuahua.jpg')
dd = defaultdict
color = dd(int)
for pixel in chihuahua.getdata():
    color[pixel] += 1

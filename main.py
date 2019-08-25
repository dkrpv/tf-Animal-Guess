from difflib import SequenceMatcher
from PIL import Image
from collections import defaultdict
from colorama import init, Fore, Back, Style
import basset
import pug
import chihuahua
import germanshepherd
import boxer

init(convert=True)
print(Fore.BLUE + "The dog guesser 9000")
inputimg = input("Path to the image: ")

imgsrc = Image.open(inputimg)
dd = defaultdict
imgcolor = dd(int)
for pixel in imgsrc.getdata():
    imgcolor[pixel] += 1

sm = SequenceMatcher
def compare(x, y):
    return sm(None, x, y).ratio()

a1 = compare(basset.color, imgcolor)
a2 = compare(pug.color, imgcolor)
a3 = compare(chihuahua.color, imgcolor)
a4 = compare(germanshepherd.color, imgcolor)
a5 = compare(boxer.color, imgcolor)

print(a1, "Basset")
print(a2, "Pug")
print(a3, "Chihuahua")
print(a4, "German Shepherd")
print(a5, "Boxer")

from flask import Flask, request, url_for, render_template
from difflib import SequenceMatcher
from PIL import Image
from collections import defaultdict
from colorama import init, Fore, Back, Style
from io import BytesIO
import requests
import shutil
import pug
import chihuahua
import basset
import boxer
import germanshepherd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def stuff():
	context= {

	}
	if request.method == "POST":
		linksrc = request.form["linktxt"]
		linkfin = requests.get(linksrc)
		file_linkdata = BytesIO(linkfin.content)
		imgop = Image.open(file_linkdata)
		dd = defaultdict
		imgcolor = dd(int)
		for pixel in imgop.getdata():
			imgcolor[pixel] += 1
		sm = SequenceMatcher
		def compare(x, y):
			return sm(None, x, y).ratio()
		a1 = compare(basset.color, imgcolor)
		a2 = compare(pug.color, imgcolor)
		a3 = compare(chihuahua.color, imgcolor)
		a4 = compare(germanshepherd.color, imgcolor)
		a5 = compare(boxer.color, imgcolor)

		maxval = max(a1, a2, a3, a4, a5)
		context["img1"] = linksrc
		if maxval == a1:
			context["dog"] = "Basset"
			context["img2"] = "http://geniusvets.s3.amazonaws.com/gv-dog-breeds/basset-hound-1.jpg"
		elif maxval == a2:
			context["img2"] = "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12225358/Pug-On-White-01.jpg"
			context["dog"] = "Pug"
		elif maxval == a3:
			context["dog"] = "Chihuahua"
			context["img2"] = "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12234710/Chihuahua-On-White-03.jpg"
		elif maxval == a4:
			context["dog"] = "German Shepherd"
			context["img2"] = "https://www.zooplus.ie/magazine/CACHE_IMAGES/768/content/uploads/2019/04/german-shepherd.jpg"
		else:
			context["dog"] = "Boxer"
			context["img2"] = "https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555356516/shape/mentalfloss/istock_000001881954_small.jpg"
		print(a1, "Basset")
		print(a2, "Pug")
		print(a3, "Chihuahua")
		print(a4, "German Shepherd")
		print(a5, "Boxer")
		print(Fore.YELLOW + linksrc)
		print(maxval)
	return render_template("index.html", context=context)

if __name__=="__main__":
	app.run(host='0.0.0.0')


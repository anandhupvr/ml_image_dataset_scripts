import sys
import os
from os import listdir, getcwd, walk
from lxml import etree
from PIL import Image
import converter.utils as utils

count = 0
img_dir = "/home/ubuntu/anandhu/open_images/"
current_dir = os.getcwd()
label_dir = current_dir+"/labels/"
yolo_label_dir = current_dir+"/yolo_label/"

if not os.path.exists(current_dir+"/yolo_label/"):
	os.mkdir(current_dir+"/yolo_label/")

for cat in os.listdir(label_dir):

	img_dir_new = img_dir + cat + "/"
	for lab in os.listdir(label_dir+"/"+cat):
		txt_path = label_dir+"/"+cat+"/"+lab
		txt_file = open(txt_path,"r")
		lines = txt_file.read().split('\n')
		if not os.path.exists(yolo_label_dir+cat):
			os.mkdir(yolo_label_dir+cat)
		txt_outfile = open(yolo_label_dir+"/"+cat+"/"+lab, "w")

		ct = 0
		for line in lines:
			if (len(line) >= 4):
				ct = ct + 1 
				elems = line.split(' ')

				xmin = elems[1]
				xmax = elems[2]
				ymin = elems[3]
				ymax = elems[4]

				cls_id = count

				
				img_path = str('%s/%s.jpg'%(os.path(img_dir), os.path.splitext(lab)[0]))
				img_path = str('%s%s.jpg'%(img_dir_new,lab.replace('.txt','')))

				im = Image.open(img_path)
				w = int(im.size[0])
				h = int(im.size[1])

				b = (float(xmin), float(xmax), float(ymin), float(ymax))

				bb = utils.convert((w,h), b)

				txt_outfile.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
count += 1


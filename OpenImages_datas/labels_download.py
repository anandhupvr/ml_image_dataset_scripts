import os
import pandas as pd
import csv
from PIL import Image

cat_dict = {}
cat_list = [cat for cat in os.listdir('/home/christie/anandhu/openImages/')]
count = 1
for cat in cat_list:
    cat_dict[cat] = count
    count += 1


def imageShape(image_id, cat_name):
    for img in os.listdir(path + cat_name + "/"):
        a = img
        if a.replace(".jpg", "") == image_id:
            print("matched")
            im = Image.open(path + cat_name + "/" + img)
            width, height = im.size
            return (width, height)


def in_txt(annotate_data, cat_name):
    for index, row in annotate_data.iterrows():
        path_lab = path_labels + cat_name + "/"
        if not os.path.exists(path_lab):
            os.makedirs(path_lab)
        item = [it.replace(".txt", "") for it in os.listdir(path_lab)]
        if (row['ImageID'] in item):
            print("appending Downloading ....")
            width, height = imageShape(str(row['ImageID']), cat_name)
            width = round(width, 2)
            height = round(height, 2)

            with open(path_lab + str(row['ImageID']) + ".txt", 'a+')as f:
                f.write("\n" +
                        str(cat_dict[cat_name]) +
                        " " +
                        str(row['XMin'] *
                            width) +
                        " " +
                        str(row['XMax'] *
                            width) +
                        " " +
                        str(row['YMin'] *
                            height) +
                        " " +
                        str(row['YMax'] *
                            height))
        else:
            print("no appending and Downloading ...")
            width, height = imageShape(str(row['ImageID']), cat_name)

            with open(path_lab + str(row['ImageID']) + ".txt", 'w+') as f:
                f.write(str(cat_dict[cat_name]) +
                        " " +
                        str(row['XMin'] *
                            width) +
                        " " +
                        str(row['XMax'] *
                            width) +
                        " " +
                        str(row['YMin'] *
                            height) +
                        " " +
                        str(row['YMax'] *
                            height))


def annotation(label_name, cat_name):
    an_data = pd.read_csv(
        'train-annotations-bbox.csv',
        usecols=[
            'ImageID',
            'LabelName',
            'Confidence',
            'XMin',
            'XMax',
            'YMin',
            'YMax'])
    label_name_l = []
    label_name_l.append(label_name)
    ann_img = an_data[an_data.LabelName.isin(label_name_l)]
    cat_name = cat_name.replace(" ", "_")
    cat_name = cat_name.lower()
    in_txt(ann_img, cat_name)


def download(cat_name):
    # print (cat_name)
    # cat_name = cat_name.capitalize()
    # cat_name = cat_name.replace("_", " ")
    class_discr = pd.read_csv(
        'class-descriptions-boxable.csv',
        names=[
            'cat',
            'name'])
    class_dict = {}
    for i, j in zip(class_discr['cat'], class_discr['name']):
        class_dict[i] = j
    print(cat_name + " : " + class_dict[cat_name])
    label_name = class_dict[cat_name]
    annotation(label_name, cat_name)


# path = '/home/christie/anandhu/openImages/'
# path_labels = '/home/christie/anandhu/script/'
# # path_datas = '/home/ubuntu/anandhu/open_images/test/'
# for cat in os.listdir(path):
# 	try:
# 		download(cat)
# 	except Exception as e:
# 		print (e)
cat_name = sys.argv[1]
try:
    download(cat_name)
except Exception as e:
    print(e)

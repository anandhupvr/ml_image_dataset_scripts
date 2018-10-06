import os
import pandas as pd
import csv


def annotation(img_id_list, label_name):
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


def download(cat_name):
    print(cat_name)
    # os.system('mkdir '+cat_name)
    class_discr = pd.read_csv(
        'class-descriptions-boxable.csv',
        names=[
            'cat',
            'name'])
    class_dict = {}
    for i, j in zip(class_discr['cat'], class_discr['name']):
        class_dict[j] = i
    print(class_dict[cat_name])
    label_name = class_dict[cat_name]

    imgId = pd.read_csv('train-annotations-human-imagelabels-boxable.csv')
    img = []
    for i, j in zip(imgId['ImageID'], imgId['LabelName']):
        if (label_name == j):
            img.append(i)
    print(len(img))

    annotation(img, label_name)


cat_name = sys.argv[1]
download('Bell pepper')

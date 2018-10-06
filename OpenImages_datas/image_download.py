import os
import pandas as pd
import csv


def download(cat_name):

    class_discr = pd.read_csv(
        'class-descriptions-boxable.csv',
        names=[
            'cat',
            'name'])
    class_dict = {}
    for i, j in zip(class_discr['cat'], class_discr['name']):
        class_dict[j] = i
    print()
    label_name = class_dict[cat_name]

    cat_name = cat_name.replace(" ", "_")
    os.system('mkdir ' + cat_name.lower())

    imgId = pd.read_csv('train-annotations-human-imagelabels-boxable.csv')
    img = []
    for i, j in zip(imgId['ImageID'], imgId['LabelName']):
        if (label_name == j):
            img.append(i)
    print(len(img) + cat_name + " images downloading")
    print(class_dict[cat_name] + "is the label name of " + cat_name)
    imgUrl = pd.read_csv(
        'train-images-boxable-with-rotation.csv',
        usecols=[
            'ImageID',
            'OriginalURL'])

    ab = (imgUrl[imgUrl.ImageID.isin(img)])
    #print (ab)

    for i, j in zip(ab['ImageID'], ab['OriginalURL']):
        try:
            cmd = "wget " + j + " -O" + cat_name.lower() + "/" + i + ".jpg"
        print(cmd)
        os.system(cmd)
        except Exception as e:
            print(e)


# fh = open('labels.txt').readlines()

# cat_list = [line.replace("\n", "") for line in fh if not line.isspace()]
cat_name = sys.argv[1]
download(cat_name)

# for cat in cat_list:
#     download(cat)
#     print(cat + " is downloaded")

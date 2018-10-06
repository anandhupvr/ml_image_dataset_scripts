import sys
import urllib2
import os


# image name as the argument
cat_name = sys.argv[1]
save_dir = '/home/ubuntu/anandhu/' + cat_name
print (cat_name)
words = open('words.txt', 'r')
word_dict = {}
while True:
    line = words.readline()
    if not line:
        break
    split = line.split('\t')
    word_dict[split[1]] = split[0]
wordNetID = word_dict[cat_name + '\n']
imgNet_url = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=' +
                wordNetID
data = urllib2.urlopen(imgNet_url)
for lines in data:
    cmd = "wget -P " + save_dir + "/  " + lines
    print (cmd)
    os.system(cmd)
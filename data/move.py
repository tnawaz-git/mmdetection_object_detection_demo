import os
import shutil 
anno = []
for fi in os.listdir("Annotations"):
    anno.append(fi.replace(".xml", ""))
for files in os.listdir("ImageSets2/"):
    if files.replace(".png","") in anno:
        shutil.copy("ImageSets2/{}".format(files),"ImageSets/{}".format(files))



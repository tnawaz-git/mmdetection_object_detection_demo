import os 
import shutil
from tqdm import tqdm 

imgs = os.listdir("eobs for labelling/")
index = 0 

for fi in tqdm(imgs):
    while "{}.png".format(index) in os.listdir("ImageSets/"):
        index += 1
    shutil.copy("eobs for labelling/{}".format(fi), "ImageSets2/{}.png".format(index))
    index += 1

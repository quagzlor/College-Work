import numpy as np
from PIL import Image
import os
from tqdm import tqdm
from random import shuffle
import pickle

from keras.applications.imagenet_utils import preprocess_input as keras_preprocess_input
import keras.preprocessing.image as keras_preprocess_image

from tkinter.filedialog import askdirectory

def IMG_to_np(image,directory_num):
    image = Image.open(image)
    image = image.resize((64,64))
    image = keras_preprocess_image.img_to_array(image.convert('RGB'))
    image = image.reshape(64,64,3)
    image = np.expand_dims(image, axis=0)
    image = keras_preprocess_input(image)

    hot_label = [0]*62
    hot_label[directory_num] = 1

    return ([image,hot_label])

def INFO_dump(data):
    split = int(len(data)/5)
    split = len(data) - split

    training = data[:split]
    testing = data[split:]

    outfile = open("training","wb")
    pickle.dump(training,outfile)
    outfile.close()

    outfile = open("testing","wb")
    pickle.dump(testing,outfile)
    outfile.close()

def IN_dir(directory,filetype):
    folder_list = []

    for filename in os.listdir(directory):
        if (filename.endswith(filetype)):
            folder_list.append(os.path.join(directory,filename))

    return folder_list

def main():
    data_path = askdirectory()
    dir_list = IN_dir(data_path,"")

    data_list = []

    for i in tqdm(range(len(dir_list))):
        img_list = IN_dir(dir_list[i],".png")

        for j in tqdm(range(len(img_list))):
            data_list.append(IMG_to_np(img_list[j],i))

    shuffle(data_list)

    INFO_dump(data_list)

main()
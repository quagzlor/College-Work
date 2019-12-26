import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, InputLayer
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras import models
from keras.applications.imagenet_utils import preprocess_input as keras_preprocess_input
import keras.preprocessing.image as keras_preprocess_image

from PIL import Image

from tkinter.filedialog import askopenfilename

def img_convert(image):
    image = Image.open(image)
    image = image.resize((64,64))
    image = keras_preprocess_image.img_to_array(image.convert('RGB'))
    image = image.reshape(64,64,3)
    image = np.expand_dims(image, axis=0)
    image = keras_preprocess_input(image)

    return image
epochs = 25
lr = 0.01

model = Sequential()

model.add(InputLayer(input_shape = [64,64,3]))

model.add(Conv2D(32,(3,3), activation = 'relu', padding='same'))
model.add(Conv2D(32,(3,3), activation = 'relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.4))

model.add(Conv2D(64, (3,3), activation = 'relu', padding='same'))
model.add(Conv2D(64,(3,3), activation = 'relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(512, activation = 'relu'))
model.add(Dropout(0.4))
#model.add(Dense(256, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(62, activation = 'softmax'))

opti = SGD()

model.compile(loss = 'categorical_crossentropy', optimizer = opti, metrics = ['accuracy'])

print (model.summary())

model.load_weights('nn_weights.h5')

filename = askopenfilename()

image = img_convert(filename)

prediction = model.predict(image)

print (prediction.argmax(axis=1))
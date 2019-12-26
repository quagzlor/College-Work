import numpy as np

import os
import pickle

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, InputLayer
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras import models

from sklearn.metrics import confusion_matrix
#import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix

def DATA_load(filename):
    infile = open(filename,'rb')
    loaded_data = pickle.load(infile)
    infile.close()

    row1 = []
    for item in loaded_data: #Splitting the data into image data
        row1.append(item[0])
    row1 = np.array(row1)
    row1 = row1.astype('float32')/255.0 #Normalise the iamge array
    row1 = np.squeeze(row1)
    
    row2 = []
    for item in loaded_data: #And label data
        row2.append(item[1])
    row2 = np.array(row2)

    return row1,row2

def TRAIN_network():
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

    xtrain, ytrain = DATA_load('training')
    xtest, ytest = DATA_load('testing')

    print ("Loaded Data")

    #model = MODEL_build(epochs, lr)

    model.load_weights('nn_weights.h5')

    print ("Built Model")

    model.fit(xtrain,ytrain, validation_data = (xtest, ytest), epochs = epochs, batch_size = 100)

    scores = model.evaluate(xtest,ytest,verbose = 0)

    print ("Accuracy: %.2f%%" % (scores[1]*100))

    model.save_weights('nn_weights.h5')

    y_pred = model.predict(xtest)
    cm = confusion_matrix(ytest.argmax(axis=1),y_pred.argmax(axis=1))
    
    #df_cm = pd.DataFrame(cm, range(len(cm)), range(len(cm[0])))
    #sn.set(font_scale= 1.4)
    #sn.heatmap(df_cm, annot = True)

    #plt.show()
    """ 
    layer_outputs = [layer.output for layer in model.layers[:6]] 
    # Extracts the outputs of the top 12 layers

    activation_model = models.Model(inputs=model.input, outputs=layer_outputs)
    img_tensor = np.vstack([xtest[0]])
    activations = activation_model.predict(img_tensor)
    first_layer_activation = activations[0]
    print(first_layer_activation.shape)
    plt.matshow(first_layer_activation[0, :, :, 4], cmap='viridis')
    """
    #fig, ax = plot_confusion_matrix(conf_mat=cm,
    #                            colorbar=True,
    #                            show_absolute=False,
    #                            show_normed=True)
    plt.imshow(cm, cmap='binary', interpolation='None')
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.show()

    #x = pd.crosstab(ytest.argmax(axis=1), y_pred.argmax(axis=1), rownames=['True'], colnames=['Predicted'], margins=True)
    #print (x)
epochs = 1
lr = 0.01



TRAIN_network()
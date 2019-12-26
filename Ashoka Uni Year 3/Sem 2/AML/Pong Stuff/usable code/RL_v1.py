import pong_v0 as pongo
import numpy as np
import random
from collections import deque #Used for replay memory

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import InputLayer
from keras.optimizers import Adam
from keras import backend as K

import tensorflow as tf

EPISODES = 3000

class RL:
    #Params
    ACTIONS = 3

    img_size = 84
    learning_rate = 0.80

    def __init__(self):
        self.memory=deque(maxlen=3000)
        self.gamma = 0.9 #Discount rate
        self.epsilon = 1 #Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.8
        self.model = self.ModelBuild()
        self.target_model = self.ModelBuild()
        self.update_target_model()

    def CustomLoss(self,ytrue,ypred,delta=1.0): #Loss function (Uses Huber Loss)
        error = ytrue - ypred
        cond = K.abs(error) <= delta

        squared_loss = 0.5 * K.square(error)
        quadratic_loss = 0.5 * K.square(delta) + delta * (K.abs(error) - delta)

        return K.mean(tf.where(cond, squared_loss, quadratic_loss))

    def ModelBuild(self): #Builds the model to use
        model = Sequential()

        model.add(Dense(24, input_dim = '84', activation = 'relu'))
        model.add(Dense(24, activation = 'relu'))
        model.add(Dense(3, activation = 'linear'))
        model.compile(loss = self.CustomLoss, optimizer = Adam(lr = 0.8))

        return model

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def recall(self,state,action,reward,next_state,done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(3)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self,batch_size):
        mini_batch = random.sample(self.memory,batch_size)

        for state,action,reward,next_state,done in mini_batch:
            target = self.model.predict(state)
            if done:
                target[0][action] = reward
            else:
                temp = self.target_model.predict(next_state)[0]
                target[0][action] = reward + self.gamma * np.amax(temp)

            self.model.fit(state,target,epochs = 1, verbose = 0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load_weights(self,name):
        self.model.load_weights(name)

    def save_weights(self,name):
        self.model.save_weights(name)


pong = pongo.Pong()
state_size = '84'
action_size = 3
game = RL()
#game.load_weights('saved')

done = False
batch_size = 40
for i in range(EPISODES):
    state = pong.getPresentFrame()
    state = np.reshape(state[1],state_size)

    for step in range(1000):
        action = game.act(state)
        reward,next_state = pong.getNextFrame(action)

        next_state = np.reshape(next_state,state_size)
        
        game.recall(state,action,reward,next_state,done)
        state = next_state
    game.update_target_model()

    if len(game.memory) > batch_size:
        agent.replay(batch_size)
    game.save_weights('saved')
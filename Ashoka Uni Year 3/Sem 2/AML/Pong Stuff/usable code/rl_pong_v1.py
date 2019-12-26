import tensorflow as tf
import pong_v0 as pong  #The game
import numpy as np
import random

from collections import deque #Queue data structure for memory


#HYPER PARAMS
ACTIONS = 3  #Stay/Up/Down

#Learning Rate
GAMMA = 0.99

#Epsilon to adjust gradient
INITIAL_EPSILON = 0.25
FINAL_EPSILON = 0.05

#Epsilon Decay
EXPLORE = 500000

#Smaller training batches
OBSERVE = 10000

#Replay Memory Size
REPLAY_MEMORY = 500000

#BAtch Size
BATCH = 100
# input image size in pixels
INPUT_SIZE = 84

#Tensorflow model
def createModel():

    #Convoluted Neural Net

    #Empty Tensor
    W_conv1 = tf.Variable(tf.random_normal([8, 8, 4, 32]))
    b_conv1 = tf.Variable(tf.random_normal([32]))

    W_conv2 = tf.Variable(tf.random_normal([4, 4, 32, 64]))
    b_conv2 = tf.Variable(tf.random_normal([64]))

    W_conv3 = tf.Variable(tf.random_normal([3, 3, 64, 64]))
    b_conv3 = tf.Variable(tf.random_normal([64]))

    W_fc4 = tf.Variable(tf.random_normal([7 * 7 * 64, 784]))  # image size 7x7 due to convolutions
    b_fc4 = tf.Variable(tf.random_normal([784]))

    W_fc5 = tf.Variable(tf.random_normal([784, ACTIONS]))
    b_fc5 = tf.Variable(tf.random_normal([ACTIONS]))

    #Image data input
    size = tf.placeholder("float", [None, INPUT_SIZE, INPUT_SIZE, 4])

    #Conv2D with relu activation
    conv1 = tf.nn.relu(
        tf.nn.conv2d(size, W_conv1, strides=[1, 4, 4, 1], padding="VALID") + b_conv1)

    conv2 = tf.nn.relu(
        tf.nn.conv2d(conv1, W_conv2, strides=[1, 2, 2, 1], padding="VALID") + b_conv2)

    conv3 = tf.nn.relu(
        tf.nn.conv2d(conv2, W_conv3, strides=[1, 1, 1, 1], padding="VALID") + b_conv3)

    conv3_flat = tf.reshape(conv3, [-1, 7 * 7 * 64])

    #Flattened layers
    fc4 = tf.nn.relu(tf.matmul(conv3_flat, W_fc4) + b_fc4)

    fc5 = tf.matmul(fc4, W_fc5) + b_fc5

    #Returns both input and final output
    return size, fc5



#The Deep Q Network, to feed in the image data
def trainGraph(inp, out, sess):

    # Argmax function
    argmax = tf.placeholder("float", [None, ACTIONS])
    gt = tf.placeholder("float", [None])

    #Game Action
    action = tf.reduce_sum(tf.multiply(out, argmax), reduction_indices=1)

    #Cost function (reduced by back propogation)
    cost = tf.reduce_mean(tf.square(action - gt))

    #Optimizer
    train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)

    #Initilizes game
    game = pong.Pong()

    #Queue to store replays
    D = deque()

    #Starting frame
    frame = game.getPresentFrame()

    #Stack frames to form the input tensor
    inp_t = np.stack((frame, frame, frame, frame), axis=2)

    #Saves the data
    saver = tf.train.Saver()

    sess.run(tf.global_variables_initializer())

    t = 0
    epsilon = INITIAL_EPSILON

    count = -1

    try:
        saver.restore(sess,'./pong_weights.ckpt')
    except:
        print ("oof")
    
    #Training
    while(count<40999):
        count+= 1

        #Output Tensor
        out_t = out.eval(feed_dict={inp: [inp_t]})[0]

        #Argmax
        argmax_t = np.zeros([ACTIONS])

        #Random action, probability affected by epsilon
        if(random.random() <= epsilon):
            maxIndex = random.randrange(ACTIONS)

        #Predicted action with a probability of (1 - epsilon)
        else:
            maxIndex = np.argmax(out_t)
        argmax_t[maxIndex] = 1

        if epsilon > FINAL_EPSILON:
            epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE

        #Reward tensor
        reward_t, frame = game.getNextFrame(argmax_t)

        frame = np.reshape(frame, (INPUT_SIZE, INPUT_SIZE, 1))
        
        #Creates a new input tensor
        inp_t1 = np.append(frame, inp_t[:, :, 0:3], axis=2)

        #Adds input tensor, argmax, reward and updated input tensor to memory
        D.append((inp_t, argmax_t, reward_t, inp_t1))

        #Deletes old memory if needed
        if len(D) > REPLAY_MEMORY:
            D.popleft()

        #Training
        if t > OBSERVE:

            #Get replay values
            minibatch = random.sample(D, BATCH)

            inp_batch = [d[0] for d in minibatch]
            argmax_batch = [d[1] for d in minibatch]
            reward_batch = [d[2] for d in minibatch]
            inp_t1_batch = [d[3] for d in minibatch]

            gt_batch = []
            out_batch = out.eval(feed_dict={inp: inp_t1_batch})

            #Add values to batch
            for i in range(0, len(minibatch)):
                gt_batch.append(reward_batch[i] + GAMMA * np.max(out_batch[i]))

            #Train on the replay batch
            train_step.run(feed_dict={
                           gt: gt_batch,
                           argmax: argmax_batch,
                           inp: inp_batch
                           })

        #Update input tensor
        inp_t = inp_t1
        t = t+1

        #Print current step
        if t % 10000 == 0:
            saver.save(sess, './pong_weights.ckpt')

        print("TIMESTEP", t, "/ EPSILON", epsilon, "/ ACTION", maxIndex,
              "/ REWARD", reward_t)


def main():
    #Starts TF shell
    shell = tf.InteractiveSession()

    #We get our input and output layers from the model
    inp, out = createModel()

    #We train our model
    trainGraph(inp, out, shell)

if __name__ == "__main__":
    for i in range(1000):
        main()
    main()
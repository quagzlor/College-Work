import math
import matplotlib.pyplot as plt

def sigmoid(value):
    return 1/(1+math.exp(-1*value))

def sigmoid_deriv(value):
    return sigmoid(value)*(1-sigmoid(value))

def plot_graph(x,y):
    plt.plot(x,y)
    plt.xlabel("Epoch")
    plt.ylabel("Error")
    plt.show()

import math
import random
import nn_calcs as nunu

class Layer:
    def __init__(self, neurons):

        self.input_weight=[0]*neurons
        self.output_weight=[0]*neurons
        self.hidden_output=[0]*neurons

        self.bias=[0]*neurons
        self.out_bias=0
        self.out_val=0

        self.hidden_preout_val=[0]*neurons
        self.number_neurons=neurons

    def initialise(self):
        for i in range(self.number_neurons):
            self.input_weight[i]=random.uniform(-0.5,0.5)
            self.output_weight[i]=random.uniform(-0.5,0.5)
            self.bias[i]=random.uniform(-0.5,0.5)

        self.out_bias=random.uniform(-0.5,0.5)

    def predict(self,given_val):

        for i in range(self.number_neurons):
            self.hidden_preout_val[i]=given_val*self.input_weight[i]+self.bias[i]
            self.hidden_output[i]=nunu.sigmoid(self.hidden_preout_val[i])

        self.out_val=self.out_bias

        for i in range(self.number_neurons):
            self.out_val=self.out_val+(self.hidden_output[i]*self.output_weight[i])

        self.final_preout_val=self.out_val
        self.out_val=nunu.sigmoid(self.out_val)

        return self.out_val

    def learn_calc(self, given_val, expected_out, learn_rate):
        actual_out=self.predict(given_val)

        x=(expected_out-actual_out)*nunu.sigmoid_deriv(self.final_preout_val)
        y=[0]*self.number_neurons

        for i in range(self.number_neurons):
            y[i]=x*self.output_weight[i]*nunu.sigmoid_deriv(self.hidden_preout_val[i])
            self.output_weight[i]=self.output_weight[i]+ (learn_rate*x*self.hidden_output[i])
            self.input_weight[i]=self.input_weight[i]+ (learn_rate*y[i]*given_val)
            self.bias[i]=self.bias[i]+(learn_rate*y[i]*given_val)

    def learn(self,given_vals,expected_vals,learn_rate,error_margarine):
        x=0

        for i in range(len(given_vals)):
            x=x+((expected_vals[i]-self.predict(given_vals[i]))**2)

        print (x)

        epoch=0

        x_axis=[]
        y_axis=[]

        while x>error_margarine:
            for i in range(len(given_vals)):
                self.learn_calc(given_vals[i],expected_vals[i],learn_rate)

            x=0

            for i in range(len(given_vals)):
                x=x+((expected_vals[i]-self.predict(given_vals[i]))**2)

            epoch=epoch+1
            
            x_axis.append(epoch)
            y_axis.append(x)
            

            print("Epoch: "+str(epoch) + " Error: " + str(x))
        nunu.plot_graph(x_axis,y_axis)

    def check(self,given_vals,expected_vals):
        error=0

        for i in range(len(given_vals)):
            error=error+((expected_vals[i]-self.predict(given_vals[i]))**2)
        error=error/len(given_vals)

        return error

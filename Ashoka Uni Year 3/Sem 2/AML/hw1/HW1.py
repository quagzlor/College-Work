import numpy as np
import matplotlib.pyplot as plt
import pandas as fluffy
import math

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def read_file(filename):
    file_data = np.array(fluffy.read_csv(filename, sep=" ", header=None))
    split_point = int(file_data.shape[0] - file_data.shape[0]/5)
    training = file_data[:split_point]
    testing = file_data[split_point:]
    
    return training,testing,file_data

def q1():
    training,testing,file_data = read_file('data.txt')

    poly1 = PolynomialFeatures(degree=1)
    poly_1 = poly1.fit_transform(training[:,0:1])

    poly5 = PolynomialFeatures(degree=5)
    poly_5 = poly5.fit_transform(training[:,0:1])

    poly10 = PolynomialFeatures(degree=10)
    poly_10 = poly10.fit_transform(training[:,0:1])

    poly50 = PolynomialFeatures(degree=50)
    poly_50 = poly50.fit_transform(training[:,0:1])

    regressor = LinearRegression()

    plt.scatter(file_data[:,0],file_data[:,1], color = 'blue')

    regressor.fit(poly_1,training[:,1])
    poly_test = poly1.fit_transform(testing[:,0:-1])
    plt.plot(testing[:,0],regressor.predict(poly_test),color = 'red')

    regressor.fit(poly_5,training[:,1])
    poly_test = poly5.fit_transform(testing[:,0:-1])
    plt.plot(testing[:,0],regressor.predict(poly_test),color = 'green')

    regressor.fit(poly_10,training[:,1])
    poly_test = poly10.fit_transform(testing[:,0:-1])
    plt.plot(testing[:,0],regressor.predict(poly_test),color = 'yellow')

    regressor.fit(poly_50,training[:,1])
    poly_test = poly50.fit_transform(testing[:,0:-1])
    plt.plot(testing[:,0],regressor.predict(poly_test),color = 'purple')

    plt.show()

def q2():
    training,testing,file_data = read_file('data.txt')

    poly1 = PolynomialFeatures(degree=1)
    poly_1 = poly1.fit_transform(training[:,0:1])

    poly5 = PolynomialFeatures(degree=5)
    poly_5 = poly5.fit_transform(training[:,0:1])

    poly10 = PolynomialFeatures(degree=10)
    poly_10 = poly10.fit_transform(training[:,0:1])

    poly50 = PolynomialFeatures(degree=50)
    poly_50 = poly50.fit_transform(training[:,0:1])

    regressor = LinearRegression()

    x = [1,5,10,50]
    y = []
    y_test = testing[:,0]

    regressor.fit(poly_1,training[:,1])
    poly_test = poly1.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))
    
    regressor.fit(poly_5,training[:,1])
    poly_test = poly5.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))

    regressor.fit(poly_10,training[:,1])
    poly_test = poly10.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))

    regressor.fit(poly_50,training[:,1])
    poly_test = poly50.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))

    plt.plot(x,y)

    plt.show()

def q3():
    training,testing,file_data = read_file('data.txt')

    poly1 = PolynomialFeatures(degree=1)
    poly_1 = poly1.fit_transform(training[:,0:1])

    poly5 = PolynomialFeatures(degree=5)
    poly_5 = poly5.fit_transform(training[:,0:1])

    poly10 = PolynomialFeatures(degree=10)
    poly_10 = poly10.fit_transform(training[:,0:1])

    poly50 = PolynomialFeatures(degree=50)
    poly_50 = poly50.fit_transform(training[:,0:1])

    regressor = LinearRegression()

    x = [1,5,10,50]
    y = []
    y_test = testing[:,0]

    regressor.fit(poly_1,training[:,1])
    poly_test = poly1.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))
    
    regressor.fit(poly_5,training[:,1])
    poly_test = poly5.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))

    regressor.fit(poly_10,training[:,1])
    poly_test = poly10.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))

    regressor.fit(poly_50,training[:,1])
    poly_test = poly50.fit_transform(testing[:,0:-1])
    y.append(mean_squared_error(y_test,regressor.predict(poly_test)))

    plt.plot(x,y, color = 'red')

    y_Var = [0]*4

    regressor.fit(poly_1,training[:,1])
    poly_test = poly1.fit_transform(testing[:,0:-1])
    predict = regressor.predict(poly_test)
    y_Var[0] = np.var(predict)

    regressor.fit(poly_5,training[:,1])
    poly_test = poly5.fit_transform(testing[:,0:-1])
    predict = regressor.predict(poly_test)
    y_Var[1] = np.var(predict)

    regressor.fit(poly_10,training[:,1])
    poly_test = poly10.fit_transform(testing[:,0:-1])
    predict = regressor.predict(poly_test)
    y_Var[2] = np.var(predict)

    regressor.fit(poly_50,training[:,1])
    poly_test = poly50.fit_transform(testing[:,0:-1])
    predict = regressor.predict(poly_test)
    y_Var[3] = np.var(predict)

    plt.plot(x,y,color = "blue")

    y[0] = y[0] = y_Var[0]
    y[1] = y[1] = y_Var[1]
    y[2] = y[2] = y_Var[2]
    y[3] = y[3] = y_Var[3]

    plt.plot(x,y,color = 'green')

    plt.show()
def q4():
    training,testing,file_data = read_file('data.txt')

    poly1 = PolynomialFeatures(degree=1)
    poly_1 = poly1.fit_transform(training[:,0:1])

    poly5 = PolynomialFeatures(degree=5)
    poly_5 = poly5.fit_transform(training[:,0:1])

    poly10 = PolynomialFeatures(degree=10)
    poly_10 = poly10.fit_transform(training[:,0:1])

    poly50 = PolynomialFeatures(degree=50)
    poly_50 = poly50.fit_transform(training[:,0:1])

    regressor = LinearRegression()

    preds = [0]*4

    regressor.fit(poly_1,training[:,1])
    poly_test = poly1.fit_transform(testing[:,0:-1])
    preds1 = regressor.predict(poly_test)

    regressor.fit(poly_5,training[:,1])
    poly_test = poly5.fit_transform(testing[:,0:-1])
    preds2 = regressor.predict(poly_test)

    regressor.fit(poly_10,training[:,1])
    poly_test = poly10.fit_transform(testing[:,0:-1])
    preds3 = regressor.predict(poly_test)

    regressor.fit(poly_50,training[:,1])
    poly_test = poly50.fit_transform(testing[:,0:-1])
    preds4 = regressor.predict(poly_test)

    big_nums = []

    for i in range(len(preds1)):
        big_nums.append((preds1[i]+preds2[i]+preds3[i]+preds4[i])/4)

    x = np.array(big_nums)
    y = np.array(testing[:,0])

    print (x)
    print (y)

    plt.plot(x,y)
    #plt.scatter(file_data[:,0],file_data[:,1], color = 'blue')
    plt.show()



q1()
q2()
q3()
q4()
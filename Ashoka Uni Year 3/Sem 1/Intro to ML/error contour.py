import matplotlib.pyplot as plt
import numpy as np

def function(w1,w2):
    return (1/2)*((w2-w1)**2 + (1-w1)**2)

def drawcontour(contour_range):
    x=[]
    y=[]
    z=np.ndarray((contour_range*2+1,contour_range*2+1))
    
    for k in range(-1*contour_range,contour_range+1,1):
        x.append(k)
        y.append(k)
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            z[i][j]=function(x[i],y[j])

    plt.contour(x,y,z)
    plt.show()
   

drawcontour(20)

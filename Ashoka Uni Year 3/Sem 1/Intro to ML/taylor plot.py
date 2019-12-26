import matplotlib.pyplot as plt
x = [0,1,2,3,4,5,6,7,8,9]
y1 = []
y2=[]
y3=[]
y4=[]

for i in range(10):
    y1.append(1)
    y2.append(1+i)
    y3.append(1+i+((i*i)/2))
    y4.append(1+i+((i*i)/2)+(((i*i)*i)/6))
    
plt.plot(x,y1,color="red")
plt.plot(x,y2,color="blue")
plt.plot(x,y3,color="green")
plt.plot(x,y4,color="yellow")
plt.axis([0,10,0,y4[9]])
plt.show()

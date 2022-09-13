import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4]#refers to the x axis, [1, 4, 9, 16] #refers to the y axis, 'ro' #the ro means that its red circles)
xaxis = [1,1,2,2,3,8,9]
yaxis = [1,2,2,3,4,8,10]
r = 0
xaxisi = 0
yaxisi = 0
xaxissq = 0
yaxissq = 0

xavg = (sum(xaxis)/len(xaxis))
yavg = (sum(yaxis)/len(yaxis))
for i in range(0,len(xaxis)):
    r = r + ((xaxis[i]-xavg)*(yaxis[i]-yavg))
    xaxisi = xaxisi + (xaxis[i]-xavg)
    yaxisi = yaxisi + (yaxis[i]-yavg)
    xaxissq = xaxissq + ((xaxis[i]-xavg)**2)
    yaxissq = yaxissq + ((yaxis[i]-yavg)**2)

r = r/((yaxissq * xaxissq)**(1/2))
Sy = ((yaxissq)/(len(xaxis)-1))**(1/2)
Sx = ((xaxissq)/(len(xaxis)-1))**(1/2)
m = r * Sy/Sx
c = yavg - m*(xavg)
x = np.linspace(0,100,100)
y = m*x + c
plt.axis([0, 11, 0,11])

plt.plot(xaxis,yaxis,'ro')
plt.plot(x,y)

plt.show()

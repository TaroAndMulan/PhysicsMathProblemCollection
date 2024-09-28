import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

vx=40.0
ts = 0.005
m=10000.0
r=-20.0
u = 1000
vy=0.0
t=0.0
x=0
y=0
xx=[x]
yy=[y]
while (t<10):
    m += r*ts
    dm = -r*ts
    fx = -r*u*vy/math.sqrt(vx**2+vy**2)
    fy = r*u*vx/math.sqrt(vx**2+vy**2)
    ax=fx/m
    ay=fy/m
    vx+=ax*ts
    vy+=ay*ts
    x+=vx*ts
    y+=vy*ts
    xx.append(x)
    yy.append(y)
    t+=ts
plt.plot(xx, yy, color = 'red',label= "t=10s", linewidth=5)
print("m:",m,"v:",math.sqrt(vx**2+vy**2),vx,"|",vy)
print(max(xx),max(yy),min(xx),min(yy))


vx=40.0
ts = 0.01
m=10000.0
r=-20.0
u = 1000
vy=0.0
t=0.0
x=0
y=0
xx=[x]
yy=[y]
while (t<490):
    m += r*ts
    dm = -r*ts
    fx = -r*u*vy/math.sqrt(vx**2+vy**2)
    fy = r*u*vx/math.sqrt(vx**2+vy**2)
    ax=fx/m
    ay=fy/m
    vx+=ax*ts
    vy+=ay*ts
    x+=vx*ts
    y+=vy*ts
    xx.append(x)
    yy.append(y)
    t+=ts
    

print("m:",m,"v:",math.sqrt(vx**2+vy**2),vx,"|",vy)
print(max(xx),max(yy),min(xx),min(yy))

plt.plot(xx, yy, color = 'green',label='t=500s')

leg = plt.legend(loc='upper left')

plt.show()


"""
xxx=[]
yyy=[]
for i in range(len(xx)):
    xxx.append(xx[i])
    yyy.append(yy[i])
  
    # Mention x and y limits to define their range
   
      
    # Ploting graph
    plt.plot(xxx, yyy, color = 'green')
  
plt.show()

"""


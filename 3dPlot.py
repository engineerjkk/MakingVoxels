from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from tqdm import tqdm

with open("points3D.txt") as f:
    points3D = f.read().splitlines() 

def mean(num):
    return sum(num)/len(num)
    
# captture nodes in 2 separate lists
X = []
Y = []
Z = []

for i in tqdm(points3D):
  X.append(i.split(' ')[1])
  Y.append(i.split(' ')[2])
  Z.append(i.split(' ')[3])    

for i in range(0, len(X)):
    X[i] = float(X[i])
for i in range(0, len(Y)):
    Y[i] = float(Y[i])
for i in range(0, len(Z)):
    Z[i] = float(Z[i])


pair=[]
for i in range(len(X)):
    tmp=(X[i],Y[i],Z[i])
    pair.append(tmp)

fig = plt.figure(figsize=(30, 30))
ax = plt.axes(projection='3d')
l=[]
total_count=0
real_count=0
for i in tqdm(range(385,1304,92)):
    for j in range(-60,226,29):
        for k in range(-501,382,89):
            #print(i,j,k)
            x2=[]
            y2=[]
            z2=[]
            for x,y,z in pair:
                if (x>i)&(x<i+92)&(y>j)&(y<j+29)&(z>k)&(z<k+89):
                  x2.append(x)
                  y2.append(y)
                  z2.append(z)
            total_count=total_count+1      
            if len(x2) >=5:
                real_count=real_count+1      
                ax.scatter(x2, y2,z2,s=1, c=np.random.rand(3,))
                ax.text(mean(x2),mean(y2),mean(z2),  '%s' % (str(real_count)), size=10, zorder=1,  color='k') 
print('total_count : ',total_count)
print('real_count : ',real_count)
ax.set_xlim(385,1304)
ax.set_ylim(-60,226)
ax.set_zlim(-501,382)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.view_init(0, 0)
plt.show()
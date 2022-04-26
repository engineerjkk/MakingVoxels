import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data=[]
X, Y, Z = [], [], []
for line in open('3d_centroid_plot.txt', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])
  Z.append(values[2])
pair=[]
for i in range(len(X)):
    tmp=(X[i],Y[i],Z[i])
    pair.append(tmp)

fig = plt.figure(figsize=(30, 30))
ax = plt.axes(projection='3d')
l=[]
for i in range(619,1076,46):
    for j in range(-19,62,9):
        for k in range(-400,187,59):
            #print(i,j,k)
            x2=[]
            y2=[]
            z2=[]
            for x,y,z in pair:
                if (x>i)&(x<i+46)&(y>j)&(y<j+9)&(z>k)&(z<k+59):
                  x2.append(x)
                  y2.append(y)
                  z2.append(z)
                  
            ax.scatter(x2, y2,z2, c=np.random.rand(3,))

ax.set_xlim(619, 1076)
ax.set_ylim(-19, 62)
ax.set_zlim(-400, 187)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
#!python
'''
dissimilarity with numerical values
'''

import scipy.spatial.distance as dist
import pandas as pd
import numpy as np
import math
'''
def Euclidian(x,y):
    
    return diss 

def Manhattan(x,y):
    
    return diss 

def Chebyshev(x,y):
    
    return diss 

def Canberra(x,y):
    
    return diss 
 
def Cosine(x,y):
    
    return diss 
'''    
    
# read the data file
#cars = pd.read_csv('/Users/steph/Dropbox/research/learning/python/myscript/csv/cars.csv',sep=',')
cars = pd.read_csv('../csv/cars.csv',sep=',')
A=np.array(cars.values[:,1:8],dtype=np.float)

# experience the different norms
v1=A[0];v2=A[1]
''' all the numpy norm at
https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
'''
print('my Euclidian dist=%f, the scipy one %f'% (Euclidian(v1,v2), dist.euclidean(v1, v2)))

# the ball arround the first element: 3: horsepower, 4:weight, 5:acceleration
'''
B=A[:,[3,4,5]]
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
v_ref=B[0]

# euclidean 
radius=100.0;xe=[0]*0;ye=[0]*0;ze=[0]*0;
for v in B:
    d=dist.euclidean(v_ref,v)
    if d<radius:
        xe.append(v[0])
        ye.append(v[1])
        ze.append(v[2])

# manhattan
# camberra
# cosine
'''
        
        
'''
fig = plt.figure()
ax = fig.add_subplot(221)
ax.scatter(B[:,0],B[:,1],c='c')
ax.scatter(xe,ye, c='r')
plt.show()
'''

'''
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')
ax.scatter(B[:,0],B[:,1], B[:,2], c='b', marker='.')
ax.scatter(xe, ye, ze, c='r', marker='o')
plt.show()
'''


# find the two closest elements
# compute dissimilarity matrix 	
print('bye')


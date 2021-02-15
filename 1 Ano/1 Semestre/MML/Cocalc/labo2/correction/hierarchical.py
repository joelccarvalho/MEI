#!python
'''
dissimilarity with numerical values
'''

import scipy.spatial.distance as dist
import pandas as pd
import numpy as np
import math

def Euclidian(x,y):
    if x.size!=y.size:
        return(-1)
    z=y-x
    nn=math.sqrt((z**2).sum())
    return nn 

def Manhattan(x,y):
    if x.size!=y.size:
        return(-1)
    z=y-x
    nn=np.fabs(z).sum()
    return nn 

def Chebyshev(x,y):
    if x.size!=y.size:
        return(-1)
    z=y-x
    nn=np.amax(np.fabs(z))
    return nn 

def Canberra(x,y):
    if x.size!=y.size:
        return(-1)
    z=y-x
    numer=np.fabs(z)
    denom=np.fabs(x)+np.fabs(y)
    r=np.true_divide(numer,denom)
    nn=r.sum()
    return nn 
 
def Cosine(x,y):
    if x.size!=y.size:
        return(-1)
    z=y-x
    numer=np.dot(x,y)
    denom=np.linalg.norm(x,2)*np.linalg.norm(y,2)
    nn=1-numer/denom
    return nn 
    
    
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
print('my Manhattan dist=%f, the scipy one %f'% (Manhattan(v1,v2),dist.cityblock(v1, v2)))
print('my Chebyshev dist=%f, the scipy one %f'% (Chebyshev(v1,v2),dist.chebyshev(v1, v2)))
print('my Canberra dist=%f, the scipy one %f'% (Canberra(v1,v2),dist.canberra(v1, v2)))
print('my cosine dist=%e, the scipy one %e'% (Cosine(v1,v2),dist.cosine(v1, v2)))

# the ball arround the first element 
# 3: horsepower, 4:weight, 5:acceleration
B=A[:,[3,4,5]]
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
v_ref=B[0]

radius=100.0;xe=[0]*0;ye=[0]*0;ze=[0]*0;
for v in B:
    d=dist.euclidean(v_ref,v)
    if d<radius:
        xe.append(v[0])
        ye.append(v[1])
        ze.append(v[2])

radius=100.0;xm=[0]*0;ym=[0]*0;zm=[0]*0;
for v in B:
    d=dist.cityblock(v_ref,v)
    if d<radius:
        xm.append(v[0])
        ym.append(v[1])
        zm.append(v[2])
        
radius=0.2;xc=[0]*0;yc=[0]*0;zc=[0]*0;
for v in B:
    d=dist.canberra(v_ref,v)
    if d<radius:
        xc.append(v[0])
        yc.append(v[1])
        zc.append(v[2])       

radius=0.00001;xcs=[0]*0;ycs=[0]*0;zcs=[0]*0;
for v in B:
    d=dist.cosine(v_ref,v)
    if d<radius:
        xcs.append(v[0])
        ycs.append(v[1])
        zcs.append(v[2])
        
        
'''
fig = plt.figure()
ax = fig.add_subplot(221)
ax.scatter(B[:,0],B[:,1],c='c')
ax.scatter(xe,ye, c='r')
ax = fig.add_subplot(222)
ax.scatter(B[:,0],B[:,1],c='c')
ax.scatter(xm,ym, c='r')
ax = fig.add_subplot(223)
ax.scatter(B[:,0],B[:,1],c='c')
ax.scatter(xc,yc, c='r')
ax = fig.add_subplot(224)
ax.scatter(B[:,0],B[:,1],c='c')
ax.scatter(xcs,ycs, c='r')
plt.show()
'''

'''
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')
ax.scatter(B[:,0],B[:,1], B[:,2], c='b', marker='.')
ax.scatter(xe, ye, ze, c='r', marker='o')
ax = fig.add_subplot(222, projection='3d')
ax.scatter(B[:,0],B[:,1], B[:,2], c='b', marker='.')
ax.scatter(xm, ym, zm, c='r', marker='o')
ax = fig.add_subplot(223, projection='3d')
ax.scatter(B[:,0],B[:,1], B[:,2], c='b', marker='.')
ax.scatter(xc, yc, zc, c='r', marker='o')
ax = fig.add_subplot(224, projection='3d')
ax.scatter(B[:,0],B[:,1], B[:,2], c='b', marker='.')
ax.scatter(xcs, ycs, zcs, c='r', marker='o')
plt.show()
'''


# find the two closest elements
# compute dissimilarity matrix 	
print('bye')


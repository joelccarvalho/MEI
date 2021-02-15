#!python
'''
dissimilarity with category values
'''

#import scipy.spatial.distance as dist
import pandas as pd
import numpy as np
import statistics as stat 

def distance_Hamming(x,y):

    return s
    
def distance_weighted_Hamming(x,y,weight):

    return s     
       
def find_medoid(L,weight):
    
    return medoid 

def find_mode(LT):

    return mode

'''
0. "p,e" 2 items
1. "b,c,x,f,k,s" 6 items
2. "f,g,y,s" 4 items
3. "n,b,c,g,r,p,u,e,w,y" 10 items
4. "t,f" 2 items
5. "a,l,c,y,f,m,n,p,s" 9 items
6. "a,d,f,n" 4 items
7. "c,w,d" 3 items
8. "b,n" 2 items
9. "k,n,b,h,g,r,o,p,u,e,w,y" 12 items
10. "e,t" 2 items
11. "b,c,u,e,z,r,?" 6 items
12. "f,y,k,s" 4 items
13. "f,y,k,s" 4 items
14. "n,b,c,g,o,p,e,w,y" 9 items
15. "n,b,c,g,o,p,e,w,y" 9 items
16. "p,u" 2 items
17. "n,o,w,y" 4 items
18. "n,o,t" 3 items
19. "c,e,f,l,n,p,s,z" 8 items
20. "k,n,b,h,r,o,u,w,y" 9 items
21. "a,c,n,s,v,y" 6 items
22. "g,l,m,p,u,w,d" 7 items
Missing Attribute "?" items
'''
 
# read the data file in dataframe
mushroom = pd.read_csv('/Users/steph/Dropbox/research/learning/python/myscript/csv/mushroom.csv',sep=',')
A=mushroom.values
AT=np.transpose(A)
L=A.tolist()
LT=AT.tolist()
nbitem=np.array([2,6,4,10,2,9,4,3,2,12,2,6,4,4,9,9,2,4,3,8,9,6,7])  
weight=1./nbitem
v1=L[0];v2=L[1]
a=distance_Hamming(v1,v2)
b=distance_weighted_Hamming(v1,v2,nbitem)
c=distance_weighted_Hamming(v1,v2,weight)
print(a,b,c)
# find the medoid
medoid=find_medoid(L[:100],weight)
print(medoid)
# find the mode 
mode=find_mode(LT)
print(mode)

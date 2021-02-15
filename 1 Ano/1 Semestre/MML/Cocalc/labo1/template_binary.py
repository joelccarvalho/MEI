#!python
''
dissimilarity with binaries values
''

import scipy.spatial.distance as dist
import pandas as pd
import numpy as np


def confusion_matrix(x,y):

    return CM 
   
def matching_distance(CM):
   
    return dist
   
def Dice_distance(CM): 

    return dist
 
def Jaccard_distance(CM):

    return dist

def SokalMichener_distance(CM):

    return dist 

def build_dissimilarity_table(A):    

    return DT
 
'''   
def transitive_closure(M):
    n=M.shape[0]
    for i in range(n):
        for j in range(i+1,n):
            if M[i,j]:
                for k in range(n):
                    if M[i,k]:
                        M[j,k]=1
                        M[k,j]=1
    for i in range(n):
        ii=n-i-1
        for j in range(i+1,n):
            jj=n-j-1
            if M[ii,jj]:       
                for k in range(n):
                    if M[ii,k]:
                        M[jj,k]=1
                        M[k,jj]=1 
    return M


def build_clusters(M):
    i=
    loop1=(i<M.shape[0])
    while loop1:
        j=i+1
        loop2=(j<M.shape[0])
        while loop2:
            if all(M[i]==M[j]):
                M=np.delete(M,j,0)
            else:
                j+=1
            loop2=(j<M.shape[0])
        i+=1
        loop1=(i<M.shape[0])
    return M 
''
# ================  MAIN ============================    
# read the data file    
SCADI = pd.read_csv('/Users/steph/Dropbox/research/learning/python/myscript/csv/SCADI.csv',sep=',')
#SCADI = pd.read_csv('../csv/SCADI.csv',sep=',')
A=np.array(SCADI.values[:,2:-1],dtype='int32')
np.set_printoptions(linewidth=100)

# test the metrics
v1=A[0];v2=A[1]
CM=confusion_matrix(v1,v2)
print("my matching distance=%f, hamming distance %f" % (matching_distance(CM),dist.hamming(v1,v2)))
#


'''
#Build the dissimilary table
DT=build_dissimilarity_table(A)
# build adjacency matrix associated to the threshold 
threshold=0.5;marker=(DT<threshold)
#print("--------------------------");print(marker)
#Close the graphe
marker=transitive_closure(marker)
#print("--------------------------");print(marker)
# build the clusters 
marker=build_clusters(marker)
#print("--------------------------");print(marker)

print("find %d clusters" % marker.shape[0])
for i in range(marker.shape[0]):
    ind=np.array(np.where(marker[i])).flatten()
    print("===============================")
    print("cluster No%d" % i)
    print("elements:",ind)
    classe=SCADI.values[ind,-1].flatten()
    #print(classe)
    my_stat=np.zeros(8, dtype=np.int8)
    for i in classe:
        my_stat[i]+=1
    print("stat:",my_stat[1:8])    
print('bye')
'''   

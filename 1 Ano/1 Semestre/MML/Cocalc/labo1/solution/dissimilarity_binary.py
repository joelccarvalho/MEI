#!python
'''
dissimilarity with binaries values
'''

import scipy.spatial.distance as dist
import pandas as pd
import numpy as np

# convention: C[0,0]=y1y2, C[0,1]=n1y2, C[1,0]=y1n2,C[1,1]=n1n2
def confusion_matrix(x,y):
    if x.size!=y.size:
        return(-1)
    CM=np.array([[0,0], [0,0]])     
    CM[0,0]=(np.multiply(x,y)).sum()
    CM[0,1]=(np.multiply((1-x),y)).sum()
    CM[1,0]=(np.multiply(x,(1-y))).sum()
    CM[1,1]=(np.multiply((1-x),(1-y))).sum()
    return CM 
    
def matching_distance(CM):
    total=CM[0,0]+CM[1,1]+CM[0,1]+CM[1,0]
    dist=(CM[0,1]+CM[1,0])/total
    return dist
    
def Dice_distance(CM): 
    total=2*CM[0,0]+CM[0,1]+CM[1,0]
    dist=(CM[1,0]+CM[0,1])/total
    return dist
  
def Jaccard_distance(CM):
    total=CM[0,0]+CM[0,1]+CM[1,0]
    dist=(CM[1,0]+CM[0,1])/total
    return dist

def SokalMichener_distance(CM):
    total=CM[0,0]+CM[1,1]+2*CM[0,1]+2*CM[1,0]  
    dist=2*(CM[0,1]+CM[1,0])/total
    return dist 

def build_dissimilarity_table(A):    
    i=0
    n=A.shape[0]
    DT=np.zeros((n,n))
    for v1 in A:
        j=0
        for v2 in A:
            CM=confusion_matrix(v1,v2)
            d=Jaccard_distance(CM)
            DT[i,j]=d
            j+=1
        i+=1
    return DT
    
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
    i=0
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
print("my Jaccard distance=%f, Jaccard distance %f" % (Jaccard_distance(CM),dist.jaccard(v1,v2)))
print("my Dice distance %f, Dice distance %f" % (Dice_distance(CM),dist.dice(v1,v2)))
print("my SokalMichener distance %f, SokalMichener distance %f" % (SokalMichener_distance(CM),dist.sokalmichener(v1,v2)))
#
#
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
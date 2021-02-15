#!python
'''
dissimilarity with binaries values
'''

#!python
import scipy.spatial.distance as dist
import pandas as pd
import numpy as np
import os
import math
from PIL import Image
import sys

def confusion_matrix(x,y):
    if x.size!=y.size:
        return(-1)
    CM=np.array([[0,0], [0,0]])
    CM[0,0]=(np.multiply(x,y)).sum()
    CM[0,1]=(np.multiply((1-x),y)).sum()
    CM[1,0]=(np.multiply(x,(1-y))).sum()
    CM[1,1]=(np.multiply((1-x),(1-y))).sum()
    return CM

def RusselRao_similarity(CM):
    total=CM[0,0]+CM[1,1]+CM[0,1]+CM[1,0]
    simil=(CM[0,0])/total
    return simil

def Dice_similarity(CM):
    total=2*CM[0,0]+CM[0,1]+CM[1,0]
    simil=(2*CM[0,0])/total
    return simil

def Jaccard_similarity(CM):
    total=CM[0,0]+CM[0,1]+CM[1,0]
    simil=(CM[0,0])/total
    return simil

def SokalMichener_similarity(CM):
    total=CM[0,0]+CM[1,1]+CM[0,1]+CM[1,0]
    simil=(CM[0,0]+CM[1,1])/total
    return simil


def SokalMichener_distance(CM):
    total=CM[0,0]+CM[1,1]+(CM[0,1]+CM[1,0])
    dist=(CM[0,1]+CM[1,0])/total
    return dist

def Hamming_distance(CM):
    dist=CM[0,1]+CM[1,0]
    return dist


def Euclidean_distance(CM):
    x=CM[0,1]+CM[1,0]
    dist=math.sqrt(x)
    return dist


def Produto_distance(CM):
    x=CM[0,1]*CM[1,0]
    dist=math.sqrt(x)
    return dist

def build_dissimilarity_table(A):
    i=0
    n=A.shape[0] # n de linhas total da matriz n=A.shape[0] = 30
    #print(n)
    DT=np.zeros((n,n)) # cria matriz vazia, com 0, com dimensao do n de linhas de A
    for v1 in A:
        j=0
        for v2 in A:
            CM=confusion_matrix(v1,v2)
            d=SokalMichener_distance(CM)
            DT[i,j]=d
            j+=1
        i+=1
        
    return DT

def transitive_closure(M): # the friends of my friends are my friends
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

directory = "pics/"

new_size = 15

arr = []
i = 0
for filename in os.listdir(directory):
    im = Image.open("pics/"+filename)
    im = im.resize((new_size,new_size), Image.ANTIALIAS)
    #print(i,filename)
    i+=1
    p = []
    for row in range(new_size):
        for col in range(new_size):
            a = im.getpixel((row,col)) # obter pixel
            if a > 0: # se pixel é preto
                a = 1
            p.append(a) # adiciona pixel branco
    p = np.asarray(p)
    arr.append(p)
arr = np.array(arr) # array que contem as imagens em binario, 30 arrays com new_size*new_size de dimensão


# test the metrics
v1=arr[0];v2=arr[1]
CM=confusion_matrix(v1,v2)

#similarity
print("#Similarity")
print("my RusselRao similarity=%f" % (RusselRao_similarity(CM)))
print("my Dice similarity=%f" % (Dice_similarity(CM)))
print("my Jaccard similarity=%f" % (Jaccard_similarity(CM)))
print("my SokalMichener similarity=%f" % (SokalMichener_similarity(CM)))

#distance
print("#Distance")
print("my SokalMichener distance=%f" % (SokalMichener_distance(CM)))
print("my Hamming distance=%f" % (Hamming_distance(CM)))
print("my Euclidean distance=%f" % (Euclidean_distance(CM)))
print("my Produto distance %f" % (Produto_distance(CM)))

#Build the dissimilary table
DT=build_dissimilarity_table(arr)

# build adjacency matrix associated to the threshold 
threshold=0.1; marker=(DT < threshold) # < threshold = 0 & > threshold = 1
#print("--------------------------");print(marker[1])

#Close the graphe
marker=transitive_closure(marker)

# build the clusters 
marker=build_clusters(marker)

print("--------------------------")
print("Numero de linhas | ou | find %d clusters" % marker.shape[0])
for i in range(marker.shape[0]):
    #print(marker[i]) # matriz binária true ou false
    ind = np.array(np.where(marker[i])).flatten()
    if len(ind) > 0:
        print("===============================")
        print("cluster No%d" % i)
        print("posição dos elements |ou| valores true:", ind)

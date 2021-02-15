#!python
'''
dissimilarity with binaries values
'''
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
    n=A.shape[0] # n de linhas total da matriz
    DT=np.zeros((n,n)) # cria matriz vazia, com 0 com dimensao do n de linhas de A
    for v1 in A:

        j=0
        for v2 in A:
            CM=confusion_matrix(v1,v2)
            d=Euclidean_distance(CM)
            DT[i,j]=d
            j+=1
        i+=1
    return DT
    
#Values into Array
arr2 = []

x = np.array([1, 1, 1, 0 , 0, 0, 0 ,0 ,0])
arr2.append(x)

y = np.array([1, 1, 1, 1, 0, 0, 0 ,0 ,0])
arr2.append(y)

z = np.array([0, 0, 0, 1, 1, 1, 1 ,0 ,0])
arr2.append(z)

w = np.array([0, 0, 0, 1, 1, 0, 0 ,0 ,1])
arr2.append(w)

arr2 = np.array(arr2)

# ================  MAIN ============================    
#X with Y
v1=arr2[0];v2=arr2[1]
CM=confusion_matrix(v1,v2)
print("===============================")
print("First Element '%s' With Second Element '%s'" % (v1, v2))
#similarity
print("Similarity")
print("my RusselRao similarity=%f" % (RusselRao_similarity(CM)))
print("my Dice similarity=%f" % (Dice_similarity(CM)))
print("my Jaccard similarity=%f" % (Jaccard_similarity(CM)))
print("my SokalMichener similarity=%f" % (SokalMichener_similarity(CM)))
#distance
print("Distance")
print("my SokalMichener distance=%f" % (SokalMichener_distance(CM)))
print("my Hamming distance=%f" % (Hamming_distance(CM)))
print("my Euclidean distance=%f" % (Euclidean_distance(CM)))
print("my Produto distance %f" % (Produto_distance(CM)))

print("===============================")
#X with Z
v1=arr2[0];v2=arr2[2]
CM=confusion_matrix(v1,v2)
print("First Element '%s' With Third Element '%s'" % (v1, v2))
#similarity
print("Similarity")
print("my RusselRao similarity=%f" % (RusselRao_similarity(CM)))
print("my Dice similarity=%f" % (Dice_similarity(CM)))
print("my Jaccard similarity=%f" % (Jaccard_similarity(CM)))
print("my SokalMichener similarity=%f" % (SokalMichener_similarity(CM)))
#distance
print("Distance")
print("my SokalMichener distance=%f" % (SokalMichener_distance(CM)))
print("my Hamming distance=%f" % (Hamming_distance(CM)))
print("my Euclidean distance=%f" % (Euclidean_distance(CM)))
print("my Produto distance %f" % (Produto_distance(CM)))


print("===============================")
#X with W
v1=arr2[0];v2=arr2[3]
CM=confusion_matrix(v1,v2)
print("First Element '%s' With Fourth Element '%s'" % (v1, v2))
#similarity
print("Similarity")
print("my RusselRao similarity=%f" % (RusselRao_similarity(CM)))
print("my Dice similarity=%f" % (Dice_similarity(CM)))
print("my Jaccard similarity=%f" % (Jaccard_similarity(CM)))
print("my SokalMichener similarity=%f" % (SokalMichener_similarity(CM)))
#distance
print("Distance")
print("my SokalMichener distance=%f" % (SokalMichener_distance(CM)))
print("my Hamming distance=%f" % (Hamming_distance(CM)))
print("my Euclidean distance=%f" % (Euclidean_distance(CM)))
print("my Produto distance %f" % (Produto_distance(CM)))


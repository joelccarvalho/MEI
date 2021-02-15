#!python
'''
partitional clustering
'''

import scipy.spatial.distance as dist
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math



#==================  my functions ================
def my_distance(x,y):
    if x.size!=y.size:
        return(-1)
    #nn=dist.euclidean(x,y)
    #nn=dist.cityblock(x,y)
    #nn=dist.chebyshev(x,y)
    #nn=dist.canberra(x,y)
    nn=dist.cosine(x,y)
    return nn 

def initialise_representative(data,K):
    rep=D[0:K,:]
    #print(rep)
    return rep

def assigment(data,rep,K,N):
    clusters=np.zeros(N,dtype=np.int) 
    for n in range(0,N):
        val_min=1E20
        for k in range(0,K):
            val=my_distance(data[n,:],rep[k,:])
            if(val<val_min):
                val_min=val
                clusters[n]=k
    return clusters

def centroid_mean(data,clusters,K,N):
    rep=data[0:K,:]*0
    nb=np.zeros(K,dtype=np.int) 
    for n in range(0,N):
        k=clusters[n]
        rep[k,:]=rep[k,:]+data[n,:]
        nb[k]=nb[k]+1
    for k in range(0,K):
        rep[k,:]=rep[k,:]/nb[k]
    return rep    
    
#def centroid_median(data,cluster):  
#
#    return representative

#def medoid(data,cluster):
#
#      return representative 

def Error_representative(old_rep,rep,K):
    error=0
    for k in range(0,K):
        error=error+my_distance(old_rep[k,:],rep[k,:])
    #print("the error of the representatives is", error)
    return error    

#def within_clusters(data,rep,clusters,K,N):
# 
#    return Sw         
    
#def between_cluster(rep,K):
#
#    return Sb            
#================== MAIN =====================


   
# ----- read the data file and initialize ------
my_data = pd.read_csv('./xclara.csv',sep=',');D=np.array(my_data.values[0:300,1:3],dtype=np.float)
#print(my_data)
#print("D=", D[0:10,:])
N=D.shape[0]  #number of elements/events
d=D.shape[1]  #number of attribute
K=3 #number of clusters
error=1;ncount=0;n_MAX=200
print('number of event:',N,'. number of attribute:',d,', number of cluster:',K)
rep=initialise_representative(D,K) # -- initialise clustering structure --
old_rep=rep;
# ------- test the assigment and centroid ------
'''
clusters=assigment(D,rep,K,N)
plt.scatter(rep[:, 0],rep[:, 1], c='red', s=200, alpha=0.5);
rep=centroid_mean(D,clusters,K,N) 
plt.scatter(D[:,0],D[:,1],c=clusters,s=50,cmap='viridis')
plt.scatter(rep[:, 0],rep[:, 1], c='black', s=200, alpha=0.5);
plt.show()
error=Error_representative(old_rep,rep,K)
'''
# ------ main loop ------
while ((error>1.E-8) and (ncount<n_MAX)):
    old_rep=rep
    clusters=assigment(D,rep,K,N)
    rep=centroid_mean(D,clusters,K,N) 
    error=Error_representative(old_rep,rep,K)
    ncount=ncount+1
    #print('number of iteration:',ncount, error)
plt.scatter(D[:,0],D[:,1],c=clusters,s=50,cmap='viridis')
plt.scatter(rep[:, 0],rep[:, 1], c='magenta', s=200, alpha=0.5);
plt.show()

# ------ validation -------
'''
Sw=within_clusters(D,rep,clusters,K,N)
Sb=between_cluster(rep,K)
print("max within clusters error",Sw.max())
print("min between clusters error",Sb.min())
print("Clustering index:",Sw.max()/Sb.min())
'''
#------- END ------
print('bye')


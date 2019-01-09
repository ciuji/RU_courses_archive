#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:40:05 2018

@author: ciuji
"""

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.preprocessing import scale
import scipy

images, labels = load_digits(2,return_X_y=True)
#training set
training_images=images[:300]
training_labels=labels[:300]
#test set
test_images=images[300:]
test_labels=labels[300:]

class my_KNN():
    def __init__(self,data,k):
        predict_labels=[]
        train_data=my_pca(training_images,19)
        for i in range(len(test_images)):
            item_label=self.getLabel(train_data,data.prin[i],k)
            predict_labels.append(self.label)
        self.predict_sign = predict_labels^test_labels
        
    def getLabel(self,train_data,point,k):
        norm=np.zeros((300,2))
        norm_list=[]
        for i in range(0,300):
            item=[np.linalg.norm(point-train_data.prin[i]),training_labels[i]]
            norm[i]=item
        sort_data=norm[norm[:,0].argsort()]
        self.sort_data=sort_data
        sign0=0
        sign1=0
        self.label=1
        for i in range(k):
            if(sort_data[i,1]==1):
                sign1+=1
            else:
                sign0+=1
        if(sign0>sign1):
            self.label=0
    def getError(self):
        error=sum(self.predict_sign)/60
        return error

class my_pca:
    def __init__(self,arr,n=0):
        mean_arr=np.mean(arr,axis=0)
        center_arr=mean_arr-arr

        u,s,v=scipy.linalg.svd(center_arr)
        self.u=u
        self.s=s
        
        if(n==0):
            self.n=self.getk(center_arr)
            #print(self.n)
        else:
            self.n=n
        
        max_abs_cols = np.argmax(np.abs(u), axis=0)
        signs = np.sign(u[max_abs_cols, range(u.shape[1])])
        u *= signs
        #v *= signs[:, np.newaxis]
        
        principal_arr=u[:,:self.n]
        principal_arr *= s[:self.n]
        self.prin=principal_arr.copy()
    def getk(self,arr):
        cum_sum=0
        data_energy=np.linalg.norm(arr)**2
        for i in range(len(self.s)):
            cum_sum=cum_sum+self.s[i]**2
            if(cum_sum/data_energy>=0.95):
                return i+1
        
train_pca2=my_pca(training_images,2)
test_pca2=my_pca(test_images,2)
fig=plt.figure()
train_pca0=train_pca2.prin[training_labels==0]
train_pca1=train_pca2.prin[training_labels==1]
trainPrin=train_pca2.prin
# =============================================================================
# plt.scatter(train_pca0[:,0],train_pca0[:,1],c='r',label='digit 0')
# plt.scatter(train_pca1[:,0],train_pca1[:,1],c='g',label='digit 1')
# plt.title("two-dimentional features of training images:")
# fig.legend()
# =============================================================================
plt.scatter(train_pca2.u[:,0],train_pca2.u[:,1])
#plt.scatter(test_pca2.u[:,0],test_pca2.u[:,1])

#plt.show()

from sklearn.datasets import load_digits

# Load data (handwritten images of digit 0)
images, labels = load_digits(1, return_X_y=True)

# Problem 1

# Show an image of digit 0 from the dataset
print('A representative image of digit 0 from the dataset')
#plt.gray() 
#plt.matshow(images[0,:].reshape((8,8)))


# Arranging the dataset so that each data sample is a column in the data matrix
X = images.T

# Computation of the empirical mean of data, both as a vector and as a tiled matrix
mean_vec = (np.sum(X, axis=1))/(X.shape[1])
mean_mat = np.tile(mean_vec.reshape(X.shape[0],1),[1,X.shape[1]])

# Centered data matrix
centered_X = X - mean_mat

U, s, Vh = np.linalg.svd(centered_X)
#plt.scatter(U[:,0],U[:,1],c='r',label='digit 0')

plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:21:16 2018

@author: ciuji
"""

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy.linalg import cholesky

images, labels = load_digits(2,return_X_y=True)
#training set
training_images=images[:300]
training_labels=labels[:300]
#test set
test_images=images[300:]
test_labels=labels[300:]


#use sklearn.decomposition.PCA
from sklearn import decomposition
pca=decomposition.PCA(n_components=2)
pca.fit(training_images)
train_pcaTrans=pca.transform(training_images)
pca.fit(test_images)
test_pcaTrans=pca.transform(test_images)

fig=plt.figure()
plt.scatter(train_pcaTrans[:,0],train_pcaTrans[:,1])
plt.show()

#compare with using sklearn.neighbors.KNeighborsClassifier
#from sklearn.neighbors import KNeighborsClassifier
#neigh=KNeighborsClassifier(n_neighbors=5)
#neigh.fit(train_pcaTrans,training_labels)
#pca.fit(test_images)
#test_pcaTrans=pca.transform(test_images)
#predit_labels=neigh.predict(test_pcaTrans)
#b=np.bitwise_xor(predit_labels,test_labels)
#a=test_images[b==1]

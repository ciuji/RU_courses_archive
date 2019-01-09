#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:43:40 2018

@author: ciuji
"""

from sklearn.datasets import load_digits
images, labels=load_digits(1,return_X_y=True)
import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

mean=np.mean(images,axis=0)

center_arr=images.copy()
center_arr-=mean
u,sigma,v=np.linalg.svd(center_arr.T)
#sigma,u=np.linalg.eig(np.dot(center_arr,center_arr.T))
#sigma,u=np.linalg.eig(np.cov(center_arr))

U=np.matrix(u[[0]])

UUT=np.dot(U.T,U)

trans=center_arr*U.T

recons = trans*U

final=recons.copy()
final += mean 

error1 = np.linalg.norm(final - images)
error= error1**2
print ("the error :",error)
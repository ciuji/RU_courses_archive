#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:54:35 2019

@author: ciuji
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.stats import truncnorm

rcParams['font.family'] = 'Times New Roman'

#%% load data

pathA='ClassA.txt'
pathB='ClassB.txt'
pathM='Mystery.txt'

def readFile(path):
    class_list=[]
    with open(path) as file:
        for line in file:
            newline=line.rstrip('\n').split('\t')
            if newline!=['']*5:
                class_list.append(newline)
    return np.array(class_list).astype('int').reshape((5,5,5))

cA=readFile(pathA)
cB=readFile(pathB)
cM=readFile(pathM)

#%% draw mean
draw=np.zeros((5,5))
for it in cA:
    draw+=it
    
for it in cB:
    draw-=it
plt.figure(figsize=[8,8])
plt.subplot(133)
plt.imshow(draw,cmap='bwr',vmin=-5,vmax=5)
plt.title('Combine')
#plt.axis('off')

plt.subplot(132)
plt.imshow(cB.mean(axis=0),cmap='Blues')
plt.title('Class B')
plt.axis('off')

plt.subplot(131)
plt.imshow(cA.mean(axis=0),cmap='Reds')
plt.title('Class A')

plt.axis('off')

plt.show()

#%% naive bayesian classifier approach


pA1=(cA.sum(axis=0)+1)/6
pB1=(cB.sum(axis=0)+1)/6

def NB_onepoint(point):
    isA=pA1[tuple(point)]
    isB=pB1[tuple(point)]
    #print(isA,isB)
    return isA,isB
    
def NB_oneimage(image):
    point_list=np.argwhere(image==1)
    A_p=[]
    B_p=[]
    for point in point_list:
        tempA,tempB=NB_onepoint(point)
        A_p.append(tempA)
        B_p.append(tempB)
    
    finalA=1
    finalB=1
    for i in range(len(point_list)):
        finalA*=A_p[i]
        finalB*=B_p[i]
    print('likelihood of A:',finalA,'likelihood of B:',finalB)
    if finalA>finalB:
        return 'Class A'
    else:
        return 'Class B'
    
#%% neural-network approach
nn_train_A=cA.reshape((5,25))
nn_train_B=cB.reshape((5,25))
def sigmoid(x):
    return 1 / (1 + np.e ** -x)
activation_function = sigmoid
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
class NeuralNetwork:
    def __init__(self, 
                 no_of_in_nodes, 
                 no_of_out_nodes, 
                 no_of_hidden_nodes,
                 learning_rate,
                ):  
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.error=1
        self.learning_rate = learning_rate 
        self.create_weight_matrices()    
        
    
    def create_weight_matrices(self):  
        rad = 1 / np.sqrt(self.no_of_in_nodes )
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, 
                                       self.no_of_in_nodes ))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes )
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, 
                                        self.no_of_hidden_nodes ))
    
        
    def train(self, input_vector, target_vector):                                    
            
        input_vector = np.array(input_vector, ndmin=2).T
        target_vector = np.array(target_vector, ndmin=2).T
        
        output_vector1 = np.dot(self.weights_in_hidden, input_vector)
        output_vector_hidden = activation_function(output_vector1)        
        output_vector2 = np.dot(self.weights_hidden_out, output_vector_hidden)
        output_vector_network = activation_function(output_vector2)
        output_errors = target_vector -  output_vector_network
        self.error=abs(min(output_errors,self.error))

        tmp = output_errors * (1.0 - output_vector_network)     
        tmp = self.learning_rate  * np.dot(tmp, output_vector_hidden.T)
        self.weights_hidden_out += tmp
        hidden_errors = np.dot(self.weights_hidden_out.T, output_errors)
 
        tmp = hidden_errors * (1- output_vector_hidden**2)
        x = np.dot(tmp, input_vector.T)
        self.weights_in_hidden += self.learning_rate * x        
    
    def run(self, input_vector):
        
        input_vector = np.array(input_vector, ndmin=2).T
        output_vector = np.dot(self.weights_in_hidden, input_vector)
        output_vector = activation_function(output_vector)
        
            
        output_vector = np.dot(self.weights_hidden_out, output_vector)
        output_vector = activation_function(output_vector)
    
        self.predict=output_vector
        return ('class B' if output_vector >=0.5 else  'class A')
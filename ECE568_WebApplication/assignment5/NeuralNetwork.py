#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ECE568: Homework 5 neural network

@author: Chaoji Zuo/190003416
"""

import numpy as np

X=np.array([[0,0],[0,1],[1,0],[1,1]])
Y=[0,1,1,0]

def sigmoid(x):
    return 1/(1+np.exp(-x))

def gradient_sigmoid(x):
    return (1-sigmoid(x))*sigmoid(x)


##init weight
def init_weight():
    
    layer1Weight=np.random.rand(2,3)#*2-1#*2*math.sqrt(6)/math.sqrt(4)-math.sqrt(6)/math.sqrt(4)
    layer2Weight=np.random.rand(1,3)#*2-1#*2/math.sqrt(6)/math.sqrt(3)-math.sqrt(6)/math.sqrt(3)
    return layer1Weight, layer2Weight

class NeuralNetwork:
    def __init__(self,weight1=None,weight2=None):
        self.X=np.array([[0,0],[0,1],[1,0],[1,1]])
        #increment matrix
        self.XX=np.insert(self.X,0,values=1,axis=1)

        self.Y=np.array([0,1,1,0]).reshape(4,1)
        self.epochs=0
        if(weight1 is not None):
            self.weight1=weight1
            self.weight2=weight2
        else:
            self.weight1,self.weight2=init_weight()
        #print("initial weight1:\n",self.weight1,'\ninitial weight2:\n',self.weight2)

    #fit the weight   
    def fit(self,learningRate,target):
        J,grad1,grad2=self.BP()
        #print("the first batch error:\n",J)
        
        while J >= target and 10000>self.epochs:
            J, grad1, grad2 = self.BP()
            self.weight1 = self.weight1 - grad1 * learningRate
            self.weight2 = self.weight2 - grad2 * learningRate
            
            self.epochs+=1
        
        self.finalError=J
        
    #do prediction           
    def predict(self, x):
# =============================================================================
#         x=self.XX
#         layer2input=x@self.weight1.T
#         
#         layer2sigmoid=sigmoid(layer2input)
#         layer2output=np.insert(layer2sigmoid,0,values=1,axis=1)
#         
#         layer3intput=layer2output@self.weight2.T
#         layer3output=sigmoid(layer3intput)
#         
#         return layer3output
# =============================================================================
        if(x==[0,0]):
            print(self.prediction[0])
        elif(x==[0,1]):
            print(self.prediction[1])
        elif(x==[1,0]):
            print(self.prediction[2])
        elif(x==[1,1]):
            print(self.prediction[3])
        
    #Back Propagation        
    def BP(self):
        layer2intput=self.XX @ self.weight1.T
        layer2sigmoid=sigmoid(layer2intput)
        #increment matrix
        layer2output=np.insert(layer2sigmoid,0,values=1,axis=1)
        
        layer3intput = layer2output@self.weight2.T
        layer3output = sigmoid(layer3intput)
        
        self.prediction=layer3output
        # use cross entropy
        crossEntropy = np.sum(np.log(layer3output)*self.Y+(1-self.Y)*np.log(1-layer3output))
        J=-crossEntropy/4
        
        # use mean square error
        J=np.sum((self.Y-layer3output)**2)/2
        delta3 = layer3output - self.Y

        delta2 = (delta3 * self.weight2)[:, 2:] * gradient_sigmoid(layer2intput)
    
        delta1 = delta2.T@self.XX
        delta2 = delta3.T@layer2output
        
        grad_weight1 = delta1 
        grad_weight2 = delta2 
        return J, grad_weight1, grad_weight2
        
#%% learning rate = 0.5 and 1.0
    
nn=NeuralNetwork()
nn.fit(0.84,0.1)

print("final weight1:\n",nn.weight1,'\nfinal weight2:\n',nn.weight2)
print("final error:",nn.finalError)
print("total number of batch:",nn.epochs)


#%% best case
'''
lrlist=np.linspace(0,1,20)

weight1,weight2=init_weight()

for i in lrlist:
    nn=NeuralNetwork(weight1,weight2)
    nn.fit(i,0.02)
    print("learning rate:",round(i,2),"total number of batch:",nn.epochs)
    '''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:23:55 2019

@author: ciuji
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

datapath="AAPL.csv"
df=pd.read_csv(datapath)

class CurveFitting:
    def __init__ (self,Alpha=5e-3,Beta=11.1,M=5):
        #using the parameters from the book PRML
        self.Alpha=Alpha
        self.Beta=Beta
        self.M=M
        self.mu=0
        self.S=None
        self.phi_x=None
        
    
    def get_phi(self,x):
        phi=np.array([x**i for i in range(self.M + 1)])
        return phi.reshape((len(phi),1))
    
    def get_S(self):
        sum_s=0
        #formula (1.72) from PRML
        for i in range(self.N):
            sum_s+=self.get_phi(self.X_train[i])@self.phi_x.T
        S_I=self.Alpha * np.identity(self.M+1) + self.Beta*sum_s
        return np.matrix(S_I).I
    
    def get_var(self):
        #formual (1.71) from PRML
        return 1/self.Beta+self.phi_x.T@self.S@self.phi_x
    
    def get_mean(self):
        sum_m=np.zeros((self.M+1,1))
        # formual (1.70) from PRML
        for i in range(self.N):
            sum_m+=self.get_phi(self.X_train[i])*self.Y_train[i]
        return self.Beta*self.phi_x.T@self.S@sum_m
    
    def fit(self,X,Y):
        self.X_all=X
        self.Y_all=Y
        self.y_test=Y[-1]
        self.x_test=X[-1]
        self.X_train=X[:-1]
        self.Y_train=Y[:-1]
        
        self.N=len(self.X_train)
        self.phi_x=self.get_phi(self.x_test)
        self.S=self.get_S()
        self.var=np.array(self.get_var())[0][0]
        self.mu=np.array(self.get_mean())[0][0]
        self.abs_error=abs(self.mu-self.y_test)
        self.rel_error=self.abs_error/self.y_test
        if (self.abs_error>=30 and self.M<14):
            self.M+=1
            return (self.fit(X,Y))
        else:
            return (self.mu)

        
    def draw(self):
        plt.figure()
        plt.plot(self.X_all,self.Y_all,c='g')
        plt.scatter(self.X_all,self.Y_all,c='b',label='true value')
        plt.scatter(self.x_test,self.mu,c='r',label='predict value')
        plt.legend()
        plt.show()
        

#%%predict 10 times

def predict10times():
    startpointslist=np.random.choice(range(0,len(df)-11),size=10)
    
    abserrorlist=[]
    relerrorlist=[]
    for i in startpointslist:
        cf=CurveFitting()
        x=list(range(0,11,1))
        y=list(df['Close'][i:i+11])
        try:
            cf.fit(x,y)
        except:
            print("S is singular matrix, try another day")
            y=list(df['Close'][i+1:i+12])
            cf.fit(x,y)
        #print(cf.M)
        abserrorlist.append(cf.abs_error)
        relerrorlist.append(cf.rel_error)
    print("10 predicted days:",startpointslist+10)
    print("absolute errors:",(np.array(abserrorlist)*100).astype('int')/100)
    print("realtive errors:",(np.array(relerrorlist)*100).astype('int')/100)
    print("mean absolute error:",np.mean(abserrorlist))
    print("mean relative error:",np.mean(relerrorlist))

#%% main
if __name__ == '__main__':
    
    datapath="AAPL.csv"
    df=pd.read_csv(datapath)
    if(len(sys.argv)==2):
        predict10times()
    else:
        x=list(range(0,11,1))
        cf=CurveFitting()
        y=list(df['Close'][:11])
        res=cf.fit(x,y)  
        print ("absoluate error:",int(cf.abs_error*1000)/1000) 
        print ("relative error:",int(cf.rel_error*1000)/1000) 
        cf.draw()

    
      
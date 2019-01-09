#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:29:48 2018

@author: ciuji
"""

from sympy import *
import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import display,Latex

i=0
w1,w2,f_w,s_s=symbols('w1 w2 f_w s_s')#s=step_size
W_00=np.array([0,-4])
f_w =(w1**2+ w2-11)**2 + (w1+w2**2-7)**2
k=0.01
iteration=0

class func_grad:
    def __init__(self,i,W_0,k):
        X=[]
        Y=[]
        while(i<10000):
            X.append(W_0[0])
            Y.append(W_0[1])
            grad_w1=diff(f_w,w1).subs([(w1,W_0[0]),(w2,W_0[1])])
            grad_w2=diff(f_w,w2).subs([(w1,W_0[0]),(w2,W_0[1])])
            p=-np.array([grad_w1,grad_w2],dtype='float64')

            W_1=p*k+W_0
        #        print (W_1[0],W_1[1],f_w.subs([(w1,W_1[0]),(w2,W_1[1])]).evalf())#look the output        
            if (np.linalg.norm(p)**2<10**-12):
                self.W=(W_1[0],W_1[1])
                self.Z=f_w.subs([(w1,W_1[0]),(w2,W_1[1])]).evalf()
                self.X=X
                self.Y=Y
                self.i=i
                break;
            i+=1
            W_0=W_1
            
a=func_grad(i,[0,-4],0.01)
b=func_grad(i,[0.5,-4],0.01)
c=func_grad(i,[0,4],0.01)
d=func_grad(i,[0.5,4],0.01)

def draw_plt(data,name=''):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)
    X,Y = np.meshgrid(x,y)
    Z=(X**2+ Y-11)**2 + (X+Y**2-7)**2
    ax.contourf(X,Y,Z)
    ax.contour(X,Y,Z)
    X=np.array(data.X)
    Y=np.array(data.Y)
    plt.plot(X,Y, (X**2+ Y-11)**2 + (X+Y**2-7)**2,c='r',lw='5',label=name)
    ax.legend()
    ax.view_init(60,35) 
    plt.show()

draw_plt(a,'a')           
draw_plt(b,'b')           
draw_plt(c,'c')           

draw_plt(d,'d')           

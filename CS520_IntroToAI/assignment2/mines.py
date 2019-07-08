#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:39:45 2019

@author: ciuji
"""

import numpy as np
import matplotlib.pyplot as plt
import random

class MineGenerator:
    def __init__(self,x=10,y=10,p=0.1):
        self.x=x
        self.y=y
        self.p=p
        self.generateboard()
        
    def generatemines(self):
        x=self.x;y=self.y;p=self.p
        arr=np.zeros(x*y)
        if(p<1):
            num = int(x*y*p)
        else:
            num=p
        mines=np.random.choice(range(x*y),size=num,replace=False)
        for i in mines:
            arr[i]=-1
            
        board=np.array(arr).reshape((x,y))
        return board
    
    def generatetips(self,board):
        x=board.shape[0]
        y=board.shape[1]
        bigboard=np.zeros((x+2,y+2))
        bigboard[1:x+1,1:y+1]=board
        mineIndices= np.argwhere(bigboard==-1)
        for i,j in mineIndices:
            for m in range(-1,2):
                for n in range(-1,2):
                    if bigboard[i+m,j+n]==-1:
                        continue
                    else:
                        bigboard[i+m,j+n]+=1
                        #bigboard[i+m,j+n]+=random.randint(0,1)
        board=bigboard[1:x+1,1:y+1]
        return board
        
    def drawboard(self,originalboard=None):
        if originalboard is None:
            board=self.board.copy()
        else:
            board=originalboard.copy()
        board[board==-1]=-5
        board[board==-2]=-12
        if((board!=-2).all()==True):
            board[board==-1]=-2
            #board[board>0]=11
            board[board==0]=0


        plt.figure(figsize=(5,5))
        plt.pcolor(-board[::-1],edgecolors='black',cmap='bwr', linewidths=2)
        plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.show()     
            
    def generateboard(self):
        board=self.generatemines()
        board=self.generatetips(board)
        self.board=board

'''example        
ms=MineGenerator(p=0.14)
print(ms.board)
ms.drawboard()    
'''
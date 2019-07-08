#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:49:44 2019

@author: Chaoji
"""

import numpy as np
import matplotlib.pyplot as plt
import random

class Maze:

    def __init__(self):
        self.mazeMap=np.zeros((10,10),dtype=int)
        self.dim=0
        self.p=0

    #generate a new maze map
    def generateMaze(self,dim=10,p=0.3):
        mazeMap=np.zeros((int(dim)+2,int(dim)+2),dtype=int)
        self.dim=dim
        self.p=p
        mazeMap[0,:]=mazeMap[-1,:]=mazeMap[:,0]=mazeMap[:,-1]=2
        mazeMap[1,1]=1
        mazeMap[dim,dim]=1
        barrier=int(dim*dim*p)
        amount=dim*dim
        
        ranList=list(range(1,amount-2))
        random.shuffle(ranList)
        choList=[]
        for i in ranList:
            barrier-=1
            a=i
            choList.append(a)
            b=a//dim
            c=a%dim
            mazeMap[b+1,c+1]=2
            if(barrier<=0):
                break
    
        self.mazeMap=mazeMap
        return mazeMap
    

    #draw a maze
    def drawMaze(self,maze=None):
        if maze is not None:
            drawMap=maze
        else:
            drawMap=self.mazeMap
            
        plt.figure(figsize=(5,5))
        plt.pcolor(drawMap[::-1],edgecolors='black',cmap='Blues', linewidths=2)
        plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.show()
        
    
    #print the array of maze    
    def printMaze(self,maze=None):
        if maze is not None:
            printMap=maze
        else:
            printMap=self.mazeMap
        print (printMap)

'''example        
mazeMap=Maze()       
mazeMap.generateMaze(10,0.3)    
mazeMap.drawMaze()
#'''



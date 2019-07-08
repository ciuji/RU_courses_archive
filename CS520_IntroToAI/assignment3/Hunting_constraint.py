#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:45:16 2019

@author: ciuji
"""
# calculate move

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
class TerrainMap:
    def __init__(self, size=50):
        self.size = size;
        self.generateMap()
        self.target=tuple(np.random.choice(size,size=2))
        self.type=self.t_map[self.target]
        
    def generateMap(self):
        #generate different terrain, 1--flat,2--hilly,3--forested,4--maze of caves
        terrain_choices=np.random.choice([1,2,3,4],p=[0.2,0.3,0.3,0.2],size=self.size**2)
        self.t_map=terrain_choices.reshape((self.size,self.size))
        
        
    def printMap(self):

        plt.figure(figsize=(10,10))
        plt.pcolor(-self.t_map[::-1],edgecolors='black',cmap='gist_earth', linewidths=2)
        plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.show()
    
    def moveTarget(self):
        moveDirection=np.random.choice(4)
        temp=self.target
        if(moveDirection==0):
            self.target=(self.target[0]-1,self.target[1])
        elif(moveDirection==1):
            self.target=(self.target[0]+1,self.target[1])
        elif(moveDirection==2):
            self.target=(self.target[0],self.target[1]-1)
        elif(moveDirection==3):
            self.target=(self.target[0],self.target[1]+1)
        try:
            self.type = self.t_map[self.target];return
        except:
            self.target=temp
            self.moveTarget()
        
class HuntingConstrain:
    def __init__(self,terrainMap=TerrainMap()):
        terrainMap=TerrainMap(size=50)
        self.terrain=terrainMap
        self.t_map=terrainMap.t_map
        self.p_map1=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map2=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map3=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)

        self.FN=[0,0.1,0.3,0.7,0.9]
    
    def checkOneGrid(self,grid):
        if(grid!=self.terrain.target):
            return False
        else:
            choice=np.random.uniform()
            gridType=self.t_map[grid]
            return (choice>=self.FN[gridType])
    
    def randomPickGrid(self):
        #random choice
        candidateList=np.argwhere(self.p_map1==self.p_map1.max())
        return tuple(candidateList[np.random.choice(len(candidateList))])
    
    
    def terrainPickGrid(self):
        arr4=np.argwhere((self.t_map==4) & (self.p_map2==self.p_map2.max()) )
        arr3=np.argwhere((self.t_map==3) & (self.p_map2==self.p_map2.max()) )
        arr2=np.argwhere((self.t_map==2) & (self.p_map2==self.p_map2.max()) )
        arr1=np.argwhere((self.t_map==1) & (self.p_map2==self.p_map2.max()) )
        candidateList=arr4
        if (arr4.size>0):
            candidateList=arr4
        if(arr3.size>0):
            candidateList=arr3
        if(arr2.size>0):
            candidateList=arr2
        if(arr1.size>0):
            candidateList=arr1
        return tuple(candidateList[np.random.choice(len(candidateList))])           

    def canstriantPickGrid(self,lastGrid):
        arr4=np.argwhere((self.t_map==4) & (self.p_map3==self.p_map3.max()) )
        arr3=np.argwhere((self.t_map==3) & (self.p_map3==self.p_map3.max()) )
        arr2=np.argwhere((self.t_map==2) & (self.p_map3==self.p_map3.max()) )
        arr1=np.argwhere((self.t_map==1) & (self.p_map3==self.p_map3.max()) )
        candidateList=arr4
        if (arr4.size>0):
            candidateList=arr4
        if(arr3.size>0):
            candidateList=arr3
        if(arr2.size>0):
            candidateList=arr2
        if(arr1.size>0):
            candidateList=arr1    
        c1=abs(candidateList-lastGrid)
        c2=c1.sum(axis=1)
        minPos=np.argmin(c2)
        return tuple(candidateList[minPos])
     
    def getDistance(self,p,q):
        return abs(p[0]-q[0])+abs(p[1]-q[1])
                   
                
    def stationarySearch1(self):
        self.rule1count=0
        self.rule1move=0
        lastGrid=None
        while(True):
            curGrid=self.randomPickGrid()
            if(self.rule1count==0):
                lastGrid=curGrid
            self.rule1count+=1
            self.rule1move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            else:
                denominator=1-self.p_map1[curGrid]+self.p_map1[curGrid]*self.FN[self.t_map[curGrid]]
                self.p_map1[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map1/=denominator
            lastGrid=curGrid

        return self.rule1count
    
    def stationarySearch2(self):
        self.rule2count=0
        self.rule2move=0
        lastGrid=0
        while(True):
            print("belief at Time:",self.rule2count)
            print(self.p_map2)
            curGrid=self.terrainPickGrid()
            if(self.rule2count==0):
                lastGrid=curGrid
            self.rule2count+=1
            self.rule2move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            else:
                denominator=1-self.p_map2[curGrid]+self.p_map2[curGrid]*self.FN[self.t_map[curGrid]]
                self.p_map2[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map2/=denominator
            lastGrid=curGrid
        return self.rule2count        
    
    def stationaryConstraintSearch(self):
        self.rule3count=0
        self.rule3move=0
        curGrid=self.terrainPickGrid()
        lastGrid=curGrid
        while(True):
            curGrid=self.canstriantPickGrid(lastGrid)
            self.rule3count+=1
            self.rule3move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            else:
                denominator=1-self.p_map3[curGrid]+self.p_map3[curGrid]*self.FN[self.t_map[curGrid]]
                self.p_map3[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map3/=denominator
            lastGrid=curGrid
        return self.rule3count   
    

    
'''
s1=[]
m1=[]
s2=[]
m2=[]
s3=[]
m3=[]
for j in range(100):
    b=HuntingConstrain()
    s1.append(b.stationarySearch1())
    m1.append(b.rule1move)
    s2.append(b.stationarySearch2())
    m2.append(b.rule2move)
    s3.append(b.stationaryConstraintSearch())
    m3.append(b.rule3move)   ''' 
'''
b=HuntingConstrain()

print('rule1 steps:',b.stationarySearch1())
print('rule1 moves:',b.rule1move)

print('rule2 steps:',b.stationarySearch2())
print('rule2 moves:',b.rule2move)
print('rule3 steps:',b.stationaryConstraintSearch())
print('rule3 moves:',b.rule3move)
'''
b=HuntingConstrain()
b.stationarySearch1()
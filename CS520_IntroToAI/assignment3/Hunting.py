#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:45:16 2019

@author: ciuji
"""

import numpy as np
import matplotlib.pyplot as plt

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
        if(moveDirection==0):
            try:
                self.target=(self.target[0]-1,self.target[1])
            except:
                self.targetMove();return
        elif(moveDirection==1):
            try:
                self.target=(self.target[0]+1,self.target[1])
            except:
                self.targetMove();return
        elif(moveDirection==2):
            try:
                self.target=(self.target[0],self.target[1]-1)
            except:
                self.targetMove();return
        elif(moveDirection==3):
            try:
                self.target=(self.target[0],self.target[1]+1)
            except:
                self.targetMove();return
        self.type = self.t_map[self.target]
        
class Hunting:
    def __init__(self,terrainMap=TerrainMap()):
        terrainMap=TerrainMap()
        self.terrain=terrainMap
        self.t_map=terrainMap.t_map
        self.p_map1=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map2=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        
        self.FN=[0,0.1,0.3,0.7,0.9]
    
    def checkOneGrid(self,grid):
        if(grid!=self.terrain.target):
            return False
        else:
            choice=np.random.uniform()
            gridType=self.t_map[grid]
            #print(grid,gridType)
            #print(choice>=self.FN[gridType])
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
                
                
    def stationarySearch1(self):
        self.rule1count=0
        while(True):
            self.rule1count+=1
            curGrid=self.randomPickGrid()
            if(self.checkOneGrid(curGrid)):
                break;
            else:
                denominator=1-self.p_map1[curGrid]+self.p_map1[curGrid]*self.FN[self.t_map[curGrid]]
                self.p_map1[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map1/=denominator

        return self.rule1count
    
    def stationarySearch2(self):
        self.rule2count=0
        while(True):
            self.rule2count+=1
            curGrid=self.terrainPickGrid()
            if(self.checkOneGrid(curGrid)):
                break;
            else:
                denominator=1-self.p_map2[curGrid]+self.p_map2[curGrid]*self.FN[self.t_map[curGrid]]
                self.p_map2[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map2/=denominator
        #print(self.t_map[curGrid])
        #print(self.rule2count)
        return self.rule2count        
'''
i=0
for j in range(50):
    b=Hunting()
    res=b.stationarySearch2()
    i+=res
    print(res)
print(i/50)
'''
b=Hunting()
print(b.stationarySearch1())
print(b.stationarySearch2())

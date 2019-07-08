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
            self.target=(abs(self.target[0]-1),abs(self.target[1]))
        elif(moveDirection==1):
            self.target=(abs(self.target[0]+1),abs(self.target[1]))
        elif(moveDirection==2):
            self.target=(abs(self.target[0]),abs(self.target[1]-1))
        elif(moveDirection==3):
            self.target=(abs(self.target[0]),abs(self.target[1]+1))
        try:
            self.type = self.t_map[self.target];return
        except:
            self.target=temp
            self.moveTarget()
        
class MovingHunting:
    def __init__(self,terrainMap=TerrainMap()):
        terrainMap=TerrainMap(size=6)
        self.terrain=terrainMap
        self.t_map=terrainMap.t_map
        self.p_map1=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map2=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map3=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.generateNeighborTable()
        self.FN=[0,0.1,0.3,0.7,0.9]
    
    def generateNeighborTable(self):
        a=self.t_map
        size=self.terrain.size
        b=np.zeros((size+2,size+2))
        b[1:size+1,1:size+1]=a
        c=[]
        for i in range(1,size+1):
            for j in range(1,size+1):
                single=[]
                single.append(b[i][j])
                single.append(b[i-1][j])
                single.append(b[i+1][j])
                single.append(b[i][j-1])
                single.append(b[i][j+1])
                c.append(single)
        #neighbor table        
        self.n_table=c

    
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
    
    def movingRandomPickGrid(self):
        candidateList=np.argwhere((self.p_map1==self.p_map1.max()) & ((self.t_map==self.s1t1)|(self.t_map==self.s1t2)))
        try:
            res=tuple(candidateList[np.random.choice(len(candidateList))])
        except:
            return self.randomPickGrid()
        index=res[0]*self.terrain.size+res[1]
        if((self.s1t1==self.n_table[index][0]) &(self.s1t2 in self.n_table[index][1:]))\
        |((self.s1t2==self.n_table[index][0]) &(self.s1t1 in self.n_table[index][1:])):
            print(self.n_table[index])
            print(self.s1t1,self.s1t2)
            return res
        else:
            self.p_map1[res]=0
            return self.movingRandomPickGrid()

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
    
    def movingTerrainPickGrid(self):
        arr4=np.argwhere((self.t_map==4) & (self.p_map2==self.p_map2.max()) )
        arr3=np.argwhere((self.t_map==3) & (self.p_map2==self.p_map2.max()) )
        arr2=np.argwhere((self.t_map==2) & (self.p_map2==self.p_map2.max()) )
        arr1=np.argwhere((self.t_map==1) & (self.p_map2==self.p_map2.max()) )
        candidateList=arr4
        if (arr4.size>0 & ((self.s2t1==4) or (self.s2t2==4)) ):
            candidateList=arr4
        if(arr3.size>0 & ((self.s2t1==3) or (self.s2t2==3)) ):
            candidateList=arr3
        if(arr2.size>0 & ((self.s2t1==2) or (self.s2t2==2)) ):
            candidateList=arr2
        if(arr1.size>0 & ((self.s2t1==1) or (self.s2t2==1)) ):
            candidateList=arr1
        res=tuple(candidateList[np.random.choice(len(candidateList))])          
        index=res[0]*self.terrain.size+res[1]
        #if(self.s2t1 in self.n_table[index]) &(self.s2t2 in self.n_table[index]):
            #print(self.p_map2[self.terrain.target])
        if((self.s2t1==self.n_table[index][0]) &(self.s2t2 in self.n_table[index][1:]))\
        |((self.s2t2==self.n_table[index][0]) &(self.s2t1 in self.n_table[index][1:])):
            return res
        else:
            self.p_map2[res]=0
            return self.movingTerrainPickGrid()
            

    
    def movingCanstriantPickGrid(self,lastGrid):
        '''arr4=np.argwhere((self.t_map==4) & (self.p_map3==self.p_map3.max()) )
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
            candidateList=arr1'''
        candidateList=np.argwhere((self.p_map3==self.p_map3.max()) & ((self.t_map==self.s3t1)|(self.t_map==self.s3t2)))
        c1=abs(candidateList-lastGrid)
        c2=c1.sum(axis=1)
        sortIndex=sorted(range(len(c2)), key=lambda k: c2[k])
        for order in sortIndex:
            res=tuple(candidateList[order])
            index=res[0]*self.terrain.size+res[1]
            #if(self.s3t1 in self.n_table[index]) &(self.s3t2 in self.n_table[index]):
                #print(res,self.terrain.type,self.n_table[index])
            if((self.s3t1==self.n_table[index][0]) &(self.s3t2 in self.n_table[index][1:]))\
            |((self.s3t2==self.n_table[index][0]) &(self.s3t1 in self.n_table[index][1:])):
                return res
            else:
                self.p_map3[res]=0
                return self.movingCanstriantPickGrid(lastGrid)

                 
    def getDistance(self,p,q):
        return abs(p[0]-q[0])+abs(p[1]-q[1])
                   
                
    
    def movingSearch1(self):
        self.rule1count=0
        self.rule1move=0
        lastGrid=self.randomPickGrid()
        self.s1t1=self.terrain.type
        self.terrain.moveTarget()
        rate=1.0
        while(True):
            self.s1t2=self.terrain.type
            total=np.count_nonzero(self.t_map==self.s1t1)+np.count_nonzero(self.t_map==self.s1t2)
            self.p_map1-=self.p_map1*rate
            self.p_map1[self.t_map==self.s1t1]+=rate/total
            self.p_map1[self.t_map==self.s1t2]+=rate/total
            curGrid=self.movingRandomPickGrid()
            #print(self.p_map1[self.terrain.target])
            self.rule1count+=1
            self.rule1move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;

            lastGrid=curGrid
            self.s1t1=self.s1t2
            self.terrain.moveTarget()
            
        return self.rule1count
    
    def movingSearch2(self):
        self.rule2count=0
        self.rule2move=0
        lastGrid=self.terrainPickGrid()
        self.s2t1=self.terrain.type
        self.terrain.moveTarget()
        rate=1.1
        while(True):

            self.s2t2=self.terrain.type
            total=np.count_nonzero(self.t_map==self.s2t1)+np.count_nonzero(self.t_map==self.s2t2)
            
            self.p_map2-=self.p_map2*rate
            self.p_map2[self.t_map==self.s2t1]+=rate/total
            self.p_map2[self.t_map==self.s2t2]+=rate/total
            
            curGrid=self.movingTerrainPickGrid()

            self.rule2count+=1
            self.rule2move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;


            lastGrid=curGrid
            self.s2t1=self.s2t2
            self.terrain.moveTarget()
        
        return self.rule2count   
    
    def movingConstraintSearch(self):
        self.rule3count=0
        self.rule3move=0
        lastGrid=self.terrainPickGrid()
        self.s3t1=self.terrain.type
        self.terrain.moveTarget()
        rate=1.0
        while(True):
            self.s3t2=self.terrain.type
            total=np.count_nonzero(self.t_map==self.s3t1)+np.count_nonzero(self.t_map==self.s3t2)
            self.p_map3-=self.p_map3*rate
            self.p_map3[self.t_map==self.s3t1]+=rate/total
            self.p_map3[self.t_map==self.s3t2]+=rate/total
            curGrid=self.movingCanstriantPickGrid(lastGrid)
            self.rule3count+=1
            self.rule3move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            lastGrid=curGrid
            self.s3t1=self.s3t2
            self.terrain.moveTarget()
        return self.rule3count   
    
#%%
        
b=MovingHunting()
b.movingSearch1()
print(b.rule1count)
#%%
s1=[]
m1=[]
s2=[]
m2=[]
s3=[]
m3=[]
for j in range(10):
    b=MovingHunting()
    #s1.append(b.movingSearch1())
    #m1.append(b.rule1move)
    #s2.append(b.movingSearch2())
    #m2.append(b.rule2move)
    s3.append(b.movingConstraintSearch())
    m3.append(b.rule3move)   
'''    
result=pd.DataFrame({'moving rule1 count':s1,
                 'moving rule1 motions':m1,
                 'moving rule2 count':s2,
                 'moving rule2 motions':m2,
                 #'moving rule3 count':s3,
                 #'moving rule3 motions':m3
                })
result.mean()'''
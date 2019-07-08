#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:45:16 2019

@author: ciuji
"""
# calculate move

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
        terrainMap=TerrainMap(size=50)
        self.terrain=terrainMap
        self.t_map=terrainMap.t_map
        self.p_map1=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map2=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map3=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)
        self.p_map=np.ones((terrainMap.size,terrainMap.size))/(terrainMap.size**2)

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
        candidateList=np.argwhere((self.p_map1==self.p_map1.max()))
        try:
            res=tuple(candidateList[np.random.choice(len(candidateList))])
            return res
        except:
            return self.randomPickGrid()
            
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
        return res      

    def movingCanstriantPickGrid(self,lastGrid):
        candidateList=np.argwhere((self.p_map3==self.p_map3.max()))
        c1=abs(candidateList-lastGrid)
        c2=c1.sum(axis=1)
        minPos=np.argmin(c2)
        return tuple(candidateList[minPos])

                 
    def getDistance(self,p,q):
        return abs(p[0]-q[0])+abs(p[1]-q[1])
                   
    def updateBelief(self,pmap,t1,t2,flag=0):
        if(flag==1):
            type1List=np.argwhere(self.t_map==t1)
            temp1=pmap.copy()
            temp1[self.t_map==t2]=0      
            npmap1=self.traverseList(temp1,type1List,t2)
            #print(npmap1)
            return npmap1

        if(t1==t2):
            typeList=np.argwhere(self.t_map==t1)
            pmap=self.sameTraverse(pmap,typeList,t2)
            return pmap
        type1List=np.argwhere(self.t_map==t1)
        type2List=np.argwhere(self.t_map==t2)
        temp1=pmap.copy()
        temp1[self.t_map==t2]=0
        temp2=pmap.copy()
        temp2[self.t_map==t1]=0
        npmap1=self.traverseList(temp1,type1List,t2)
        npmap2=self.traverseList(temp2,type2List,t1)

        return npmap1+npmap2
        
    def sameTraverse(self,pmap,List,t):
        newmap=pmap-pmap
        for node in List:
            nodeT=tuple(node)
            index=node[0]*self.terrain.size + node[1]
            table=np.array(self.n_table[index][1:])
            if (not (t in table)):  
                continue;
            curProb=pmap[nodeT]
            tableIndex=np.argwhere(table==t)
            #print(node,tableIndex)
            singleProb=curProb/len(tableIndex)
            for tindex in tableIndex:
                if tindex==0:
                    newmap[nodeT[0]-1,nodeT[1]]+=singleProb
                    continue;
                if tindex==1:
                    newmap[nodeT[0]+1,nodeT[1]]+=singleProb
                    continue;     
                if tindex==2:
                    newmap[nodeT[0],nodeT[1]-1]+=singleProb
                    continue;
                if tindex==3:
                    newmap[nodeT[0],nodeT[1]+1]+=singleProb
                    continue;
        return newmap        
    
    
    def traverseList(self,pmap,List,t):
        for node in List:
            nodeT=tuple(node)
            index=node[0]*self.terrain.size + node[1]
            table=np.array(self.n_table[index][1:])
            if (not (t in table)):  
                pmap[nodeT]=0
                #print(nodeT)
                continue;
            curProb=pmap[nodeT]
            tableIndex=np.argwhere(table==t)
            #print(node,tableIndex)
            singleProb=curProb/len(tableIndex)
            for tindex in tableIndex:
                if tindex==0:
                    pmap[nodeT[0]-1,nodeT[1]]+=singleProb
                    continue;
                if tindex==1:
                    pmap[nodeT[0]+1,nodeT[1]]+=singleProb
                    continue;     
                if tindex==2:
                    pmap[nodeT[0],nodeT[1]-1]+=singleProb
                    continue;
                if tindex==3:
                    pmap[nodeT[0],nodeT[1]+1]+=singleProb
                    continue;
            pmap[nodeT]=0
        return pmap
    
    def movingSearch1(self):
        self.rule1count=0
        self.rule1move=0
        lastGrid=self.randomPickGrid()
        self.s1t1=self.terrain.type
        self.terrain.moveTarget()
        lastType=self.terrain.type
        while(True):
            self.s1t2=self.terrain.type
           # if (self.s1t1!=self.s1t2) & (lastType!=self.s1t2):
            #    self.p_map1=self.updateBelief(self.p_map1,self.s1t1,self.s1t2,1)
           #else:     
            self.p_map1=self.updateBelief(self.p_map1,self.s1t1,self.s1t2)
               
            #print(np.count_nonzero(self.p_map1==self.p_map1.max()))
            self.p_map1[(self.t_map!=self.s1t1)&(self.t_map!=self.s1t2)]=0
            self.p_map1=self.p_map1/self.p_map1.sum()
            #print(np.where(self.p_map1==self.p_map1.max()))

            if(self.p_map1.max()>=1.0):
                print('speciala')
                if tuple(np.argwhere(self.p_map1>=1)[0])==self.terrain.target:
                    break
            curGrid=self.movingRandomPickGrid()
            self.rule1count+=1
            self.rule1move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            denominator=1-self.p_map1[curGrid]+self.p_map1[curGrid]*self.FN[self.t_map[curGrid]]
            self.p_map1[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map1/=denominator

            lastGrid=curGrid
            lastType=self.s1t1
            self.s1t1=self.s1t2
            self.terrain.moveTarget()
            
        return self.rule1count
    
    def movingSearch2(self):
        self.rule2count=0
        self.rule2move=0
        lastGrid=self.randomPickGrid()
        self.s2t1=self.terrain.type
        self.terrain.moveTarget()
        while(True):
            self.s2t2=self.terrain.type            
            self.p_map2=self.updateBelief(self.p_map2,self.s2t1,self.s2t2)
            self.p_map2[(self.t_map!=self.s2t1)&(self.t_map!=self.s2t2)]=0
            self.p_map2=self.p_map2/self.p_map2.sum() 
            if(self.p_map3.max()>=1.0):
                print('specialb')
                if tuple(np.argwhere(self.p_map3>=1)[0])==self.terrain.target:
                    break
            curGrid=self.movingTerrainPickGrid()
            self.rule2count+=1
            self.rule2move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            denominator=1-self.p_map2[curGrid]+self.p_map2[curGrid]*self.FN[self.t_map[curGrid]]
            self.p_map2[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map2/=denominator
            lastGrid=curGrid
            self.s2t1=self.s2t2
            self.terrain.moveTarget()
        return self.rule2count   
    
    def movingConstraintSearch(self):
        self.rule3count=0
        self.rule3move=0
        lastGrid=self.movingRandomPickGrid()
        self.s3t1=self.terrain.type
        self.terrain.moveTarget()
        while(True):
            self.s3t2=self.terrain.type
            self.p_map3=self.updateBelief(self.p_map3,self.s3t1,self.s3t2)
            self.p_map3[(self.t_map!=self.s3t1)&(self.t_map!=self.s3t2)]=0
            self.p_map3=self.p_map3/self.p_map3.sum()    
            if(self.p_map3.max()>=1.0):
                print('specialc')
                if tuple(np.argwhere(self.p_map3>=1)[0])==self.terrain.target:
                    break
            curGrid=self.movingCanstriantPickGrid(lastGrid)
            self.rule3count+=1
            self.rule3move+=self.getDistance(lastGrid,curGrid)
            if(self.checkOneGrid(curGrid)):
                break;
            lastGrid=curGrid
            denominator=1-self.p_map3[curGrid]+self.p_map3[curGrid]*self.FN[self.t_map[curGrid]]
            self.p_map3[curGrid]*=self.FN[self.t_map[curGrid]] 
            self.p_map3/=denominator
            self.s3t1=self.s3t2
            self.terrain.moveTarget()
        return self.rule3count   
    
    def togetherSearch(self):
        self.rule3count=0;self.rule3move=0;flag1=0
        self.rule2count=0;self.rule2move=0;flag2=0
        self.rule1count=0;self.rule1move=0;flag3=0
        lastGrid=self.movingRandomPickGrid()
        lastGrid3=lastGrid
        lastGrid2=lastGrid
        lastGrid1=lastGrid
        t1=self.terrain.type
        self.terrain.moveTarget()
        while(flag2*flag1*flag3!=1):
            #print("belief at Time:",self.rule1count)
            #print(self.p_map)
            t2=self.terrain.type
            self.s2t2=self.s1t2=self.s3t2=t2
            self.s1t1=self.s2t1=self.s3t1=t1
            self.p_map=self.updateBelief(self.p_map,t1,t2)
            self.p_map[(self.t_map!=t1)&(self.t_map!=t2)]=0
            self.p_map=self.p_map/self.p_map.sum()    
            self.p_map1=self.p_map2=self.p_map3=self.p_map

            '''if(self.p_map.max()>=1.0):
                print('special')
                if tuple(np.argwhere(self.p_map>=1)[0])==self.terrain.target:
                    break'''
            if(flag3!=1):
                curGrid3=self.movingCanstriantPickGrid(lastGrid3)
                self.rule3count+=1
                self.rule3move+=self.getDistance(lastGrid3,curGrid3)
                if(self.checkOneGrid(curGrid3)):
                    flag3=1;
                lastGrid3=curGrid3
            if(flag2!=1):
                curGrid2=self.movingTerrainPickGrid()
                self.rule2count+=1
                self.rule2move+=self.getDistance(lastGrid2,curGrid2)
                if(self.checkOneGrid(curGrid2)):
                    flag2=1;
                lastGrid2=curGrid2
                #print(curGrid2)
                #print(self.terrain.target)
            if(flag1!=1):
                curGrid1=self.movingRandomPickGrid()
                self.rule1count+=1
                self.rule1move+=self.getDistance(lastGrid1,curGrid1)
                if(self.checkOneGrid(curGrid1)):
                    flag1=1;
                lastGrid1=curGrid1

            t1=t2
            self.terrain.moveTarget()
        #print(flag1,flag2,flag3)
        return (self.rule1count,self.rule2count,self.rule3count)



#%%
        
b=MovingHunting()

b.movingSearch2()


#%%
import pandas as pd
s1=[]
m1=[]
s2=[]
m2=[]
s3=[]
m3=[]
for j in range(100):
    b=MovingHunting()
    b.movingSearch1()
    s1.append(b.rule1count)
    m1.append(b.rule1move)
    b.movingSearch2()
    s2.append(b.rule2count)
    m2.append(b.rule2move)
    b.movingConstraintSearch()
    s3.append(b.rule3count)
    m3.append(b.rule3move)   
    
result=pd.DataFrame({'moving rule1 count':s1,
                 'moving rule1 motions':m1,
                 'moving rule2 count':s2,
                 'moving rule2 motions':m2,
                 'moving rule3 count':s3,
                 'moving rule3 motions':m3
                })
result.mean()

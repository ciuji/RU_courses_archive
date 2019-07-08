#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:01:15 2019

@author: ciuji
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
maze_path='Maze.txt'

MSIZE=37

def readMaze(path=maze_path):
    maze=[]
    with open(path) as file:
        for line in file:
            newline=line.rstrip('\n').split('\t')
            maze.append(newline)
    maze[30][30]=-1
    return np.array(maze).astype(int)
#%% draw
def drawMaze(mmap,goal=1):
        plotmaze=mmap.copy()
        if(goal==1):
            plotmaze[30][30]=2
        plt.figure(figsize=(5,5))
        plt.pcolor(-plotmaze[::-1],cmap='gray',edgecolors='black',linewidth=1)
        #plt.imshow(-plotmaze,cmap='gray')

        plt.tight_layout()
        plt.axis('off')

        plt.show()
#%%
class Maze:
    def __init__(self):
        self.map=readMaze()
        
    def print(self):
        print(self.map)
        
    def show(self):
        plotmaze=self.map
        plotmaze[30][30]=2
        plt.axis('off')
        plt.imshow(-plotmaze,cmap='gray')
        plt.show()
    
    def isWall(self,arrij):
        return self.map[arrij[0],arrij[1]]==1
    
    def buildSurroundMap(self):
        bigmap=np.zeros((MSIZE+2,MSIZE+2))
        wall_list=np.argwhere(self.map==1)
        for node in wall_list:
            row=node[0]+1
            col=node[1]+1
            bigmap[row-1:row+2,col-1:col+2]+=1
        self.surroundMap=bigmap[1:MSIZE+1,1:MSIZE+1]
        self.surroundMap[self.map==1]=0
        return self.surroundMap
    
    
class Agent:
    def __init__(self):
        self.m=Maze()
        self.current_map=np.zeros((MSIZE,MSIZE))
        self.h_move=[]  #history move
        self.h_pos=[]   #history agent position
        self.c_pos=None #current agent position
        self.move_times=0
        
    def reNewMaze(self):
        #self.m=Maze()
        self.c_map=self.m.map.copy()
 
    def randomStart(self):
        pos=np.random.choice(range(MSIZE),size=2)
        while(self.m.isWall(pos)):
            pos=np.random.choice(range(MSIZE),size=2)
        self.start_pos=tuple(pos)
        self.c_pos=tuple(pos)
        self.h_pos.append(self.c_pos)

        return pos
    
    def randomOneMove(self,direction=None):
        if direction is None:
            direction=np.random.choice(range(4))
        self.move_times+=1
        if direction==0:#up
            move=tuple([-1,0])
        elif direction==1:#down
            move=tuple([1,0])
        elif direction==2:#left
            move=tuple([0,-1])
        elif direction==3:#right
            move=tuple([0,1])
        
        self.h_move.append(move)
        new_pos=tuple([self.c_pos[0]+move[0],self.c_pos[1]+move[1]])
        if not (self.m.isWall(new_pos)):
            self.c_pos=new_pos
            self.h_pos.append(self.c_pos)
            self.current_map[new_pos]+=1
            print(new_pos)
        else:
            return
        if(self.c_pos==(30,30)):
            
            print('got target!')
            raise Exception("got target!")

#%% gravity maze to find sequence      
            
class GravityMaze:
    def __init__(self):
        self.m=Maze()
        self.space_map=np.zeros((MSIZE,MSIZE))
        self.space_map[self.m.map==0]=1
        self.wall_map=np.zeros((MSIZE,MSIZE))
        self.wall_map[self.m.map==1]=1
        self.space_map[30,30]=1
        self.calculateBlock()
    
    #initial block surrounding information
    def calculateBlock(self):
        self.block_map=np.zeros((MSIZE,MSIZE))
        space_list=np.argwhere(self.space_map==1)
        for space in space_list:
            self.block_map[tuple(space)]=np.count_nonzero(self.wall_map[space[0]-1:space[0]+2,space[1]-1:space[1]+2])

    #find the highest probability cells after moves.
    #question e of Maze problem
    def findCell(self,observations=[],actions=[]):
        self.space_map[self.block_map!=observations[0]]=0

        for index,action in enumerate(actions):
            self.moveAll(action)
            self.space_map[self.block_map!=observations[index+1]]=0

        self.probability_map=self.space_map/self.space_map.sum()
        if (self.space_map>0).any():
            return np.argwhere(self.space_map==self.space_map.max()), self.space_map.max()/self.space_map.sum()
        else:
            print ("wrong! no such cell!")
            return None
     
    #move all the cells
    def moveAll(self,direction):
        old_map=self.space_map.copy()
        if(direction==0):
            #x_d=-1;y_d=0
            self.space_map[0:MSIZE-2,:]+=self.space_map[1:MSIZE-1,:]
            self.space_map[1:MSIZE-1,:]-=old_map[1:MSIZE-1,:]
            self.space_map[1:MSIZE-1,:]+=old_map[1:MSIZE-1,:]*self.wall_map[0:MSIZE-2,:]
            self.space_map[self.space_map<0]=0
            self.space_map[self.m.map==1]=0
            #self.space_map[30,30]=0
        elif(direction==1):
            #x_d=1;y_d=0
            self.space_map[1:MSIZE-1,:]+=self.space_map[0:MSIZE-2,:]
            self.space_map[0:MSIZE-2,:]-=old_map[0:MSIZE-2,:]
            self.space_map[0:MSIZE-2,:]+=old_map[0:MSIZE-2,:]*self.wall_map[1:MSIZE-1,:]
            self.space_map[self.space_map<0]=0
            self.space_map[self.m.map==1]=0
            #self.space_map[30,30]=0
        elif(direction==2):
            #x_d=0;y_d=-1;
            self.space_map[:,0:MSIZE-2]+=self.space_map[:,1:MSIZE-1]
            self.space_map[:,1:MSIZE-1]-=old_map[:,1:MSIZE-1]
            self.space_map[:,1:MSIZE-1]+=old_map[:,1:MSIZE-1]*self.wall_map[:,0:MSIZE-2]
            self.space_map[self.space_map<0]=0
            self.space_map[self.m.map==1]=0
            #self.space_map[30,30]=0
        elif(direction==3):
            #x_d=0;y_d=1
            self.space_map[:,1:MSIZE-1]+=self.space_map[:,0:MSIZE-2]
            self.space_map[:,0:MSIZE-2]-=old_map[:,0:MSIZE-2]
            self.space_map[:,0:MSIZE-2]+=old_map[:,0:MSIZE-2]*self.wall_map[:,1:MSIZE-1]
            self.space_map[self.space_map<0]=0
            self.space_map[self.m.map==1]=0
            #self.space_map[30,30]=0
            
    def bestMove(self):
        current_map=self.space_map.copy()
        count_nextmap=[]
        self.moveAll(0)
        count_nextmap.append(np.count_nonzero(self.space_map==0))
        self.space_map=current_map.copy()
        self.moveAll(1)
        count_nextmap.append(np.count_nonzero(self.space_map==0))   
        self.space_map=current_map.copy()
        self.moveAll(2)
        count_nextmap.append(np.count_nonzero(self.space_map==0)) 
        self.space_map=current_map.copy()
        self.moveAll(3)
        count_nextmap.append(np.count_nonzero(self.space_map==0)) 
        #print(count_nextmap)
        best_direction=count_nextmap.index(max(count_nextmap))
        self.space_map=current_map.copy()
        self.moveAll(best_direction)
        #print(best_direction)
        
'''
g.moveAll(1)
drawMaze(g.space_map,0)
print(g.space_map.sum())   '''     
#%%
'''
a=Agent()
a.randomStart()
for i in range(100):
    a.randomOneMove()


drawMaze(a.current_map)
'''
#%% get the shortest road from sequences

#is useful to find a road.
def findRoad(road):
    newroad=road.copy()
    node_index=pd.value_counts(list(newroad)).index

    for index in node_index:
        #print(node)
        node=tuple(index)
        print(node)
        temp=np.array(newroad)
        nodes_list=np.where((temp[:,0]==node[0]) & (temp[:,1]==node[1]))[0]
        if len(nodes_list)<=1:
            print(nodes_list)
            pass
        else:
            newroad=np.concatenate((newroad[:nodes_list[0]],newroad[nodes_list[-1]:]))
    return newroad

    
#%% DFS to find road
from collections import deque

class Node:
    def __init__(self,i=0,j=0):
        self.i=i
        self.j=j
        self.loc=(self.i,self.j)
        #self.loc=[i,j]

    
def bfs(maze,begin,target):
    start=Node(begin[0],begin[1])
    goal=Node(target[0],target[1])
    mp=maze.copy()
    #queue
    qu=deque()
    #record path
    path=[]
    dirArr=[[-1,0],[1,0],[0,-1],[0,1]] #four directions

    qu.append((start,0,0))
    while len(qu)!=0:
        curNode=qu.popleft()
        #print(curNode[0].loc)
        path.append(curNode)
        if curNode[0].i==goal.i and curNode[0].j==goal.j:
            mm=maze.copy()
            output=get_path(mm,path)
            #return (np.count_nonzero(mp==3))
            return output[::-1]
        for index,dirMove in enumerate(dirArr):
            nextNode=Node(curNode[0].i+dirMove[0],curNode[0].j+dirMove[1])
            if mp[nextNode.loc]!=1 and mp[nextNode.loc]!=3:
                qu.append((nextNode,len(path),index))
                mp[nextNode.loc]=3
    return False
    
    
def get_path(maze,path):
    curNode = path[-1]
    outputPath=[]
    while curNode[1]!=0:
        outputPath.append(curNode[2])
        curNode=path[curNode[1]-1]
        #print(curNode[2])
        #print (curNode[0].loc())
        maze[curNode[0].loc]=1
    return outputPath
    #for node in outputPath:
       # maze[node.loc()]=1
    
#%% find sequence
def findSequence():
    mmp=readMaze()
    g=GravityMaze()
    sequence=[]
    #solve points in diagonal
    for i in range(1,MSIZE-1):
        arr=bfs(mmp,[i,i],[35,35])
        temp=np.count_nonzero(g.space_map!=0)
        for move in arr:
            g.moveAll(move)
        if(temp>np.count_nonzero(g.space_map!=0)):
            temp=np.count_nonzero(g.space_map!=0)
            sequence+=arr
            #drawMaze(g.space_map,0)
    #print(np.count_nonzero(g.space_map!=0))    
    #solve other points
    not_solve_list=np.argwhere(g.space_map!=0)
    for point in not_solve_list:
        arr=bfs(mmp,point,[35,35])
        temp=np.count_nonzero(g.space_map!=0)
        for move in arr:
            g.moveAll(move)
        if(temp>np.count_nonzero(g.space_map!=0)):
            temp=np.count_nonzero(g.space_map!=0)
            sequence+=arr
            #drawMaze(g.space_map,0)
    #from 35,35 to goal
    arr=bfs(mmp,[35,35],[30,30])
    for move in arr:
        g.moveAll(move)
    sequence.append(arr)
    return sequence,g.space_map
    
    
    
    
    
    
    
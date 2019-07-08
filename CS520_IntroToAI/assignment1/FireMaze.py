#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 14:54:57 2019

@author: ciuji
"""

import numpy as np
import time
from Maze import Maze
from collections import deque
from Fringe import Node
from Fringe import Stack
from Fringe import PriorityQueue
import matplotlib.pyplot as plt
import random

        
#%% dfs
def dfs(maze):
    mp=maze.copy()
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    st=Stack()
    st.push(start)
    #print(des.loc())
    i=0
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]] #four directions
    while st.is_empty()==0:
        #print (st.stack)
        i+=1
        curNode=st.top()
        mp[1:11,1:11]=fire(mp[1:11,1:11])
        if(mp[curNode.loc]==5):
            #print("you are on fire")
            #print("game over")
            for node in st.stack:
                maze[node.loc]=1
            maze[mp==5]=3
            return False
        if curNode.loc==goal.loc:
            for node in st.stack:
                maze[node.loc]=1
            #print(np.count_nonzero(mp==3))
            maze[mp==5]=5
            return  i
            #return len(st.stack)-1
        for dirMove in dirArr:
            nextNode=Node(curNode.i+dirMove[0],curNode.j+dirMove[1])
            
            if mp[nextNode.loc]==0 or mp[nextNode.loc]==1:
                st.push(nextNode)
                mp[nextNode.loc]=3
                #print(nextNode.loc())
                break
            #mp[nextNode.loc]=3
        else:
            mp[curNode.loc]=3
            st.pop()
    return False

#%% bfs
def bfs(maze):
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    mp=maze.copy()
    #queue
    qu=deque()
    #record path
    path=[]
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]] #four directions

    qu.append((start,0))
    while len(qu)!=0:
        curNode=qu.popleft()
        path.append(curNode)
        if curNode[0].i==goal.i and curNode[0].j==goal.j:
            output=get_path(maze,path)
            return (np.count_nonzero(mp==3))
            #return len(output)
        for dirMove in dirArr:
            nextNode=Node(curNode[0].i+dirMove[0],curNode[0].j+dirMove[1])
            if mp[nextNode.loc]==0 or mp[nextNode.loc]==1:
                qu.append((nextNode,len(path)))
                mp[nextNode.loc]=3
    return False
    
    
def get_path(maze,path):
    curNode = path[-1]
    outputPath=[]
    while curNode[1]!=0:
        outputPath.append(curNode[0])
        curNode=path[curNode[1]-1]
        #print (curNode[0].loc())
        maze[curNode[0].loc]=1
    return outputPath
    #for node in outputPath:
       # maze[node.loc()]=1

#%% Astar
def manhattan_distance(start, goal):
        return abs(goal.i - start.i) + abs(goal.j - start.j)
    
def euclidean_distance(start, goal):
        return ((start.i - goal.i) ** 2 + (start.j - goal.j) ** 2)**0.5
    

    #priorityqueue

def singlefire(prob):
    tempList=np.zeros(16)
    tempList[:int(16*prob)]=5
    return random.choice(tempList)

def fire(mazemap):
    probMap=np.ones((10,10))
    if np.count_nonzero(mazemap==5)==0:
        mazemap[0,9]=5
    else: 
        for i in range(10):
            if np.count_nonzero(mazemap[i]==5) ==0:
                break
            for jj in range(10):
                j=-jj+9
                if mazemap[i,j]==5:
                    if(i>0 and mazemap[i-1,j]!=5):
                        probMap[i-1,j]*=(1/2)
                    if(i<9 and mazemap[i+1,j]!=5):
                        probMap[i+1,j]*=(1/2)
                        
                    if(j>0 and mazemap[i,j-1]!=5):
                        probMap[i,j-1]*=(1/2)
                    if(j<9 and mazemap[i,j+1]!=5):
                        probMap[i,j+1]*=(1/2)
                #else:
                    #break
        
        probMap=1-probMap
        for i in range(10):
            if np.count_nonzero(probMap[i]==0) ==10:
                break
            for jj in range(10):
                j=-jj+9
                if(probMap[i,j]!=0.0 and mazemap[i,j]!=2):
                    temp=singlefire(probMap[i,j])
                    if(temp!=0):
                        mazemap[i,j]=temp
    #print(probMap)
    return mazemap
                        
def astar(maze,heuristic=manhattan_distance):
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    mp=maze.copy()
    pq=PriorityQueue()
    pq.push(node=start,priority=heuristic(start,goal),path=[start])
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]]
    i=0
    while not pq.is_empty() :
        (curPrior,_,curNode,path)=pq.pop()
        i+=1
        #print(curPrior,len(path))
        #print(i)
        #print(curNode.loc,len(path))
        #mz.drawMaze(mp)
        if(mp[curNode.loc]==5):
            #print("you are on fire")
            #print("game over")
            #for node in path:
                #maze[node.loc]=1
            maze[mp==5]=3
            return False
        mp[1:11,1:11]=fire(mp[1:11,1:11])
        
        if curNode.loc==goal.loc:
            #mz.drawMaze(mp)
            for node in path:
                maze[node.loc]=1
            maze[mp==5]=3
            #return len(path)
            return i
        tempPath=path.copy()
        times=0
        for dirMove in dirArr:
            nextNode=Node(curNode.i+dirMove[0],curNode.j+dirMove[1])
            if mp[nextNode.loc]==0 or mp[nextNode.loc]==1:
                #times+=1
                if(len(tempPath)>0 and curNode.loc!=tempPath[-1].loc):
                    tempPath.append(curNode)
                #add escape to heuristic
                danger=0

                if( (nextNode.j<10 and mp[nextNode.i,nextNode.j+1]==5) or (nextNode.i<10 and mp[nextNode.i+1,nextNode.j]==5)):
                    danger=0
                elif( (nextNode.j<9 and mp[nextNode.i,nextNode.j+2]==5) or (nextNode.i<9 and mp[nextNode.i+2,nextNode.j]==5)):
                    danger=2
                elif( (nextNode.j<8 and mp[nextNode.i,nextNode.j+3]==5) or (nextNode.i<8 and mp[nextNode.i+3,nextNode.j]==5)):
                    danger=1
                else :
                    danger = -1
                    
                #print("danger",danger)    
                pq.push(nextNode,heuristic(nextNode,goal)+danger+times,tempPath)
                mp[nextNode.loc]=3  

    return False                     
                        
                        
                        
                        
mz=Maze()
x=[]
y1=[]
y2=[]
def analysisMaze(times,N=6):
    p = np.linspace(0.3,0.4, N, endpoint=True)

    for ap in p:
        ii=0
        temp1=[]
        temp2=[]
        maze=Maze()
        for ii in range(times):

            mp=maze.generateMaze(10,ap)   
            m1=mp.copy()
            m2=mp.copy()
            if(bfs(mp) is False):
                continue
            #result2=astar(maze.mazeMap,euclidean_distance)
            #result1=astar(maze.mazeMap,manhattan_distance)
            result1=astar(m1)
            result2=dfs(m2)
            if(result1 is not False):
                temp1.append(result1)
                mz.drawMaze(m1)
                mz.drawMaze(m2)
            if(result2 is not False):
                temp2.append(result2)
                
            #if result>temp[0]:
                #maze.drawMaze()
                
        y1.append(np.mean(temp1))
        y2.append(np.mean(temp2))
        
        #print (ap,":",y[-1])
    return p

x=analysisMaze(10,3)
plt.plot(x,y1,label="astar")
plt.plot(x,y2,label="DFS")
plt.xlabel("block density")
plt.ylabel("steps")
plt.legend()
plt.show()
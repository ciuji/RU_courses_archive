#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:42:37 2019

@author: ciuji
"""

#%% problem 3 hardmaze


import numpy as np
import time
from Maze import Maze
from collections import deque
from Fringe import Node
from Fringe import Stack
from Fringe import PriorityQueue
import matplotlib.pyplot as plt
import random

        
#%% bfs
def dfs(maze):
    mp=maze.copy()
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    st=Stack()
    st.push(start)
    #print(des.loc())
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]] #four directions
    while st.is_empty()==0:
        #print (st.stack)
        curNode=st.top()
        if curNode.loc==goal.loc:
            for node in st.stack:
                maze[node.loc]=1
            #print(np.count_nonzero(mp==3))
            return  np.count_nonzero(mp==3)
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
            return output
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
    return maze
    #for node in outputPath:
       # maze[node.loc()]=1

#%% Astar
def manhattan_distance(start, goal):
        return abs(goal.i - start.i) + abs(goal.j - start.j)
    
def euclidean_distance(start, goal):
        return ((start.i - goal.i) ** 2 + (start.j - goal.j) ** 2)**0.5
def astarLength(maze,start=Node(1,1),heuristic=manhattan_distance):
    goal=Node(len(maze)-2,len(maze)-2)
    mp=maze.copy()
    pq=PriorityQueue()
    pq.push(node=start,priority=heuristic(start,goal),path=[start])
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]]

    while not pq.is_empty() :
        (curPrior,_,curNode,path)=pq.pop()
        #print (curPrior)
        if curNode.loc==goal.loc:
            #return len(path)
            return (len(path))
        tempPath=path.copy()
        for dirMove in dirArr:
            nextNode=Node(curNode.i+dirMove[0],curNode.j+dirMove[1])
            if mp[nextNode.loc]==0 or mp[nextNode.loc]==1:
                if(len(tempPath)>0 and curNode.loc!=tempPath[-1].loc):
                    tempPath.append(curNode)

                pq.push(nextNode,heuristic(nextNode,goal)+len(path),tempPath)
                
                mp[nextNode.loc]=3
    return False

def astarExpand(maze,start=Node(1,1),heuristic=manhattan_distance):
    goal=Node(len(maze)-2,len(maze)-2)
    mp=maze.copy()
    pq=PriorityQueue()
    pq.push(node=start,priority=heuristic(start,goal),path=[start])
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]]

    while not pq.is_empty() :
        (curPrior,_,curNode,path)=pq.pop()
        #print (curPrior)
        if curNode.loc==goal.loc:
            #return len(path)
            return (np.count_nonzero(mp==3))
        tempPath=path.copy()
        for dirMove in dirArr:
            nextNode=Node(curNode.i+dirMove[0],curNode.j+dirMove[1])
            if mp[nextNode.loc]==0 or mp[nextNode.loc]==1:
                if(len(tempPath)>0 and curNode.loc!=tempPath[-1].loc):
                    tempPath.append(curNode)

                pq.push(nextNode,heuristic(nextNode,goal)+len(path),tempPath)
                
                mp[nextNode.loc]=3
    return False

def astar(maze,heuristic):
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    curMaze=maze.copy()
    mp=maze.copy()
    pq=PriorityQueue()
    pq.push(node=start,priority=heuristic(start,goal),path=[start])
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]]

    while not pq.is_empty() :
        (curPrior,_,curNode,path)=pq.pop()
        #print (curPrior)
        if(len(path)%4==0 ):
            curLen=astarLength(curMaze)
            if(curLen == False):
                return False
            if(astarLength(curMaze,curNode)+5<=curLen):
                curMaze=hardmaze(curMaze,mp==3,curLen)
        if curNode.loc==goal.loc:
            #get_path(maze)
            #for node in path:
            #    curMaze[node.loc]=1
            #print(mp==3)
            return curMaze
            #return (np.count_nonzero(mp==3))
        tempPath=path.copy()
        for dirMove in dirArr:
            nextNode=Node(curNode.i+dirMove[0],curNode.j+dirMove[1])
            if(mp[nextNode.loc]!=3):
                if curMaze[nextNode.loc]==0 or curMaze[nextNode.loc]==1:
                    if(len(tempPath)>0 and curNode.loc!=tempPath[-1].loc):
                        tempPath.append(curNode)
    
                    pq.push(nextNode,heuristic(nextNode,goal)+len(path),tempPath)
                    
                    mp[nextNode.loc]=3  
                mp[nextNode.loc]=3  

    return False
    #priorityqueue


#%%
x=[]
y=[]
maze=Maze()
'''
for i in range(1000):
    mp=maze.generateMaze(10,0.1)
    a=astar(mp,manhattan_distance)
    y.append(a)
    if(a>19):
        maze.drawMaze(mp)

print (np.max(y))
 
    
'''   
    
def hardmaze(originMap,visitedMap,curLen):
    #print(visitedMap)
    #print("do hard maze")
    originMap[1,1]=originMap[10,10]=0
    for i in range(200):
        newMap=originMap.copy()
        
        shuffleMap=newMap[1:11,1:11]
        shuffleMap=shuffleMap.flatten()
        random.shuffle(shuffleMap)
        shuffleMap=shuffleMap.reshape((10,10))
        newMap[1:11,1:11]=shuffleMap
        newMap[visitedMap]=originMap[visitedMap]
        newMap[1,1]=newMap[10,10]=1
        
        
        #maze.drawMaze(newMap)
        newLen=astarLength(newMap)
        #print(newLen,curLen)
        if(newLen>curLen):
            print (newLen)
            #maze.drawMaze(newMap)
            return newMap
    #print("fail")
    originMap[1,1]=originMap[10,10]=1

    return originMap

    
    
mp=maze.generateMaze(10,0.3)
#maze.drawMaze(mp)    

mp1=mp.copy()
a=astar(mp1,manhattan_distance) 
if (a is not False):
    maze.drawMaze(bfs(a))
    maze.drawMaze(bfs(mp1))
    
    
    
    
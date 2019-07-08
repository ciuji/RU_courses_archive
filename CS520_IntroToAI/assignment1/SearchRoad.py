#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:22:16 2019

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


        
#%% dfs
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
            #for node in st.stack:
                #maze[node.loc]=1
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
            #output=get_path(maze,path)
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
    
def astar(maze,heuristic):
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    mp=maze.copy()
    pq=PriorityQueue()
    pq.push(node=start,priority=heuristic(start,goal),path=[start])
    dirArr=[[1,0],[0,1],[0,-1],[-1,0]]

    while not pq.is_empty() :
        (curPrior,_,curNode,path)=pq.pop()
        #print (curPrior)
        if curNode.loc==goal.loc:
            #get_path(maze)
            #for node in path:
             #   maze[node.loc]=1
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
    #priorityqueue
    
#%%
    #def fire(maze):
        
#%%
'''
maze=Maze()
maze.generateMaze(10,0.2)    
maze.drawMaze()           
# mp=maze.mazeMap.copy()    
mp1=maze.mazeMap.copy()
mp2=maze.mazeMap.copy()
#bfs(maze=mp)
dfs(maze=mp1)
astar(maze=mp2,heuristic=manhattan_distance)
#maze.drawMaze(mp1)
maze.drawMaze(mp2)
'''
#%% problem 2-2: analysis
# =============================================================================
# x=[]
# y=[]
# def analysisMaze(times,N=6):
#     p = np.linspace(0.1, .7, N, endpoint=False)
# 
#     for ap in p:
#         i=0
#         for ii in range(times):
#             maze=Maze()
#             maze.generateMaze(10,ap)    
#             if(astar(maze.mazeMap,manhattan_distance)):
#                 i+=1
#         y.append(i/times)
#         
#         print (ap,":",i/times)
#     return p
# x=analysisMaze(2000,20)
# =============================================================================
# =============================================================================
# plt.xlabel("density")
# plt.ylabel("solvability")
# plt.scatter(x[7],y[7],c='r',s=50)
# 
# #problem 2.3
# plt.annotate(
#         '(%s, %s)' %(x[7], y[7]),
#         xy=(x[7], y[7]),
#         xytext=(0, -10),
#         textcoords='offset points',
#         ha='center',
#         va='top')
# 
# plt.plot(x,y)
# plt.savefig("denistyandsolvability.png")
# =============================================================================
#%% problem 2-4

# =============================================================================
# x=[]
# y=[]
# start=time.time()
# def analysisMaze(times,N=6):
#     p = np.linspace(0.05,0.30, N, endpoint=True)
# 
#     for ap in p:
#         i=0
#         temp=[]
#         for ii in range(times):
#             maze=Maze()
#             maze.generateMaze(10,ap)   
#             result=astar(maze.mazeMap,euclidean_distance)
#             #result=dfs(maze.mazeMap)
# 
#             if(result):
#                 i+=1
#                 temp.append(result)
#             #if result>temp[0]:
#                 #maze.drawMaze()
#                 
#         y.append(np.mean(temp))
#         
#         print (ap,":",y[-1])
#     return p
# x=analysisMaze(1000,10)
# plt.xlabel("density")
# plt.ylabel("length of shortest path")
# plt.title("A*:density vs expected shortest path length")
# plt.plot(x,y)
# print("time:",time.time()-start)
# plt.savefig("astarECDshortestpath.png")
# =============================================================================

# =============================================================================
# maze=Maze()
# maze.generateMaze(10,0.2)    
# mp2=maze.mazeMap.copy()
# astar(maze=mp2,heuristic=manhattan_distance)
# maze.drawMaze(mp2)
# =============================================================================
#%% problem 2-5
# =============================================================================
# x=[]
# y=[]
# start=time.time()
# def analysisMaze(times,N=6):
#     p = np.linspace(0.05,0.30, N, endpoint=True)
# 
#     for ap in p:
#         i=0
#         temp=[]
#         for ii in range(times):
#             maze=Maze()
#             maze.generateMaze(10,ap)   
#             #result=astar(maze.mazeMap,euclidean_distance)
#             result=dfs(maze.mazeMap)
# 
#             if(result):
#                 i+=1
#                 temp.append(result)
#             #if result>temp[0]:
#                 #maze.drawMaze()
#                 
#         y.append(np.mean(temp))
#         
#         print (ap,":",y[-1])
#     return p
# x=analysisMaze(1000,10)
# plt.xlabel("density")
# plt.ylabel("length of shortest path")
# plt.title("A*:density vs expected shortest path length")
# plt.plot(x,y)
# print("time:",time.time()-start)
# =============================================================================
# =============================================================================
# start1=time.time()
# result=[]
# for i in range(500):
#     
#     maze=Maze()
#     maze.generateMaze(10,0.2)    
#     mp2=maze.mazeMap.copy()
#     a=astar(mp2,manhattan_distance)
#     if a:
#         result.append(a)
#         
# print (np.mean(result))
# 
# =============================================================================

# 2.1
# =============================================================================
# x=[]
# y=[]
# def analysisMaze(times,N=6):
#     p = [5,10,20,50]
#     start=time.time()
#     for ap in p:
#         i=0
#         for ii in range(times):
#             maze=Maze()
#             maze.generateMaze(ap,0.2)    
#             if(astar(maze.mazeMap,manhattan_distance)):
#                 i+=1
#         y.append(i/times)
#         
#         print ("dim=",ap,"time:",time.time()-start,"solvability:",y[-1])
#     return p
# x=analysisMaze(2000,20)
# =============================================================================
# =============================================================================
# x=[]
# y1=[]
# y2=[]
# start=time.time()
# def analysisMaze(times,N=6):
#     p = np.linspace(0.0,0.30, N, endpoint=True)
# 
#     for ap in p:
#         i=0
#         temp1=[]
#         temp2=[]
#         for ii in range(times):
#             maze=Maze()
#             maze.generateMaze(10,ap)   
#             #result2=astar(maze.mazeMap,euclidean_distance)
#             #result1=astar(maze.mazeMap,manhattan_distance)
#             result1=dfs1(maze.mazeMap)
#             result2=dfs2(maze.mazeMap)
#             if(result1):
#                 i+=1
#                 temp1.append(result1)
#                 temp2.append(result2)
#             #if result>temp[0]:
#                 #maze.drawMaze()
#                 
#         y1.append(np.mean(temp1))
#         y2.append(np.mean(temp2))
#         
#         #print (ap,":",y[-1])
#     return p
# x=analysisMaze(100,10)
# plt.xlabel("density")
# plt.ylabel("visited nodes")
# plt.title("BFS and DFS comparison")
# plt.plot(x,y1,label="BFS")
# plt.plot(x,y2,label="DFS")
# plt.legend()
# print("time:",time.time()-start)
# =============================================================================
'''
def dfs1(maze):
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
            #for node in st.stack:
                #maze[node.loc]=1
            #print(np.count_nonzero(mp==3))
            #return  np.count_nonzero(mp==3)
            return len(st.stack)-1
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
def dfs2(maze):
    mp=maze.copy()
    start=Node(1,1)
    goal=Node(len(maze)-2,len(maze)-2)
    st=Stack()
    st.push(start)
    #print(des.loc())
    dirArr=[[-1,0],[0,-1],[0,1],[1,0]] #four directions
    while st.is_empty()==0:
        #print (st.stack)
        curNode=st.top()
        if curNode.loc==goal.loc:
            #for node in st.stack:
                #maze[node.loc]=1
            #print(np.count_nonzero(mp==3))
            #return  np.count_nonzero(mp==3)
            return len(st.stack)-1
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
x=[]
y1=[]
y2=[]
start=time.time()
def analysisMaze(times,N=6):
    p = np.linspace(0.0,0.30, N, endpoint=True)

    for ap in p:
        i=0
        temp1=[]
        temp2=[]
        for ii in range(times):
            maze=Maze()
            maze.generateMaze(10,ap)   
            #result2=astar(maze.mazeMap,euclidean_distance)
            #result1=astar(maze.mazeMap,manhattan_distance)
            result1=dfs1(maze.mazeMap)
            result2=dfs2(maze.mazeMap)
            if(result1):
                i+=1
                temp1.append(result1)
                temp2.append(result2)
            #if result>temp[0]:
                #maze.drawMaze()
                
        y1.append(np.mean(temp1))
        y2.append(np.mean(temp2))
        
        #print (ap,":",y[-1])
    return p
x=analysisMaze(100,10)
plt.xlabel("density")
plt.ylabel("average length of path")
plt.title("different DFS comparison")
plt.plot(x,y1,label="good DFS")
plt.plot(x,y2,label="bad DFS")
plt.legend()
print("time:",time.time()-start)
'''

x=[]
y4=[]
def analysisMaze(times,d,p):

    i=0
    for ii in range(times):
        maze=Maze()
        maze.generateMaze(d,p)    
        if(astar(maze.mazeMap,manhattan_distance)):
            i+=1
    
        #print ("dim=",ap,"time:",time.time()-start,"solvability:",y[-1])
    return i/times


pp=np.linspace(0.3,0.60, 6, endpoint=True)
for ap in pp:
    y4.append(analysisMaze(100,50,ap))
    
# =============================================================================
# x=np.linspace(0.0,0.60, 6, endpoint=True)
# plt.plot(x,y1,label=:)
# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.plot(x,y4)
# =============================================================================

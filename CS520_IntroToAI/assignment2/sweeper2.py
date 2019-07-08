#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:11:54 2019

@author: ciuji
"""

import numpy as np
from mines import MineGenerator
import heapq
import matplotlib.pyplot as plt
from collections import defaultdict

#from sweeper import Agent
'''
class LogicalCheck:
    def __init__(self,board):
        self.original=board
        self.state=board.copy()
        self.blocks=list(np.argwhere(board>0))
        self.unknown=list(np.argwhere(board==-2))
        #self.blocklist=defaultdict(list)
        self.unknownlist=defaultdict(list)
        self.x=board.shape[0]
        self.y=board.shape[1]
        self.result=np.zeros((len(self.unknown),0))
# =============================================================================
#         for i in self.blocks:
#             for j in self.unknown:
#                 if (self.euclidean_distance(i,j)<2):
#                     self.blocklist[tuple(i)].append(tuple(j))
# =============================================================================
        for i in self.unknown:
            for j in self.blocks:
                if (self.euclidean_distance(i,j)<2):
                    self.unknownlist[tuple(i)].append(tuple(j))
        
        self.backtrack(self.unknown,[],self.state)
        
    def get_result(self):
        positions=[]
        if(len(self.result)>0):
            self.result=self.result.reshape(int(len(self.result)/len(self.unknown)),len(self.unknown))
            count=0
            for i in self.result.T:
                if((i==0).all() or (i==1).all()):
                    positions.append(count)
                count+=1
        if(positions==[]):
            return False
        else:
            finalPos=[]
            finalValue=[]
            for i in positions:
                finalPos.append(self.unknown[i])
                finalValue.append(int(self.result[0][i]))
        #print(finalPos,finalValue)
            self.finalPos=finalPos
            self.finalValue=finalValue
            return True
    
    def backtrack(self,prop_stack,prop_valuelist,prop_state):

        #print(node)
        for i in list(range(2))[::-1]:
            state=prop_state.copy()
            stack=prop_stack.copy()
            valuelist=prop_valuelist.copy()
            try:
                node=stack.pop(0)
            except:
                print(state)
                print(valuelist)
                self.result=np.append(self.result,valuelist)
                return True
            #if(node[0]==0):
                #print(valuelist)
            try_return=self.try_value(node[0],node[1],i,state)
            if(try_return is not False):
                state=try_return
                valuelist.append(i)

                if(len(stack)!=0):
                    self.backtrack(stack,valuelist,state)

                
                else:
                    if(np.count_nonzero(state>0)==0):
                        #print(state)
                        #print(valuelist)
                        self.result=np.append(self.result,valuelist)
                        return True
                valuelist.pop()
        return False
    
   # def get_result(self):
        #for i
    
    def try_value(self,xx,yy,value,state):
        board=state.copy()
        if(board[xx,yy]==0):
            return False
        lx=-1;ly=-1;rx=2;ry=2
        if xx==0:lx=0
        if yy==0:ly=0
        if xx==self.x-1:rx=1
        if xx==self.y-1:ry=1    
        temp= np.argwhere(self.original[xx+lx:xx+rx,yy+ly:yy+ry]>0)
        for item in temp:
            if (item[0]==1 and item[1]==1):
                continue
            
            board[xx+lx+item[0],yy+ly+item[1]]-=value
        #print(board)
        if(np.count_nonzero(board==-1)!=0):
            return False
        else:
            state=board
            return board
        
    def euclidean_distance(self,start, goal):
        return ((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2)**0.5
'''
class Heap:
    def __init__(self):
        self.heap=[]
        self.index=0
        
    def push(self,board,node):
        blockValue=board[node[0],node[1]]
        heapq.heappush(self.heap,(blockValue,self.index,node))
        self.index-=1
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return self.heap==[]
        
    
class Agent_nbt:
    def __init__(self,board):
        self.object=board
        self.x=board.shape[0]
        self.y=board.shape[1]
        self.current=np.ones([self.x,self.y])*-2
        self.visited=np.zeros([self.x,self.y])
        self.target=np.count_nonzero(self.object==-1)
        self.nodelist=Heap()
        self.cannotsolve=Heap()
        self.unsolvedboard=np.zeros([self.x,self.y])
        self.score=0
    
    def first_step(self):
        while(True):
            if(np.count_nonzero(self.object==0)<4):
                self.try_one_block(0,0)
            xx= np.random.choice(range(self.x))
            yy=np.random.choice(range(self.y))
            if(self.object[xx,yy]==0):
                #self.current[xx,yy]==0
                break;
        self.update_zero(xx,yy)
        count=0
# =============================================================================
#         while(self.target!=0):
#             self.scan_nodelist()
# 
#             unsolvedlist=np.argwhere(self.visited<0)
#             print(self.score)
#             print(self.visited)
#             for item in unsolvedlist:
#                 possibleMineList=self.get_neighbor(item[0],item[1],-2)
#                 for onemine in possibleMineList:
#                     if( self.try_one_block(onemine[0],onemine[1])==False):
#                         continue
#                     else:
#                         break
#             print(self.nodelist.heap[0])
#             self.scan_nodelist()
#             count+=1
#             if(count>=40):
#                 break
# =============================================================================
        

        
        
        while(self.target!=0):
            self.scan_nodelist()
            #unsolvedlist=np.argwhere(self.visited<0)
            #print(self.score)
            #print(self.visited)
            #print(self.cannotsolve.is_empty())
            unsolvedlist=np.argwhere(self.visited<0)
            
            
# =============================================================================
#            #solve uncetain situation
#             for item in unsolvedlist:
#                 blockValue=self.current[tuple(item)]-len(self.get_neighbor(item[0],item[1],-1))
#                 self.unsolvedboard[tuple(item)]=blockValue
#                 neighborlist=self.get_neighbor(item[0],item[1],-2)
#                 for item1 in neighborlist:
#                     self.unsolvedboard[tuple(item1)]=-2
#             
#             if(not (self.unsolvedboard==0).all()):
#                 lc=LogicalCheck(self.unsolvedboard)
#                 #mg.drawboard(self.current)
#                 if(lc.get_result()):
#                     for i,element in enumerate(lc.finalValue):
#                         if element==0:
#                             self.try_one_block(lc.finalPos[i][0],lc.finalPos[i][1])
#                         else:
#                             self.update_newmine(lc.finalPos[i][0],lc.finalPos[i][1])
#                     #mg.drawboard(self.current)
#                     #print(self.nodelist.is_empty())
#                     self.scan_nodelist()
#                 #else:
#                     #print("no")
#             #mg.drawboard(self.current)
#             #print(self.nodelist.is_empty())'''
# =============================================================================
    
            
            while(self.cannotsolve.is_empty()==False):
                _,_,item=self.cannotsolve.pop()
                if(self.visited[tuple(item)]==1):
                    continue
                #print(item)
                possibleMineList=self.get_neighbor(item[0],item[1],-2)
                for onemine in possibleMineList:
                    if( self.try_one_block(onemine[0],onemine[1])==False):
                        continue
                    else:
                        break
            self.scan_nodelist()
            count+=1
            if(count>=40):
                print("toomuch")
                break
            
        if(self.target==0):
            #print("success!")  
            #print(self.score)
            return (abs(self.score))
        else:
            return -1
            
# =============================================================================
#             unsolveddic={}
#             for item in unsolvedlist:
#                 blockValue=self.current[tuple(item)]-len(self.get_neighbor(item[0],item[1],-1))
#                 unsolveddic[tuple(item)]=blockValue
#                 self.unsolvedboard[tuple(item)]=blockValue
#             self.unsolvedboard[self.current==-2]=self.current[self.current==-2]
#             print (self.unsolvedboard)
#             self.unsolveddic=unsolveddic
# =============================================================================

            
    def scan_nodelist(self):
        while(self.nodelist.is_empty() is False):
            _,_,node=self.nodelist.pop()
            if(self.visited[tuple(node)]==1):
                continue
            #print(node)
            self.check_one_block(node[0],node[1])         
            
            
    # find a new zero
    def update_zero(self,xx,yy):
        # make sure no visited
        if(self.current[xx,yy]!=-2):
            return
        if(self.visited[xx,yy]==1):
            return
         
        # if 0, keey going
        if(self.object[xx,yy]==0):
            self.current[xx,yy]=0
            #north
            if(xx>0):
                self.update_zero(xx-1,yy)
                if(yy>0):
                    self.update_zero(xx-1,yy-1)
                if(yy<self.y-1):
                    self.update_zero(xx-1,yy+1)                 
            #south
            if(xx<self.x-1):
                self.update_zero(xx+1,yy)
                if(yy>0):
                    self.update_zero(xx+1,yy-1)
                if(yy<self.y-1):
                    self.update_zero(xx+1,yy+1)
            #east
            if(yy>0):
                self.update_zero(xx,yy-1)
            #west
            if(yy<self.y-1):
                self.update_zero(xx,yy+1)
            self.visited[xx,yy]==1
            
        else:
            self.current[xx,yy]=self.object[xx,yy]
            self.nodelist.push(self.current,[xx,yy])
        
        self.visited[self.current==0]=1
        
            
        # not zero, push in
        
            
    # found a new mine
    def update_newmine(self,xx,yy):
        #print("mine",xx,yy)

        #mg.drawboard(self.current)
        if(self.visited[xx,yy]==1):
            return 
        if(self.object[xx,yy]!=-1):
            self.score-=1
            self.current[xx,yy]=self.object[xx,yy]
            self.nodelist.push(self.visited,[xx,yy])
            self.check_one_block(xx,yy)
            #raise Exception("wrong step! game over!",xx,yy)
            return
        self.current[xx,yy]=-1
        self.visited[xx,yy]=1
        self.target-=1
        #get known neighbor to update
        neighborlist=self.get_not_neighbor(xx,yy,-2)
        for item in neighborlist:
            self.check_one_block(item[0],item[1])
        
        
    # scan the whole board
    def scan_unsolved(self):
        return self.x
    
    def try_one_block(self,xx,yy):
        blockValue=self.object[xx,yy]
        if (blockValue==-1):
            self.score-=1
            self.update_newmine(xx,yy)
            return False
            #raise Exception("wrong step! game over!",xx,yy) 
        else:
            self.current[xx,yy]=blockValue
            self.nodelist.push(self.current,[xx,yy])
            self.check_one_block(xx,yy,1)
        return True

    
    def check_one_block(self,xx,yy,sign=0):
        #if block is visited or mine, return
        if(self.visited[xx,yy]==1  or self.current[xx,yy]==-2):
            return 
        if(self.current[xx,yy]==-1):
            self.update_newmine(xx,yy)
            return 
        if(self.current[xx,yy]==0):
            self.update_zero(xx,yy)
        bigboard=np.zeros((self.x+2,self.y+2))
        bigboard[1:self.x+1,1:self.y+1]=self.current
        blockValue=bigboard[xx+1,yy+1]
        if(np.count_nonzero(bigboard[xx:xx+3,yy:yy+3]==-2)==0):
            self.visited[xx,yy]=1
            return  
        elif ((np.count_nonzero(bigboard[xx:xx+3,yy:yy+3]==-2))+(np.count_nonzero(bigboard[xx:xx+3,yy:yy+3]==-1)))==blockValue:
            #visited this block, never visit again
            self.visited[xx,yy]=1
            neighbor_mine=self.get_neighbor(xx,yy,-2)
            #open neighbors
            for item in neighbor_mine:
                self.current[item[0],item[1]]=-1
            neighbor_number=self.get_not_neighbor(xx,yy,-1)            
            for item in neighbor_number:
                self.current[item[0],item[1]]=self.object[item[0],item[1]]      
                self.nodelist.push(self.current,item)
            #check neighbor    
            for item in neighbor_mine:
                #print(xx,yy,"find",item[0],item[1])
                self.update_newmine(item[0],item[1])
            for item in neighbor_number:
                #print(xx,yy,"origin",item[0],item[1])
                self.check_one_block(item[0],item[1])
        # open all the nearby blocks
        elif (np.count_nonzero(bigboard[xx:xx+3,yy:yy+3]==-1)==blockValue):
            #visited this block, never visit again
            self.visited[xx,yy]=1
            #open neighbors
            neighbor_number=self.get_not_neighbor(xx,yy,-1)   
            for item in neighbor_number:
                self.current[item[0],item[1]]=self.object[item[0],item[1]]
                self.nodelist.push(self.current,item)

            #check neighbor    
            for item in neighbor_number:
                #print(xx,yy,"origin",item[0],item[1])
                self.check_one_block(item[0],item[1])    

        else:
            #uncertain block, push in nodelist again
            self.cannotsolve.push(self.current,[xx,yy])

            self.visited[xx,yy]-=1
            
            
    def get_neighbor(self,xx,yy,target):
        lx=-1;ly=-1;rx=2;ry=2
        if xx==0:lx=0
        if yy==0:ly=0
        if xx==self.x-1:rx=1
        if xx==self.y-1:ry=1    
        temp= np.argwhere(self.current[xx+lx:xx+rx,yy+ly:yy+ry]==target)
        result=[]
        for item in temp:
            if (item[0]==1 and item[1]==1):
                continue
            
            result.append([xx+lx+item[0],yy+ly+item[1]])
        return result
    
    def get_not_neighbor(self,xx,yy,target):
        lx=-1;ly=-1;rx=2;ry=2
        if xx==0:lx=0;
        if yy==0:ly=0;
        if xx==self.x-1:rx=1;
        if yy==self.y-1:ry=1; 
        temp= np.argwhere(self.current[xx+lx:xx+rx,yy+ly:yy+ry]!=target)
        result=[]
        for item in temp:
            if (item[0]==1 and item[1]==1):
                continue
            else:
                result.append([xx+lx+item[0],yy+ly+item[1]])
        return result


# =============================================================================
# #example
# mg=MineGenerator(p=20)
# #mg.drawboard()
# #print('object:\n',mg.board)
# sp=Agent(mg.board)
# sp.first_step()
# #print('current:\n',sp.current)
# mg.drawboard(sp.current)
# =============================================================================
# =============================================================================
# y=[]
# x=np.array([8,12,16,22,28])
# 
# for i in x:
#     temp=[]
#     for j in range(40):
#         mg=MineGenerator(p=i)
#         sp=Agent(mg.board)
#         res=sp.first_step()
#         if(res!=-1):
#             temp.append(res)
#     print("dd")
#     y.append(np.mean(temp))
#     
# plt.figure()
# plt.plot(x,y)
# plt.show()
# =============================================================================

# =============================================================================
# y=[]
# x=np.array(range(30,40,2))
# 
# for i in x:
#     temp=[]
#     for j in range(30):
#         mg=MineGenerator(x=i,y=i,p=0.1)
#         sp=Agent_nbt(mg.board)
#         res=sp.first_step()
#         if(res!=-1):
#             temp.append(res)
#     print("dd")
#     y.append(np.mean(temp))
#     
# plt.figure()
# plt.plot(x,y)
# plt.show()
# =============================================================================


# =============================================================================
# #example
# #mg=MineGenerator(p=20)
# #mg.drawboard()
# #print('object:\n',mg.board)
# sp2=Agent2(mg.board)
# res2=sp2.first_step()
# #print('current:\n',sp.current)
# mg.drawboard(sp2.current)
# print(res2)
# =============================================================================

sp1=Agent_nbt(mg.board)
res1=sp1.first_step()
print(res1)

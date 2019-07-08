import numpy as np
import matplotlib.pyplot as plt
import random

class MineGenerator:
    def __init__(self,x=10,y=10,p=0.1):
        self.x=x
        self.y=y
        self.p=p
        self.generateboard()
        
    def generatemines(self):
        x=self.x;y=self.y;p=self.p
        arr=np.zeros(x*y)
        if(p<1):
            num = int(x*y*p)
        else:
            num=p
        mines=np.random.choice(range(x*y),size=num,replace=False)
        for i in mines:
            arr[i]=-1
            
        board=np.array(arr).reshape((x,y))
        return board
    
    def generatetips(self,board):
        x=board.shape[0]
        y=board.shape[1]
        bigboard=np.zeros((x+2,y+2))
        bigboard[1:x+1,1:y+1]=board
        mineIndices= np.argwhere(bigboard==-1)
        for i,j in mineIndices:
            for m in range(-1,2):
                for n in range(-1,2):
                    if bigboard[i+m,j+n]==-1:
                        continue
                    else:
                        bigboard[i+m,j+n]+=1
                        #bigboard[i+m,j+n]+=random.randint(0,1)
        board=bigboard[1:x+1,1:y+1]
        return board
        
    def drawboard(self,originalboard=None):
        if originalboard is None:
            board=self.board.copy()
        else:
            board=originalboard.copy()
        board[board==-1]=-5
        board[board==-2]=-12
        if((board!=-2).all()==True):
            board[board==-1]=-2
            #board[board>0]=11
            board[board==0]=0


        plt.figure(figsize=(5,5))
        plt.pcolor(-board[::-1],edgecolors='black',cmap='bwr', linewidths=2)
        plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.show()     
            
    def generateboard(self):
        board=self.generatemines()
        board=self.generatetips(board)
        self.board=board

import numpy as np
import heapq
import matplotlib.pyplot as plt
from collections import defaultdict

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
        '''for i in self.blocks:
            for j in self.unknown:
                if (self.euclidean_distance(i,j)<2):
                    self.blocklist[tuple(i)].append(tuple(j))'''
        for i in self.unknown:
            for j in self.blocks:
                if (self.euclidean_distance(i,j)<2):
                    self.unknownlist[tuple(i)].append(tuple(j))
                    
        if(len(self.unknown)<30):
            self.backtrack(self.unknown,[],self.state)
        
    def get_result(self):
        if(len(self.unknown)>30):
            return False
        positions=[]
        if(self.result.size>0):
            try:
                self.result=self.result.reshape(int(len(self.result)/len(self.unknown)),len(self.unknown))
            except:
                print(self.result)
                return False
            count=0
            for i in self.result.T:
                if((i==0).all() or (i==1).all()):
                    positions.append(count)
                count+=1
        else:
            return False
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
            stack=prop_stack[:]
            valuelist=prop_valuelist[:]
            try:
                node=stack.pop(0)
            except:
                #print(state)
                #print(valuelist)
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
        
    
class Agent:
    def __init__(self,board):
        self.object=board
        self.x=board.shape[0]
        self.y=board.shape[1]
        self.current=np.ones([self.x,self.y])*-2
        self.visited=np.zeros([self.x,self.y])
        self.target=np.count_nonzero(self.object==-1)
        self.allnumber=np.count_nonzero(self.object==-1)
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
        
        while(self.target!=0):
            self.scan_nodelist()
            unsolvedlist=np.argwhere(self.visited<0)
            print(self.current)
            #solve uncetain situation
            for item in unsolvedlist:
                blockValue=self.current[tuple(item)]-len(self.get_neighbor(item[0],item[1],-1))
                self.unsolvedboard[tuple(item)]=blockValue
                neighborlist=self.get_neighbor(item[0],item[1],-2)
                for item1 in neighborlist:
                    self.unsolvedboard[tuple(item1)]=-2

            if(not (self.unsolvedboard==0).all()):
                lc=LogicalCheck(self.unsolvedboard)
                print(len(lc.unknown))
                #mg.drawboard(self.current)
                if(lc.get_result()):
                    print (lc.finalValue)
                    for i,element in enumerate(lc.finalValue):
                        if element==0:
                            self.try_one_block(lc.finalPos[i][0],lc.finalPos[i][1])
                            print("backtrack")

                        else:
                            self.update_newmine(lc.finalPos[i][0],lc.finalPos[i][1])
                            print("backtrack")
                    print(self.current)
                    self.scan_nodelist()

            

    
            self.try_cannot_solve()

            self.scan_nodelist()
            count+=1
            if(count>60):
                print("toomuch")
                break
            
        if(self.target==0):
            self.rightrate=(self.allnumber+self.score)/float(self.allnumber)
            self.current[self.current==-2]=self.object[self.current==-2]
            return (abs(self.score))
        else:
            self.rightrate=(np.count_nonzero(self.current==-2))/float(self.allnumber)
            return -1
    
    def try_cannot_solve(self):
        while(self.cannotsolve.is_empty()==False):
            _,_,item=self.cannotsolve.pop()
            if(self.visited[tuple(item)]==1):
                continue
            #print(item)
            possibleMineList=self.get_neighbor(item[0],item[1],-2)
            for onemine in possibleMineList:
                if( self.try_one_block(onemine[0],onemine[1])==False):
                    #self.scan_nodelist()
                    return
                else:
                    #self.scan_nodelist()
                    return

            
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
            if(self.object[xx,yy]==-1):
                self.score-=1
        
        self.visited[self.current==0]=1
        
            
        # not zero, push in
        
            
    # found a new mine
    def update_newmine(self,xx,yy):
        #print("mine",xx,yy)

        #mg.drawboard(self.current)
        if(self.visited[xx,yy]==1):
            return 
        if(self.object[xx,yy]!=-1):
            print("updatewrong")
            #self.score-=1
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
            #mg.drawboard(self.current)
            #print(xx,yy)
            self.score-=1
            self.update_newmine(xx,yy)
            print("trywrong")
            return False
            #raise Exception("wrong step! game over!",xx,yy) 
        else:
            self.current[xx,yy]=blockValue
            neighborlist=self.get_not_neighbor(xx,yy,-2)
            for item in neighborlist:
                if(self.visited[tuple(item)]<0):
                    self.nodelist.push(self.current,item)
              
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
# 
# y=[]
# x=np.array(range(30,40,2))
# 
# for i in x:
#     temp=[]
#     for j in range(30):
#         mg=MineGenerator(x=i,y=i,p=0.1)
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
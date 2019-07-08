#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:47:28 2019

@author: ciuji
"""
import heapq

class Node:
    def __init__(self,i=0,j=0):
        self.i=i
        self.j=j
        self.loc=(self.i,self.j)
        #self.loc=[i,j]


class Stack:
    def __init__(self):
        self.stack=[]
    
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        return self.stack.pop()
    
    def push(self,node):
        self.stack.append(node)
        
    def top(self):
        return self.stack[-1]


class PriorityQueue:
    def __init__(self):
        self.heap=[]
        self.index=0
        
    def push(self,node,priority,path):
        heapq.heappush(self.heap,(priority,self.index,node,path))
        self.index-=1
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return self.heap==[]
        
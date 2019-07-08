#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:58:55 2019

@author: Himmel
"""
import structure
import numpy as np
import matplotlib.pyplot as plt
import random

class Maze:
    def __init__(self, length, width, initialP):
        self.length = length
        self.width = width
        self.maze = {}
        for i in range(length):
            for j in range(width):
                self.maze[(i, j)] = initialP
        self.maze[(0, 0)] = -1
        self.maze[(length - 1, width - 1)] = -1
        self.start = (0, 0)
        self.goal = (length - 1, width - 1)
        
    def isWall(self, state):
        return self.maze[state] == 0
        
    def getSuccessor(self, state):
        '''input:
            - state: a tuple stands for coordinates
           output:
            - a list of successor,
            - a successor contains the neighbor's cooridinates and the action 
              for current state to go there, and the cost(distance) between
        '''
        successors = []
        (x, y) = state
        if not self.isWall((x - 1, y)):
            successors.append(((x - 1, y), "west", 1))
        if not self.isWall((x, y - 1)):
            successors.append(((x, y - 1), "north", 1))
        if not self.isWall((x + 1, y)):
            successors.append(((x + 1, y), "east", 1))
        if not self.isWall((x, y + 1)):
            successors.append(((x, y + 1), "south", 1))
        return successors
        
    def isGoalState(self, state):
        '''
            check if the current state is the goal state
        '''
        return state == self.goal
    
    def DFS(self):
        '''
            Using stack as the data structure
            return when we pop the goal state
            Output:
                a series of actions
        '''
        stack = structure.Stack()
        stack.push((self.start, []))
        visited = {}
        while not stack.isEmpty():
            (state, path) = stack.pop()
            if self.isGoalState(state):
                return path
            for successor in self.getSuccessor(state):
                (neighbor, action, _) = successor
                if neighbor not in visited.keys():
                    stack.append((neighbor, path + [action]))
            if state not in visited.keys():
                visited[state] = True
            if stack.isEmpty():
                return path
                
    def BFS(self):
        '''
            Using queue as the data structure
            return when we meet the goal state
            Output:
                a series of actions
        '''
        queue = structure.Queue()
        queue.enqueue((self.start, []))
        visited = {}
        while not queue.isEmpty():
            (state, path) = queue.dequeue()
            for successor in self.getSuccessor(state):
                (neighbor, action, _) = successor
                if self.isGoalState(neighbor):
                    return path + [action]
                elif neighbor not in visited.keys():
                    queue.enqueue((neighbor, path + [action]))
            if state not in visited.keys():
                visited[state] = True
            if queue.isEmpty():
                return path
    
    def manhattanDistance(self, state):
        (x1, y1), (x2, y2) = state, self.goal
        return abs(x2 - x1) + abs(y2 - y1)
    
    def euclideanDistance(self, state):
        (x1, y1), (x2, y2) = state, self.goal
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
    
    def Astar(self, heuristic):
        '''
           input:
             - heuristic : a function which gives us the estimated value
           Using min-heap (priority queue) as data structure
           return when we pop the goal state
           Output:
                a series of actions
        '''
        Heap = structure.PriorityQueue()
        Heap.heap = [(0, 1, (self.start, [], self.heuristic(self.start)))]
        visited = {}
        while not Heap.isEmpty():
            (state, path, priority) = Heap.pop()
            if self.isGoalState(state):
                return path
            for successor in self.getSuccessor(state):
                (neighbor, action, cost) = successor
                if neighbor not in visited.keys():
                    visited[neighbor[0]] = True
                    Heap.update((neighbor, path + [action], priority + cost), priority + cost + self.heuristic(neighbor))
            if state not in visited.keys():
                visited[state] = True
            if Heap.isEmpty():        
                return path
    
    def getPath(self, Search, heuristic = None):
        '''
           Input: a search function, which may have heuristic function 
           
           Turning the series of actions into coordinates 
           
           Output: a list of states               
        '''
        path = []
        if heuristic == None:
            path = self.Search()
        else:
            path = self.Search(heuristic)
        states = [self.start]
        for action in path:
            (x, y) = states[-1]
            if action == "west":
                states.append((x - 1, y))
            elif action == "north":
                states.append((x, y - 1))
            elif action == "east":
                states.append((x + 1, y))
            elif action == "south":
                states.append((x, y + 1))
        return states
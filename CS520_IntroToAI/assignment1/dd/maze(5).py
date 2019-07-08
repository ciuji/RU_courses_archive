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
import math
e = math.e

def manhattanDistance(state, goal):
        (x1, y1), (x2, y2) = state, goal
        return abs(x2 - x1) + abs(y2 - y1)
    
def euclideanDistance(state, goal):
        (x1, y1), (x2, y2) = state, goal
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5

class Maze:
    def __init__(self, length, width, initialP):
        self.length = length
        self.width = width
        self.maze = {}
        self.initialP = initialP
        self.numerator = -(self.length + self.width)
        self.denominator = length * width -2
        self.probability = initialP * (e)**(self.numerator/self.denominator)
        for i in range(length):
            for j in range(width):
                self.maze[(i, j)] = -1
        self.start = (0, 0)
        self.goal = (length - 1, width - 1)
        
    def generateMaze(self):
        '''
            (x, y) -> 0 : empty
            (x, y) -> 1 : obstruction
        '''
        for coordinates in self.maze.keys():
            if coordinates != self.start and coordinates != self.goal:
                p = random.random()
                if p < self.probability:
                    self.maze[coordinates] = 1
                    self.denominator -= 1
                else:
                    self.maze[coordinates] = 0
                    self.numerator += 1
            self.probability = self.initialP * (e)**(self.numerator/self.denominator)
    
            
    def printMaze(self, Search, heuristic = None):
        path = self.getPath(Search, heuristic)
        mazeMap = np.zeros((self.length, self.width), dtype = int)
        for (x, y) in self.maze.keys():
            mazeMap[x, y] = self.maze[(x, y)]
        for (x, y) in path:
            mazeMap[x, y] = -1
        plt.figure(figsize=(5,5))
        plt.pcolor(mazeMap[::-1],edgecolors='black',cmap='Blues', linewidths=2)
        plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.show()
        
    def isWall(self, state):
        return self.maze[state] == 1
        
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
        if x - 1 >= 0 and not self.isWall((x - 1, y)):
            successors.append(((x - 1, y), "west", 1))
        if y - 1 >= 0 and not self.isWall((x, y - 1)):
            successors.append(((x, y - 1), "north", 1))
        if x + 1 < self.length and not self.isWall((x + 1, y)):
            successors.append(((x + 1, y), "east", 1))
        if y + 1 < self.width and not self.isWall((x, y + 1)):
            successors.append(((x, y + 1), "south", 1))
        return successors
        
    def isGoalState(self, state):
        '''
            check if the current state is the goal state
        '''
        return state == self.goal
    
    
    def getPath(self, Search, heuristic = None):
        '''
           Input: a search function, which may have heuristic function 
           
           Turning the series of actions into coordinates 
           
           Output: a list of states               
        '''
        path = []
        if heuristic == None:
            path = Search(self)
        else:
            path = Search(self, heuristic)
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
    
    def simplify(self, fraction):
        '''
           input: 
            fraction: a number ∈ [0,1]
            fraction == 1: empty maze
            fraction == 0: no changes
           output:
            a copy of the maze, which strip out a fraction of the obstructions
        '''
        
        simple = Maze(self.length, self.width, 0)
        simple.maze = self.maze.copy()
        wallState = []
        numberOfWall = 0
        for state in self.maze.keys():
            if self.maze[state] == 1:
                wallState.append(state)
                numberOfWall += 1
        random.shuffle(wallState)
        stripNumber = math.ceil(fraction * numberOfWall)
        for state in wallState:
            simple.maze[state] = 0
            stripNumber -= 1
            if stripNumber == 0:
                break
        return simple
 

        
        

def DFS(maze):
        '''
            Using stack as the data structure
            return when we pop the goal state
            Output:
                a series of actions
        '''
        stack = structure.Stack()
        stack.push((maze.start, []))
        visited = {}
        while not stack.isEmpty():
            (state, path) = stack.pop()
            if maze.isGoalState(state):
                #print("Reach the goal!")
                return path
            for successor in maze.getSuccessor(state):
                (neighbor, action, _) = successor
                if neighbor not in visited.keys():
                    stack.push((neighbor, path + [action]))
            if state not in visited.keys():
                visited[state] = True
            if stack.isEmpty():
                #print("There is no such a path!")
                return path
                
def BFS(maze):
        '''
            Using queue as the data structure
            return when we meet the goal state
            Output:
                a series of actions
        '''
        queue = structure.Queue()
        queue.enqueue((maze.start, []))
        visited = {}
        while not queue.isEmpty():
            (state, path) = queue.dequeue()
            for successor in maze.getSuccessor(state):
                (neighbor, action, _) = successor
                if maze.isGoalState(neighbor):
                    #print("Reach the goal!")
                    return path + [action]
                elif neighbor not in visited.keys():
                    queue.enqueue((neighbor, path + [action]))
            if state not in visited.keys():
                visited[state] = True
            if queue.isEmpty():
                #print("There is no such a path!")
                return path
    
    
    
def Astar(maze, heuristic):
        '''
           input:
             - heuristic : a function which gives us the estimated value
           Using min-heap (priority queue) as data structure
           return when we pop the goal state
           Output:
                a series of actions
        '''
        Heap = structure.PriorityQueue()
        Heap.heap = [(0, 1, (maze.start, [], heuristic(maze.start, maze.goal)))]
        visited = {}
        while not Heap.isEmpty():
            (state, path, priority) = Heap.pop()
            if maze.isGoalState(state):
                #print("Reach the goal!")
                return path
            for successor in maze.getSuccessor(state):
                (neighbor, action, cost) = successor
                if neighbor not in visited.keys():
                    visited[neighbor[0]] = True
                    Heap.update((neighbor, path + [action], priority + cost), priority + cost + heuristic(neighbor, maze.goal))
            if state not in visited.keys():
                visited[state] = True
            if Heap.isEmpty(): 
                #print("There is no such a path!")
                return path
    
 
def approximateDistance(maze):
    return len(BFS(maze))

def Astar_Thinning(maze):
    Heap = structure.PriorityQueue()
    Heap.heap = [(0, 1, (maze.start, [], approximateDistance(maze)))]
    simple = maze.simplify(0.3)
    simple.printMaze(Astar, manhattanDistance)
    visited = {}
    while not Heap.isEmpty():
        (state, path, priority) = Heap.pop()
        if maze.isGoalState(state):
            #print("Reach the goal!")
            return path
        simple.start = state
        for successor in maze.getSuccessor(state):
            (neighbor, action, cost) = successor
            if neighbor not in visited.keys():
                visited[neighbor[0]] = True
                Heap.update((neighbor, path + [action], priority + cost), priority + cost + approximateDistance(simple))
        if state not in visited.keys():
            visited[state] = True
        if Heap.isEmpty(): 
            #print("There is no such a path!")
            return path    
        

    
        

maze = Maze(10, 10, 0.3)
maze.generateMaze()
maze.printMaze(BFS)
maze.printMaze(DFS)
maze.printMaze(Astar, manhattanDistance)
maze.printMaze(Astar, euclideanDistance)
maze.printMaze(Astar_Thinning)
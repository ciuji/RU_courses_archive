#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 23:05:35 2019

@author: Himmel
"""
from maze import Maze
import random
import structure

class FireMaze(Maze):
    def __init__(self,length, width, initialP):
        '''
            initialize the number of the fire spots
        '''
        Maze.__init__(self, length, width, initialP)
        self.fireSpots = []
        self.probabilityDistribution = {}
        for state in self.maze.keys():
            self.probabilityDistribution[state] = 0
        self.utility = {}
    
    def setFire(self):
        '''
            randomly distribute the fire spots
        '''
        self.fireSpots.append((self.length - 1, 0))
        self.probabilityDistribution[(self.length - 1, 0)] = 1
        
            
    def fireProbability(self, state):
        '''
            Input:
                - a state coordinate
            Output:
                - a number between 0 ~ 1 indicates the probability of the state
                  changing to fire state
        '''
        
        (x, y) = state
        if self.maze[state] == 2:
            self.probabilityDistribution[state] = 1
            if state not in self.fireSpots:
                self.fireSpots.append(state)
            return 1
        
        probFire = 0
        if x - 1 >= 0:
            probFire += self.probabilityDistribution[(x - 1, y)]
        if y - 1 >= 0:
            probFire += self.probabilityDistribution[(x, y - 1)]
        if x + 1 < self.length:
            probFire += self.probabilityDistribution[(x + 1, y)]
        if y + 1 < self.width:
            probFire += self.probabilityDistribution[(x, y + 1)]
        return 1 - (0.5)**(probFire)
        '''
        distances = []
        for spot in self.fireSpots:
            distances.append(manhattanDistance(spot, state) + euclideanDistance(spot, state))
        distance = min(distances) 
        return (1/e) ** (distance)
        '''
    def getNeighbor(self, state):
        '''
            Input: a given state with (x, y) as its coordinates
            
            Output:
                    the neighborhoods in four directions(n, e, s, w)
        '''
        (x, y) = state
        neighbor = []
        if x - 1 >= 0:
            neighbor.append((x - 1, y))
        if x + 1 < self.length:
            neighbor.append((x + 1, y))
        if y - 1 >= 0:
            neighbor.append((x, y - 1))
        if y + 1 < self.width:
            neighbor.append((x, y + 1))
        return neighbor

    def distributeFire(self):
        '''
            Distribute the fire probability to whole maze
            Using a dictionary to keep memorize the probability in each state
            Update probability when we spread fire
        '''
        probabilityLevel = self.fireSpots.copy()
        #print(probabilityLevel)
        #return None
        newProbability = {}
        for state in self.fireSpots:
            newProbability[state] = 1
        #n = 10
        for state in self.probabilityDistribution.keys():
            if self.probabilityDistribution[state] != 1:
                self.probabilityDistribution[state] = 0
        while len(newProbability) < len(self.probabilityDistribution):
            amount = len(probabilityLevel)
            for i in range(amount):
                state = probabilityLevel[i]
                #print('state:', state, 'neighbor:', self.getNeighbor(state))
                #print('current state ', state, 'has probability', self.probabilityDistribution[state])
                for neighbor in self.getNeighbor(state):
                    #print('neighbor', neighbor, 'has probability', self.probabilityDistribution[neighbor])
                    if self.probabilityDistribution[neighbor] < self.probabilityDistribution[state] and neighbor not in newProbability.keys():
                        newProbability[neighbor] = self.fireProbability(neighbor)
                        probabilityLevel.append(neighbor)
                        #print('changed neighbor:', neighbor,'now has probabilit', self.probabilityDistribution[neighbor] ,'but will have probability:', newProbability[neighbor])
            for location in newProbability.keys():
                self.probabilityDistribution[location] = newProbability[location]
            probabilityLevel = probabilityLevel[amount:]
            #print(self.probabilityDistribution)
            
            
            
        
    def spreadFire(self):
        '''
            Spread fire from the fire spots
        '''
        #print(1)
        #print(self.probabilityDistribution)
        newSpots = []
        for state in self.fireSpots:
            for neighbor in self.getNeighbor(state):
                if neighbor not in self.fireSpots and random.random() > self.fireProbability(neighbor) and not self.isWall(neighbor):
                    self.probabilityDistribution[neighbor] = 1
                    if neighbor not in newSpots:
                        newSpots.append(neighbor)
        self.fireSpots += newSpots            
        #print(1)
        #print(self.probabilityDistribution)
    
        
def FireBFS(fireMaze, state):
    '''
        Using BFS to find state's utility
        utility is cumulative probability times penalty, or utility is award based on size of maze
'''
    queue = structure.Queue()
    queue.enqueue((state, []))
    visited = {}
    states = [state]
    if fireMaze.isGoalState(state):
        return (fireMaze.length + fireMaze.width) ** 2
    elif state in fireMaze.fireSpots:
        return -100
    while not queue.isEmpty():
        (state, path) = queue.dequeue()
        for successor in fireMaze.getSuccessor(state):
            (neighbor, action, _) = successor
            if fireMaze.isGoalState(neighbor) or neighbor in fireMaze.fireSpots:
                #print("Reach the goal!")
                utility = 1
                cost = 0
                for action in path + [action]:
                    (x, y) = states[-1]
                    if action == "west":
                        states.append((x - 1, y))
                        utility *= fireMaze.probabilityDistribution[(x - 1, y)]
                    elif action == "north":
                        states.append((x, y - 1))
                        utility *= fireMaze.probabilityDistribution[(x, y - 1)]
                    elif action == "east":
                        states.append((x + 1, y))
                        utility *= fireMaze.probabilityDistribution[(x + 1, y)]
                    elif action == "south":
                        utility *= fireMaze.probabilityDistribution[(x, y + 1)]
                        states.append((x, y + 1))
                    cost -= 1
                if states[-1] in fireMaze.fireSpots:
                    utility *= (-100)
                elif fireMaze.isGoalState(states[-1]):                       
                    utility = (fireMaze.length + fireMaze.width) ** 2
                utility += cost
                return utility
            elif neighbor not in visited.keys():
                queue.enqueue((neighbor, path + [action]))
        if state not in visited.keys():
            visited[state] = True
    return 0
        
def makeDecision(fireMaze):
    '''
    make decision (local optimal) by choose the max utility in a state's neighborhood
    '''
    visited = [fireMaze.start]
    path = []
    while True:
        state = visited[-1]
        v = -2 ** 64
        print('number of fire spots:', len(fireMaze.fireSpots))
        print('---------')
        print(fireMaze.fireSpots)
        print('---------')
        print('current state is', state, 'the probability of being fire is', fireMaze.probabilityDistribution[state])
        if fireMaze.isGoalState(state):
            print("You escape the fire maze!")
            return path
        elif state in fireMaze.fireSpots:
            print("You are burned")
            return path
        optimalAction = ''
        nextState = state
        for successor in fireMaze.getSuccessor(state):
            (neighbor, action, _) = successor
            print('utility of', neighbor, ' is ', FireBFS(fireMaze, neighbor))
            if neighbor not in visited and v < FireBFS(fireMaze, neighbor):
                v = FireBFS(fireMaze, neighbor)
                nextState = neighbor
                optimalAction = action
        print(v)
        print('next State is', nextState)
        if nextState == state:
            print('You will die anyway')
            return []
        if v == 0:
            print('There is not a path to escape!')
            return []
        visited += [nextState]
        if optimalAction != '':
            path.append(optimalAction)
        fireMaze.spreadFire()
        fireMaze.distributeFire()
                

firemaze = FireMaze(10, 10, 0.2)
firemaze.generateMaze()
firemaze.setFire()
firemaze.distributeFire()
print(makeDecision(firemaze))        
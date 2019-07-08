#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:45:16 2019

@author: ciuji
"""

import random
import numpy as np
import matplotlib.pyplot as plt

class Map:
    def __init__(self, size=20):
        self.size = size;
        self.terrain = {}
        for x in range(self.size):
            for y in range(self.size):
                self.terrain[(x, y)] = 0
        self.target = (0,0)
        self.typeReport = ["", ""]
        
        
    def generateMap(self):
        locations = list(self.terrain.keys())
        random.shuffle(locations)
        for coordinate in locations:
            probability = random.random()
            if probability <= 0.2:
                self.terrain[coordinate] = 1000 #flat
            elif probability <= 0.5:
                self.terrain[coordinate] = 800 #hilly
            elif probability <= 0.8:
                self.terrain[coordinate] = 500 #forested
            else:
                self.terrain[coordinate] = 0   #cave
        random.shuffle(locations)
        self.target = random.choice(locations)
    
    def printMap(self):
        graph = np.zeros((self.size, self.size), dtype = int)
        for (x, y) in self.terrain.keys():
            graph[x, y] = self.terrain[(x, y)]
        plt.figure(figsize=(10,10))
        plt.pcolor(graph[::-1],edgecolors='black',cmap='gist_earth', linewidths=2)
        plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.show()
    
    def targetMove(self):
        choice = []
        (x, y) = self.target
        if x - 1 >= 0:
            choice.append((x - 1, y))
        if y - 1 >= 0:
            choice.append((x, y - 1))
        if x + 1 < self.size:
            choice.append((x + 1, y))
        if y + 1 < self.size:
            choice.append((x, y + 1))
        self.target = random.choice(choice)
        self.typeReport = [self.terrain[(x, y)], self.terrain[self.target]]

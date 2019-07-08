#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:24:54 2019

@author: Himmel
"""

import heapq

class Stack:
    def __init__(self):
        self.list = []
        
    def push(self, item):
        self.list.append(item)
        
    def pop(self):
        return self.list.pop()
    
    def isEmpty(self):
        return self.list == []
    
class Queue:
    def __init__(self):
        self.list = []
        
    def enqueue(self, item):
        self.list.insert(0, item)
        
    def dequeue(self):
        return self.list.pop()
        
    def isEmpty(self):
        return self.list == []
    
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)
    

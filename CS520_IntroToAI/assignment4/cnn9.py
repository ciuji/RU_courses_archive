#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:31:38 2019

@author: ciuji
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from PIL import Image

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.21, 0.72, 0.07])

lena=mpimg.imread('data/1.jpg')
gray = rgb2gray(lena)    
# 也可以用 plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.imshow(gray, cmap='Greys_r')
plt.axis('off')
plt.show()
'''
I = Image.open('data/1.jpg')
I.show()
L = I.convert('L')
L.show()
'''
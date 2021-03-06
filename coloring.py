# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:13:47 2020

@author: jfarm
"""

from Grid import ColorGrid
from BinaryTree import BinaryTree
from Sidewinder import Sidewinder

grid = ColorGrid(2,2)

BinaryTree.on(grid)

start = grid[int(grid.rows / 2)][int(grid.columns / 2)]

grid.setDistances(grid.findDistances(start)) 

print(grid)

grid.toImage()
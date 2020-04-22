# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:23:00 2020

@author: jfarm
"""

from BinaryTree import BinaryTree
from Grid import ColorGrid

grid = ColorGrid(10,10)

BinaryTree.on(grid)
start = grid[0][0]

distances = grid.findDistances(start)

maxDistance, newStart = distances.maxDistance()

newDistances = grid.findDistances(newStart)
maxDist, goal = newDistances.maxDistance()

grid.setDistances(newDistances.pathTo(goal))

print(grid)

grid.toImage()

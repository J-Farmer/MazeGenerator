# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:37:45 2020

@author: jfarm
"""


from BinaryTree import BinaryTree
from Grid import DistanceGrid

grid = DistanceGrid(10,10)

BinaryTree.on(grid)
start = grid[0][0]

distances = start.distances()

maxDistance, newStart = distances.maxDistance()

newDistances = newStart.distances()
maxDist, goal = newDistances.maxDistance()

grid.distances = newDistances.pathTo(goal)

print(grid)
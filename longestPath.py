# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:55:34 2020

@author: jfarm
"""


from Grid import DistanceGrid
from BinaryTree import BinaryTree

grid = DistanceGrid(5,5)

BinaryTree.on(grid)

print(grid)

start = grid[0][0]

distances = start.distances()

grid.distances = distances

print(grid)

distance, newStart = distances.maxDistance()

newDistances = newStart.distances()

distances, goal = newDistances.maxDistance()

grid.distances = newDistances.pathTo(goal)

print(grid)
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

distances = grid.findDistances(start)

grid.setDistances(distances)

print(grid)

distance, newStart = distances.maxDistance()

newDistances = grid.findDistances(newStart)

distances, goal = newDistances.maxDistance()

grid.distances = newDistances.pathTo(goal)

print(grid)
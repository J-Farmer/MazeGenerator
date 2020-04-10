# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:13:47 2020

@author: jfarm
"""

from Grid import ColorGrid
from BinaryTree import BinaryTree
from Sidewinder import Sidewinder

grid = ColorGrid(25,25)

Sidewinder.on(grid)

start = grid[int(grid.rows / 2)][int(grid.columns / 2)]

grid.setDistances(start.distances())

grid.toImage()
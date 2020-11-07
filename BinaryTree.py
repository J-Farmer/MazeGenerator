# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:38:11 2020

@author: jfarm
"""
from random import choice

class BinaryTree():
    @staticmethod
    def on(grid):
        for row in grid.grid:
            for cell in row:
                neighbors = []
                for n in cell.neighbors:
                    if cell.neighbors[n] == None: continue
                    else:
                        if n == "east" or n == "north":
                            neighbors.append(cell.neighbors[n])
                            
                if not neighbors: continue
                else: cell.link(choice(neighbors))
                
        return grid
    
if __name__ == "__main__":
    from GridTest import Grid
    
    g = BinaryTree.on(Grid(100,100))
    
    print(g)
    
    g.toImage()
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:43:56 2020

@author: jfarm
"""


from Grid import *
from random import choice
from Cell import *

class Wilson():
    
    @staticmethod
    def on(grid):
        unvisited = []
        for row in grid.grid:
            for cell in row:
                unvisited.append(cell)
        
        first = choice(unvisited)
        unvisited.remove(cell)
        
        while unvisited:
            cell = choice(unvisited)
            path = [cell]
            
            while cell in unvisited:
                cell = cell.getRandomNeighbor()
                if cell in path: 
                    position = path.index(cell)
                    path = path[0:position+1]
                else:
                    path.append(cell)

            for i in range(0, len(path)-1):
                path[i].link(path[i+1])
                unvisited.remove(path[i])
        
        return grid
                    
                    
                    
if __name__ == "__main__":
    
    g = ColorGrid(10,10)
    
    Wilson.on(g)
    
    g.setDistances(g.findDistances(g[g.rows // 2][g.columns // 2]))
        
    print(g)
        
    g.toImage()

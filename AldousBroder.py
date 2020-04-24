# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:02:49 2020

@author: jfarm
"""
from Grid import *
from random import choice

class AldousBroder():
    
    @staticmethod
    def on(grid):
        cell = grid.getRandomCell()
        unvisited = grid.size - 1
        
        while unvisited > 0:
            neighbor = cell.getRandomNeighbor()
            
            if not any(neighbor.links.values()):
                cell.link(neighbor)
                unvisited -= 1
            
            cell = neighbor
            
        return grid
    
    
if __name__ == "__main__":
     
    for i in range(0,6):
    
        g = AldousBroder.on(ColorGrid(10,10))
        
        g.setDistances(g.findDistances(g[g.rows // 2][g.columns // 2]))
        
        print(g)
        
        g.toImage()
                
        
        
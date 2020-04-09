# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:25:00 2020

@author: jfarm
"""
from random import randint
from random import choice
class Sidewinder():
    @staticmethod
    def on(grid):
        
        for row in grid.grid:
            run = []
            for cell in row:
                run.append(cell)
                
                atEastBound = (cell.neighbors['east'] == None)
                atNorthBound = (cell.neighbors['north'] == None)
                
                shouldCloseOut = atEastBound or (not atNorthBound and randint(0,1) == 0)
                
                if shouldCloseOut:
                    member = choice(run)
                    if member.neighbors['north'] != None:
                        member.link(member.neighbors['north'])
                    run.clear()
                else: cell.link(cell.neighbors["east"])
        
        
        return grid 


if __name__ == "__main__":
    from Grid import Grid
    
    g = Sidewinder.on(Grid(10,10))
    
    print(g)
    
    g.toImage()
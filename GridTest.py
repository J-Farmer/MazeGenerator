# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:07:18 2020

@author: jfarm
"""

from Cell import Cell

from random import randint
from PIL import Image, ImageDraw
from Distances import Distances

class Grid():
    
    def prepareGrid(self):
        grid = []
        for row in range(self.rows):
            row = []
            for col in range(self.columns):
                row.append(Cell(col, len(row), self.cellSize))
            grid.append(row)

        return grid
    
    def getRandomCell(self):
        x = randint(0, self.rows - 1)
        y = randint(0, self.columns - 1)
        
        return self.grid[x][y]

    def configureCells(self):
        for row in range(self.rows):
            for col in range(self.columns):
                
                cell = self.grid[row][col]
                
                
                if col == 0:
                    cell.neighbors["west"]=None
                    cell.neighbors["east"]=self.grid[row][col+1]
                elif col == self.columns-1:
                    cell.neighbors["west"]=self.grid[row][col-1]
                    cell.neighbors["east"]=None
                else:
                    cell.neighbors["west"]=self.grid[row][col-1]
                    cell.neighbors["east"]=self.grid[row][col+1]

             
                if row == 0:
                    cell.neighbors["north"]=None
                    cell.neighbors["south"]=self.grid[row+1][col]

                elif row==self.rows-1:
                    cell.neighbors["north"]=self.grid[row-1][col]
                    cell.neighbors["south"]=None
                else:
                    cell.neighbors["north"]=self.grid[row-1][col]
                    cell.neighbors["south"]=self.grid[row+1][col]
                
                '''
                if col == 0:
                    cell.neighbors["west"]=None
                else:
                    cell.neighbors["west"]=self.grid[row][col-1]

                if col == self.columns-1:
                    cell.neighbors["east"]=None
                else:
                    cell.neighbors["east"]=self.grid[row][col+1]
                
                if row == 0:
                    cell.neighbors["north"]=None
                else:
                    cell.neighbors["north"]=self.grid[row-1][col]
                
                if row == self.rows-1:
                    cell.neighbors["south"]=None
                else:
                    cell.neighbors["south"]=self.grid[row+1][col]
                
                '''
                '''
                if row == 0 and col == 0:
                    cell.neighbors["north"] = None
                    cell.neighbors["west"] = None
                    cell.neighbors["east"] = self.grid[row][col+1]
                    cell.neighbors["south"] = self.grid[row+1][col]
                    
                elif row == 0 and col == self.columns - 1: 
                    cell.neighbors["north"] = None
                    cell.neighbors["west"] = self.grid[row][col-1]
                    cell.neighbors["east"] = None
                    cell.neighbors["south"] = self.grid[row + 1][col]
                    
                elif row == self.rows - 1 and col == self.columns - 1:
                    cell.neighbors["north"] = self.grid[row-1][col]
                    cell.neighbors["west"] = self.grid[row][col-1]
                    cell.neighbors["east"] = None
                    cell.neighbors["south"] = None
                    
                elif row == self.rows - 1 and col == 0:
                    cell.neighbors["north"] = self.grid[row-1][col]
                    cell.neighbors["west"] = None
                    cell.neighbors["east"] = self.grid[row][col+1]
                    cell.neighbors["south"] = None

                elif row == 0:
                    cell.neighbors["north"] = None
                    cell.neighbors["west"] = self.grid[row][col-1]
                    cell.neighbors["east"] = self.grid[row][col+1]
                    cell.neighbors["south"] = self.grid[row+1][col]

                elif row == self.rows - 1:
                    cell.neighbors["north"] = self.grid[row-1][col]
                    cell.neighbors["west"] = self.grid[row][col-1]
                    cell.neighbors["east"] = self.grid[row][col+1]
                    cell.neighbors["south"] = None

                elif col == 0:
                    cell.neighbors["north"] = self.grid[row-1][col]
                    cell.neighbors["west"] = None
                    cell.neighbors["east"] = self.grid[row][col+1]
                    cell.neighbors["south"] = self.grid[row+1][col]

                elif col == self.columns - 1:
                    cell.neighbors["north"] = self.grid[row-1][col]
                    cell.neighbors["west"] = self.grid[row][col-1]
                    cell.neighbors["east"] = None
                    cell.neighbors["south"] = self.grid[row+1][col]
                                
                else:
                    cell.neighbors["north"] = self.grid[row-1][col]
                    cell.neighbors["west"] = self.grid[row][col-1]
                    cell.neighbors["east"] = self.grid[row][col+1]
                    cell.neighbors["south"] = self.grid[row+1][col]
                '''
    
    def __init__(self, rows, columns, cellSize=50):
        self.rows = rows
        self.columns = columns
        self.cellSize = cellSize
        self.size = self.rows * self.columns
        self.grid = self.prepareGrid()
        self.configureCells()
        
    def __getitem__(self, idx):
        return self.grid[idx]
    
    def __setitem__(self, idx, cell):
        self.grid[idx] = cell
        
    def contentsOf(self, cell):
        return " "
    
    def backgroundColor(self,cell):
        return None
    
    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        
        for row in self.grid:
            top = "|"
            bottom = "+"
            
            for cell in row:
                body = f" {self.contentsOf(cell)} "
                eastBound = southBound = ""
                
                if cell.isLinked(cell.neighbors["east"]): 
                    eastBound = " "
                else: 
                    eastBound = "|"
                top += body + eastBound
                
                if cell.isLinked(cell.neighbors["south"]): 
                    southBound = "   "
                else: 
                    southBound = "---"
                corner = "+"
                bottom += southBound + corner
            
            output += top + "\n"
            output += bottom + "\n"
        
        return output
          
    def toImage(self, name=None):
        
        if name == None:
            print("Displaying Maze!")
        else:
            print(f"Saving maze to {name}")
            
        imWidth = self.cellSize * self.columns
        imHeight = self.cellSize * self.rows
        
        bg =    (255,255,255)
        wall =  (0,0,0)
        
        im =    Image.new("RGB", (imWidth + 1, imHeight + 1), color = bg)
        draw =  ImageDraw.Draw(im)
        
        for row in range(self.rows):
            for col in range(self.columns):
                    
                cell = self.grid[row][col]
                    
                x1 = col * self.cellSize
                x2 = (col + 1) * self.cellSize
                y1 = row * self.cellSize
                y2 = (row + 1) * self.cellSize

                        
                if(cell.neighbors["north"] == None):
                    draw.line((x1,y1, x2, y1), fill=wall)

                if(cell.neighbors["west"] == None):
                    draw.line((x1,y1, x1, y2), fill=wall)
                
                if(not(cell.isLinked(cell.neighbors["east"]))):
                   draw.line((x2, y1, x2, y2), fill=wall)
                   
                if(not(cell.isLinked(cell.neighbors["south"]))):
                   draw.line((x1, y2, x2, y2), fill=wall)

        
        if(name == None):
            im.show()
            return
        
        im.save(name)           
 
######################################################################################################################
               
class DistanceGrid(Grid):
    
    def __init__(self, row, col):
        self.distances = None
        
        super().__init__(row, col)
    
    def contentsOf(self, cell):
        if self.distances and (cell in self.distances.cells):
            return self.toBase62(self.distances[cell])
        else:    
            return super().contentsOf(cell) 
        
    def getDistances(self):
        return self.distances
        
    def setDistances(self, distances):
        self.distances = distances

    def toBase36(self,num):
        
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
        
        if(type(num) is not int):
            raise TypeError("Number must be an integer!")
        if(num < 0):
            raise ValueError("Number must be positve!")
            
        idx = num % len(alphabet)
        
        return alphabet[idx]
    
    def toBase62(self, num):
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        string = ""
            
        if(type(num) is not int):
            raise TypeError("Number must be an integer!")
        if(num < 0):
            raise ValueError("Number must be positve!")
        if(num == 0):
            return "0"
        
        while num:
            idx = num % len(alphabet)
            string += alphabet[idx]
            num //= 62
            
        return string[::-1]
    
    def findDistances(self, startCell):
        dis = Distances(startCell)
        unvisited = [startCell]
        
        while unvisited:
            notSeen = []
            
            for cell in unvisited:
                for k in cell.linkedCells(dir=False):
                    if(k in dis.cells):
                        continue
                    else:
                        dis[k] = dis[cell] + 1
                        notSeen.append(k)
            unvisited = notSeen
                
        return dis

######################################################################################################################
        
class ColorGrid(DistanceGrid):
    
    def __init__(self, row, col):
        self.distances = None
        self.max = None
        super().__init__(row, col)
        
    def getDistances(self):
        return self.distances
        
    def setDistances(self, distances, calculateMax=True):
        self.distances = distances
        
        if calculateMax:
            self.max = self.distances.maxDistance()[0]
            
    def backgroundColor(self, cell):
        
        if cell in self.distances.cells:
            distance = self.distances[cell]
        else:
            distance = 0

        intensity = float(self.max - distance) / self.max
        dark = round(255 * intensity)
        bright = 128 + round(127*intensity)
        
        return (dark, dark, bright)
        
    #TODO: Add in code to color the longest path of the cells only.
    def toImage(self, name=None):
        
        if name == None:
            print("Displaying Maze!")
        else:
            print(f"Saving maze to {name}")
            
        imWidth = self.cellSize * self.columns
        imHeight = self.cellSize * self.rows
        
        bg = (255,255,255)
        wall = (255,0,0)
        
        mode = ["background", "wall"]
        
        im = Image.new("RGB", (imHeight + 1, imWidth + 1), color = bg)
        draw = ImageDraw.Draw(im)
        
        for m in mode:
            for row in range(self.rows):
                for col in range(self.columns):
                        
                    cell = self.grid[row][col]
                        
                    x1 = col * self.cellSize
                    x2 = (col + 1) * self.cellSize
                    y1 = row * self.cellSize
                    y2 = (row + 1) * self.cellSize
                    
                    if m == "background":
                        color = self.backgroundColor(cell)
                        draw.rectangle((x1,y1,x2,y2), fill=color, outline=color)
                    else:       
                        if(self.grid[row][col].neighbors["north"] == None):
                            draw.line((x1,y1, x2, y1), fill=wall)
        
                        if(self.grid[row][col].neighbors["west"] == None):
                            draw.line((x1,y1, x1, y2), fill=wall)
                        
                        if(not(self.grid[row][col].isLinked(self.grid[row][col].neighbors["east"]))):
                           draw.line((x2, y1, x2, y2), fill=wall)
                           
                        if(not(self.grid[row][col].isLinked(self.grid[row][col].neighbors["south"]))):
                           draw.line((x1, y2, x2, y2), fill=wall)

        
        if(name == None):
            im.show()
            return
        
        im.save(name)        
     
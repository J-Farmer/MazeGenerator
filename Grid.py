from Cell import Cell

from random import randint
from PIL import Image, ImageDraw

class Grid():
    
    def prepareGrid(self):
        grid = []
        for row in range(self.rows):
            row = []
            for col in range(self.columns):
                row.append(Cell(self.cellSize))
            grid.append(row)

        return grid
    
    def getRandomCell(self):
        x = randint(0, self.rows - 1)
        y = randint(0, self.columns - 1)
        
        return self.grid[x][y], x, y

    def configureCells(self):
        for row in range(self.rows):
            for col in range(self.columns):
                
                cell = self.grid[row][col]
                
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
                    
    
    def __init__(self, rows, columns, cellSize=50):
        self.rows = rows
        self.columns = columns
        self.cellSize = cellSize
        self.grid = self.prepareGrid()
        self.configureCells()
        
    def __getitem__(self, idx):
        return self.grid[idx]
    
    def __setitem__(self, idx, cell):
        self.grid[idx] = cell
        
    def contentsOf(self, cell):
        return " "
    
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
        
        print(f"Converting maze to {name}")
        imWidth = self.cellSize * self.columns
        imHeight = self.cellSize * self.rows
        
        bg = (255,255,255)
        wall = (255,0,0)
        
        im = Image.new("RGB", (imHeight + 1, imWidth + 1), color = bg)
        draw = ImageDraw.Draw(im)
        
        for row in range(self.rows):
            for col in range(self.columns):
                
                x1 = col * self.cellSize
                x2 = (col + 1) * self.cellSize
                y1 = row * self.cellSize
                y2 = (row + 1) * self.cellSize
                
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
                

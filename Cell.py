from Distances import Distances
class Cell():
    def __init__(self, x, y, size=10):
        self.size = size
        self.edgeCell = False
        self.edgeCellType = None
        self.x = x
        self.y = y
        self.walls = {"north": None, "east": None, "south": None, "west": None}
        self.neighbors = {"north": None, "east": None, "south": None, "west": None}
        self.links = {"north": None, "east": None, "south": None, "west": None}
        self.opposite = {"north": "south", "east": "west", "south": "north", "west": "east"}

    def link(self, cell, bidi=True):
        for dir in self.neighbors:
            if self.neighbors[dir] == cell:
                self.links[dir] = True
                if bidi:
                    cell.links[self.opposite[dir]] = True

    def unlink(self, cell, bidi=True):
        for dir in self.neighbors:
            if self.neighbors[dir] == cell:
                self.links[dir] = False
                if bidi:
                    cell.links[self.opposite[dir]] = False

    def linkedCells(self, dir=True):
        linkedCells = []
        if dir:
            for cell in self.links:
                if self.links[cell]:
                    linkedCells.append(cell)
        else:
            for cell in self.links:
                if self.links[cell]:
                    linkedCells.append(self.neighbors[cell])

        if not linkedCells:
            return None
        
        return linkedCells
    
    def isLinked(self, cell):
        for dir in self.neighbors:
            if self.neighbors[dir] == cell and self.links[dir] == True:
                return True
        return False
    
    def distances(self):
        dis = Distances(self)
        unvisited = [self]
        
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
                        
                        
                    

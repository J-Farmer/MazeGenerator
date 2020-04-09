# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:57:18 2020

@author: jfarm
"""
from Grid import Grid

class DistanceGrid(Grid):
    
    def __init__(self, row, col):
        self.distances = None
        
        super().__init__(row, col)
    
    def contentsOf(self, cell):
        if self.distances == None:
            return super().contentsOf(cell)
        
        return self.toBase36(self.distances[cell])
        
    def toBase36(self,num):
        
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
        
        if(type(num) is not int):
            raise TypeError("Number must be an integer!")
        if(num < 0):
            raise ValueError("Number must be positve!")
            
        idx = num % len(alphabet)
        
        return alphabet[idx]
    
    

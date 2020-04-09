# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:49:14 2020

@author: jfarm
"""


class Distances():
    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[root] = 0
        
    def getCells(self):
        return list(self.cells.keys())
    
    def __getitem__(self, key):
        return self.cells[key]
    
    def __setitem__(self, key, distance):
        self.cells[key] = distance
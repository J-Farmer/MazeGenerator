# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:40:19 2020

@author: jfarm
"""
import PIL as p

cellSize = 50
rows = 5
columns = 5

bg = (255,255,255)
wall = (0,0,0)

imHeight = (cellSize * columns)
imWidth = (cellSize * rows) 

img = p.Image.new("RGB", (imHeight + 1, imWidth + 1), color=bg)

draw = p.ImageDraw.Draw(img)

x1 = 4 * cellSize
y1 = 0 * cellSize
x2 = 5 * cellSize
y2 = 1 * cellSize

draw.line((x1,y1, x2, y1), fill=wall)

img.save("Test.png")


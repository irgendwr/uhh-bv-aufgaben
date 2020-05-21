# -*- coding: utf-8 -*-
"""
Aufgabenblatt 3, Aufgabe 3
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

#1. und 2.
prefix = "findetDieFehler/"
ohneFehler = imread(prefix+"ohneFehler.png").astype(np.float)
mitFehler = imread(prefix+"mitFehler.png").astype(np.float)

threshold = 1  # Jede Änderung soll erkannt werden
changes = abs(ohneFehler - mitFehler) > threshold
plt.imshow(changes, cmap="Greys_r")

#3.
changeCoord = np.argwhere(changes == 1)

def unsetNeighbors(x, y):
    if x >= 0 and y >= 0 and x < changes.shape[0] and y < changes.shape[1] and changes[x][y] == True:
        changes[x][y] = False
        unsetNeighbors(x-1, y-1)
        unsetNeighbors(x-1, y  )
        unsetNeighbors(x-1, y+1)
        unsetNeighbors(x  , y-1)
        #unsetNeighbors(x  , y  )
        unsetNeighbors(x  , y+1)
        unsetNeighbors(x+1, y-1)
        unsetNeighbors(x+1, y  )
        unsetNeighbors(x+1, y+1)

changeAreas = 0

#3b.
for coord in changeCoord:
    x = coord[0]
    y = coord[1]
    if changes[x][y]:
        changeAreas += 1
        unsetNeighbors(x, y)

#3c.
print("Anzahl veränderter Bereiche: " + str(changeAreas))
# => Anzahl veränderter Bereiche: 8

# -*- coding: utf-8 -*-
"""
Aufgabenblatt 8, Aufgabe 5
"""

import numpy as np
from skimage.io import imread
import skimage.filters
import matplotlib.pyplot as plt

#1.
opera = imread("./opera.png")

operaBlueOrange = opera[:,:,2] - opera[:,:,1]/2 - opera[:,:,0]/2
operaBlueOrange = operaBlueOrange - np.min(operaBlueOrange)                     # Geringster Wert = 0
operaBlueOrange = (operaBlueOrange / np.max(operaBlueOrange)) * 255             # Normalisierung auf 0-255

operaBlueOrangeGradient = skimage.filters.sobel(operaBlueOrange)

operaBlueOrangeOrientation = np.rad2deg(np.arctan(skimage.filters.sobel_v(operaBlueOrange)/skimage.filters.sobel_h(operaBlueOrange)))
operaBlueOrangeOrientation[np.isnan(operaBlueOrangeOrientation)] = 90           # Setzt alle NaNs auf 90

operaBlueOrangeOrientationNew = np.full_like(operaBlueOrangeOrientation, 90)
operaBlueOrangeOrientationNew[np.logical_and(operaBlueOrangeOrientation >= -67.5, operaBlueOrangeOrientation < -22.5)] = -45
operaBlueOrangeOrientationNew[np.logical_and(operaBlueOrangeOrientation >= -22.5, operaBlueOrangeOrientation < 22.5)] = 0
operaBlueOrangeOrientationNew[np.logical_and(operaBlueOrangeOrientation >= 22.5, operaBlueOrangeOrientation < 65.5)] = 45

result = np.zeros_like(operaBlueOrangeGradient)

plt.figure(1)
plt.imshow(operaBlueOrangeGradient)

#2.
"""
Die Positionen der beiden Nachbarn werden in einen 4-dimensionalen Array gespeichert:
[:,:,0] = Erste y-Position
[:,:,1] = Erste x-Position
[:,:,2] = Zweite y-Position
[:,:,3] = Zweite x-Position

Wäre ein Nachbar außerhalb des Bildes, wird dessen Position auf y=0, x=0 gesetzt.
Eigentlich sollten die Positionen auf null gestellt werden, 
da die Gradientenstärke aber an dieser Stelle 0 beträgt, verändert dies die
Ergebnisse für weitere Berechnungen nicht.

Bei -45° geht die Kante von oben-rechts nach unten-links
Bei 0° geht die Kante von oben nach unten
Bei 45° geht die Kante von oben-links nach unten-rechts
Bei 90° geht die Kante von links nach rechts

Im Nachhinein hätte man das Bild auch mit Nullen padden können, statt die
ganzen if-Abfragen zur Grenzbestimmung zu benutzen... *Wendler voice* Egal!
"""
neighbors = np.zeros((result.shape[0], result.shape[1], 4))

for y in range(result.shape[0]):
    for x in range(result.shape[1]):
        if (operaBlueOrangeOrientationNew[y, x]) == -45:
            if (y > 0 and x < (result.shape[1]-1)):
                neighbors[y, x, 0] = y-1                                        # oben-rechts
                neighbors[y, x, 1] = x+1
            if (y < (result.shape[0]-1) and x > 0):
                neighbors[y, x, 2] = y+1                                        # unten-links
                neighbors[y, x, 3] = x-1
        if (operaBlueOrangeOrientationNew[y, x]) == 0:
            if (y > 0):
                neighbors[y, x, 0] = y-1                                        # oben
                neighbors[y, x, 1] = x
            if (y < (result.shape[0]-1)):
                neighbors[y, x, 2] = y+1                                        # unten
                neighbors[y, x, 3] = x
        if (operaBlueOrangeOrientationNew[y, x]) == 45:
            if (y > 0 and x < 0):
                neighbors[y, x, 0] = y-1                                        # oben-links
                neighbors[y, x, 1] = x-1
            if (y < (result.shape[0]-1) and x > (result.shape[1]-1)):
                neighbors[y, x, 2] = y+1                                        # unten-rechts
                neighbors[y, x, 3] = x+1
        if (operaBlueOrangeOrientationNew[y, x]) == 90:
            if (x > 0):
                neighbors[y, x, 0] = y                                          # links
                neighbors[y, x, 1] = x-1
            if (x < (result.shape[1]-1)):
                neighbors[y, x, 2] = y                                          # rechts
                neighbors[y, x, 3] = x+1

#3.
#compare = np.logical_and(operaBlueOrangeGradient > operaBlueOrangeGradient[int(neighbors[:,:,0]), int(neighbors[:,:,1])], operaBlueOrangeGradient > operaBlueOrangeGradient[int(neighbors[:,:,2]), int(neighbors[:,:,3])])
#result[compare] = operaBlueOrangeGradient[compare]
                
for y in range(result.shape[0]):
    for x in range(result.shape[1]):
        if(operaBlueOrangeGradient[y,x] >= operaBlueOrangeGradient[int(neighbors[y,x,0]), int(neighbors[y,x,1])]):
            if(operaBlueOrangeGradient[y,x] >= operaBlueOrangeGradient[int(neighbors[y,x,2]), int(neighbors[y,x,3])]):
                result[y,x] = operaBlueOrangeGradient[y,x]

plt.figure(2)
plt.imshow(result)

"""
Die Ausdünnung hatte nur mittelmäßig viel Erfolg. Einige Kanten sind zwar nur ein Pixel breit,
allerdings sind ebenfalls Lücken entstanden, oder die Kanten sind zwei Pixel breit.
"""

#4.
threshold = 22
resultLine = result > threshold

plt.figure(3)
plt.imshow(resultLine)

"""
Es existiert kein Schwellwert, mit welchem es möglich ist eine durchgehende
Kanten zwischen Himmel und Dach zu ziehen, da die Gradientenstärke bei einen Teil
des Daches geringer ist, als bei Kanten innerhalb der Oper.
Eventuell könnte man das Ursprungsbild weichzeichnen, bevor man die Gradienten berechnet,
um die Kanten innerhalb des Gebäudes abzuschwächen.
"""
# -*- coding: utf-8 -*-
"""
Aufgabenblatt 8, Aufgabe 4
"""

import numpy as np
from skimage.io import imread
import skimage.filters, skimage.color
import matplotlib.pyplot as plt

#1.
opera = imread("./opera.png")
operaGray = skimage.color.rgb2gray(opera)
operaGrayGradient = skimage.filters.sobel(operaGray)

#plt.figure(1)
#plt.imshow(opera, cmap="Greys_r")
plt.figure(2)
plt.imshow(operaGrayGradient)

"""
Alle Kanten, auch die Kante zwischen Himmel und Dach, sind erkennbar.
Besonders bei Lichtreflektionen entstehen starke Kantn, auch wenn bei diesen
sich öfters gar keine Kante am Gebäude befindet.
"""

#2.
"""
Erklärung des Farbraumes:
Es ist eine Achse von Orange bis Blau.
Die Konvertierung geschieht so, dass aus den RGB-Bild der Blau-Kanal genommen
und dann die Hälfte des Rot- und Grün-Kanals abgezogen wird. So wäre ein blauer
Wert ganz hoch, ein orangener (Rot und Grün) Wert am niedriegsten.
Graustufen würden dann auf 0 gesetzt werden, da x -x/2 - x/2 = 0 ist.
"""

operaBlueOrange = opera[:,:,2] - opera[:,:,1]/2 - opera[:,:,0]/2
operaBlueOrange = operaBlueOrange - np.min(operaBlueOrange)                     #Geringster Wert = 0
operaBlueOrange = (operaBlueOrange / np.max(operaBlueOrange)) * 255             #Normalisierung auf 0-255

#3. 
operaBlueOrangeGradient = skimage.filters.sobel(operaBlueOrange)

#plt.figure(3)
#plt.imshow(operaBlueOrange, cmap="Greys_r")
plt.figure(4)
plt.imshow(operaBlueOrangeGradient)

"""
Die Kanten zwischen Himmel und Dach sind nun nicht nur viel stärker erkennbar,
sondern auch die einzig starken Kanten im gesamten Bild.
"""
# -*- coding: utf-8 -*-
"""
Aufgabenblatt 4, Aufgabe 4
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import math

image = imread("./tv.png").astype(np.float)

def nearestNeighbor(img, y, x):
    y = int(round(y))
    x = int(round(x))
    if(y > img.shape[0] - 1):
        y = img.shape[0] - 1
    if(x > img.shape[1] - 1):
        x = img.shape[1] - 1
    return img[y, x]

def scale(img, scale):
    matrix = np.array(((scale,0,0),(0,scale,0),(0,0,1)))
    result = np.zeros((round(img.shape[0] * scale), round(img.shape[1] * scale)))
    for coord in (itertools.product(range(result.shape[0]), range(result.shape[1]))):
        y, x, z = np.array([coord[0], coord[1], 1]).dot(np.linalg.inv(matrix))
        result[coord[0], coord[1]] = nearestNeighbor(img, y, x)
    result = result.astype(np.uint8)
    plt.imshow(result, cmap="Greys_r")
    plt.imsave("tv2.png", result, cmap="Greys_r")
    return result

"""
4.3:
    Es werden durch das Skalieren mit einem Faktor s > 1 keine Informationen gewonnen, da
    es nur eine vorgegebene Menge an Pixeln im Bild gibt. Alle anderen Pixel wurden durch
    Interpolation generiert, welche keine neuen Informationen hinzufügen, sondern nur auf bestehenden
    zurückgreifen.

4.4:
    Das Ergebnis ist nicht identisch zum Urpsrungsbild, da man durch die erste Skalierung
    Informationen verliert und bei der zweiten Skalierung sich nun auf ein Bild beruft, welches
    weniger Informationen besitzt.
"""
# -*- coding: utf-8 -*-
"""
Aufgabenblatt 2, Aufgabe 1
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

# Frequenzbereiche der Bänder sind auf Seite 35 im Buch Digital Image Processing vermerkt
red = imread("./band3.png")         # Rotes Licht
nir = imread("./band4.png")         # Nahes Infrarot

# Konvertierung des Datentypes um negative Werte zu ermöglichen
red = red.astype(np.float)
nir = nir.astype(np.float)

# Berechnung des normalized difference vegetation index (NDVI)
ndvi = (nir - red)/(nir + red)
plt.imshow(ndvi, cmap="Greys_r")

'''
Die hellen Flächen des NDVI zeigen die Bereiche mit höherer Vegetationsdichte.
Pflanzen reflektieren Rot relativ wenig, dafür Infrarot relativ viel, weshalb man den Unterschied (nir - red) beider
Kanäle nutzen kann, um die Dichte an Vegetation zu bestimmen. Durch die Division mit der Summe beider Kanäle (nir + red)
werden die Werte anschließend normalisiert.
'''
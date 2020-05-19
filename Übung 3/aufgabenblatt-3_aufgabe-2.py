# -*- coding: utf-8 -*-
"""
Aufgabenblatt 3, Aufgabe 2
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

#1.
image1 = imread("./bild1.png").astype(np.float)
image2 = imread("./bild2.png").astype(np.float)
image3 = imread("./bild3.png").astype(np.float)
image4 = imread("./bild4.png").astype(np.float)
image5 = imread("./bild5.png").astype(np.float)

background1 = (image1 + image2 + image3 + image4 + image5)/5
plt.imshow(background1, cmap="Greys_r")

"""
5 Bilder reichen nicht aus, da man immer noch "Geister-Bälle" erkennt.
"""

#2.
"""
Da der Ball heller ist als der Hintergrund, kann man von den 5 Pixeln immer den dunkelsten nehmen,
um ein "Hintergrund"-Pixel zu erhalten. Da der dunkelste Pixel aber noch den Schatten beinhaltet,
wird stattdessen der mittlerste, also der dritthellste/dunkelste, der 5 Pixel genommen.
Würde man den hellsten Pixel nehmen, hätte man basically bereits das fertige Bild :D
"""
# Ich hab' keine Ahnung, wie man das ohne Schleife macht... geht bestimmt, finde nur nichts...
background2 = np.zeros_like(image1)
for y in range(background2.shape[0]):
    for x in range(background2.shape[1]):
        background2[y,x] = np.sort((image1[y,x], image2[y,x], image3[y,x], image4[y,x], image5[y,x]))[2]

# plt.imshow(background2, cmap="Greys_r")

#3.
threshold = 17  # Testweise guter Wert

image1Ball = abs(image1 - background2) > threshold
image2Ball = abs(image2 - background2) > threshold
image3Ball = abs(image3 - background2) > threshold
image4Ball = abs(image4 - background2) > threshold
image5Ball = abs(image5 - background2) > threshold
plt.imshow(image5Ball, cmap="Greys_r")

#4.
background3 = np.copy(background2)
background3 = np.where(image1Ball, image1 * image1Ball, background3)
background3 = np.where(image2Ball, image2 * image2Ball, background3)
background3 = np.where(image3Ball, image3 * image3Ball, background3)
background3 = np.where(image4Ball, image4 * image4Ball, background3)
background3 = np.where(image5Ball, image5 * image5Ball, background3).astype(np.uint8)
plt.imshow(background3, cmap="Greys_r")

#5.
plt.imsave("./bild6.png", background3, cmap="Greys_r")
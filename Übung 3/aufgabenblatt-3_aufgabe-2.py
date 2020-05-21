# -*- coding: utf-8 -*-
"""
Aufgabenblatt 3, Aufgabe 2
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
# from skimage.color import rgb2gray

#1.
prefix = "serienbild2/bild"
appendix = ".png"
image1 = imread(prefix+"1"+appendix).astype(np.float)
image2 = imread(prefix+"2"+appendix).astype(np.float)
image3 = imread(prefix+"3"+appendix).astype(np.float)
image4 = imread(prefix+"4"+appendix).astype(np.float)
image5 = imread(prefix+"5"+appendix).astype(np.float)

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
# threshold = 17  # Testweise guter Wert für gegebene Bilder
threshold = 60  # Testweise guter Wert für eigene Bilder

image1obj = abs(image1 - background2) > threshold
image2obj = abs(image2 - background2) > threshold
image3obj = abs(image3 - background2) > threshold
image4obj = abs(image4 - background2) > threshold
image5obj = abs(image5 - background2) > threshold

#4.
serienbild = np.copy(background2)
serienbild = np.where(image1obj, image1 * image1obj, serienbild)
serienbild = np.where(image2obj, image2 * image2obj, serienbild)
serienbild = np.where(image3obj, image3 * image3obj, serienbild)
serienbild = np.where(image4obj, image4 * image4obj, serienbild)
serienbild = np.where(image5obj, image5 * image5obj, serienbild).astype(np.uint8)
plt.imshow(serienbild, cmap="Greys_r")

#5.
plt.imsave("./serienbild.png", serienbild, cmap="Greys_r")
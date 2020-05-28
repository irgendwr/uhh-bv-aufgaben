# -*- coding: utf-8 -*-
"""
Aufgabenblatt 4, Aufgabe 1
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray

bild1 = imread("./bild1.png").astype(np.float)
bild2 = imread("./bild2.png").astype(np.float)
bild3 = rgb2gray(imread("./bild3.png").astype(np.float))

#1
c = 255/(np.log(1 + np.max(bild1)))
bild1Improved = c * np.log(bild1 + 1)
bild1Improved = bild1Improved.astype(np.uint8)
plt.imshow(bild1Improved, cmap="Greys_r", vmin=0, vmax=255)
#plt.imsave("bild1Improved.png", bild1Improved, cmap="Greys_r", vmin=0, vmax=255)

"""
Auf bild1 wird eine Logarithmus-Transformation angewendet, um die dunkleren Bereiche
stärker von einander abzugrenzen, bzw. aufzuhellen.
An der kleinen grünen Insel befinden sich 8 Poller.
"""


#2.
bild2Improved = (bild2 - np.min(bild2)) / (np.max(bild2) - np.min(bild2)) * 255
bild2Improved = bild2Improved.astype(np.uint8)
plt.imshow(bild2Improved, cmap="Greys_r", vmin=0, vmax=255)
#plt.imsave("bild2Improved.png", bild2Improved, cmap="Greys_r", vmin=0, vmax=255)

"""
Auf bild2 wird Contrast-Stretching angewendet, um den dunkelsten Bereich auf 0
und den hellsten auf 255 zu setzen um so den Kontrast zwischen Gebäuden und Himmel zu erhöhen.
"""


#3.
def levelSlicing(pixel, l, h):
    if pixel > l and pixel < h:
        return 255
    return pixel

thres1 = 100
thres2 = 255
bild3Improved = np.vectorize(levelSlicing)(bild3, thres1, thres2)
bild3Improved = bild3Improved.astype(np.uint8)
plt.imshow(bild3Improved, cmap="Greys_r", vmin=0, vmax=255)
plt.imsave("bild3Improved.png", bild3Improved, cmap="Greys_r", vmin=0, vmax=255)

"""
Auf bild3 wurde ein Intensity-level slicing, welches alle Pixel in einen bestimmten
Wertebereich auf 255 setzt.
"""
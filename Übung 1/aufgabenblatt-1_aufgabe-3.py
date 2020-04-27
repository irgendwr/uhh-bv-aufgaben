# -*- coding: utf-8 -*-
"""
Aufgabenblatt 1, Aufgabe 3
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave

#1.
mandrill = imread("./mandrill.png")

#2.
plt.imshow(mandrill, cmap="Greys_r")

#3.
mandrillNose = mandrill[325:450, 150:350]

#4.
plt.imsave("./mandrillNose.png", mandrillNose, cmap="Greys_r")

#5.
mandrill2 = mandrill
mandrill2[0, 0] = 0
plt.imshow(mandrill2, cmap="Greys_r")       #Kein Unterschied erkennbar

#6.
mandrill3 = mandrill
mandrill3[25:75, 150:375] = 0
plt.imshow(mandrill3, cmap="Greys_r")       #Unterschied erkennbar
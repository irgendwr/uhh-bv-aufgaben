# -*- coding: utf-8 -*-
"""
Aufgabenblatt 1, Aufgabe 4
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

#1.
mandrill = imread("./mandrill.png")
mandrill2 = np.fliplr(mandrill)
mandrill3 = np.flipud(mandrill)
mandrill4 = np.flipud(np.fliplr(mandrill))

mandrill5 = np.zeros((mandrill.shape[0] * 2, mandrill.shape[1] * 2))
mandrill5[0:mandrill.shape[0], 0:mandrill.shape[1]] = mandrill      #Oben-links
mandrill5[0:mandrill.shape[0], mandrill.shape[1]:] = mandrill2      #Oben-rechts
mandrill5[mandrill.shape[0]:, 0:mandrill.shape[1]] = mandrill3      #Unten-links
mandrill5[mandrill.shape[0]:, mandrill.shape[1]:] = mandrill4       #Unten-rechts
plt.imshow(mandrill5, cmap="Greys_r")

#2.
mandrillInverted = np.invert(mandrill)
plt.imshow(mandrillInverted, cmap="Greys_r")

#3.
mandrillNose = mandrill[325:450, 150:350]
mandrillNose[0, 0] = 0      #Pixel wurde ebenfalls im Originalbild schwarz

#4.
mandrillMask = np.zeros(mandrill.shape)
mandrillMask[325:450, 150:350] = 1
mandrillMasked = mandrill * mandrillMask
plt.imshow(mandrillMasked, cmap="Greys_r")
# -*- coding: utf-8 -*-
"""
Aufgabenblatt 8, Aufgabe 2
"""

import numpy as np
from skimage.io import imread
import skimage.filters
import matplotlib.pyplot as plt

#1.
mandrill = imread("./mandrill.png")
mandrillGradient = skimage.filters.sobel(mandrill)

threshold1 = 0.12
mandrillGradientSliced = np.zeros_like(mandrillGradient)
mandrillGradientSliced[mandrillGradient > threshold1] = 1

plt.figure(1)
plt.imshow(mandrill, cmap="Greys_r")
plt.figure(2)
plt.imshow(mandrillGradient)
plt.figure(3)
plt.imshow(mandrillGradientSliced)

"""
Während die wichtigsten Kanten wie Augen, Nase und Nasenpartien erkennbar sind,
wird auch ein Großteil des Felles als Kanten erkannt.
Das beste Ergebbnis entsteht bei einen Grenzwert um 0.12
"""

#2.
sigma = 2.5
mandrillGauss = skimage.filters.gaussian(mandrill, sigma, preserve_range=True)
mandrillGaussGradient = skimage.filters.sobel(mandrillGauss)

threshold2 = 0.0375*255                                                         # Normalisierung 0-255
mandrillGaussGradientSliced = np.zeros_like(mandrillGaussGradient)
mandrillGaussGradientSliced[mandrillGaussGradient > threshold2] = 1

plt.figure(4)
plt.imshow(mandrillGaussGradient)
plt.figure(5)
plt.imshow(mandrillGaussGradientSliced)

"""
Durch das Weichzeihnen verschwinden die Kanten im Fell überwiegend und nur noch
die Kanten an Augen, Nase/Nasenpartien und Bart sind gut erkennbar, wobei der
Bart hingegen überwiegend nicht erkennbar ist.

Mit einem größer werdenen Sigma, muss der Grenzwert nach unten angepasst werden, da
durch das Weichzeihnen sich die Gradientenstärken verringern, weil die Unterschiede
zwischen den Pixel nun verringert sind.
"""

#3.
row1 = mandrill[:,150]
row1Sobel = skimage.filters.sobel_v(mandrill)[:,150]*255                        # Normalisierung auf 0-255

row2 = mandrillGauss[:,150]
row2Sobel = skimage.filters.sobel_v(mandrillGauss)[:,150]

mandrillMoreGauss= skimage.filters.gaussian(mandrill, 20, preserve_range=True)
row3 = mandrillMoreGauss[:,150]
row3Sobel = skimage.filters.sobel_v(mandrillMoreGauss)[:,150]

plt.figure(6)
plt.plot(range(len(row1)), row1)
plt.plot(range(len(row1Sobel)), row1Sobel)

plt.figure(7)
plt.plot(range(len(row2)), row2)
plt.plot(range(len(row2Sobel)), row2Sobel)

plt.figure(8)
plt.plot(range(len(row3)), row3)
plt.plot(range(len(row3Sobel)), row3Sobel)

"""
Die Intensitätskurven des eigentlichen Bilder werden durch den Weichzeichner glatter.
Die Ableitungskurven werden glatter, kleiner und vorallem weniger sparodisch in ihrer Steigung.
"""

#4.
mandrillGradientOrientation = np.rad2deg(np.arctan(skimage.filters.sobel_v(mandrill)/skimage.filters.sobel_h(mandrill)))
mandrillGaussGradientOrientation = np.rad2deg(np.arctan(skimage.filters.sobel_v(mandrillGauss)/skimage.filters.sobel_h(mandrillGauss)))

mandrillGradientOrientationHist = np.histogram(mandrillGradientOrientation, bins=9, range=(-90,90), density=True)
mandrillGaussGradientOrientationHist = np.histogram(mandrillGaussGradientOrientation, bins=9, range=(-90,90), density=True)

plt.figure(9)
plt.hist(mandrillGradientOrientation.flatten(), bins=9, range=(-90,90), density=True)
plt.figure(10)
plt.hist(mandrillGaussGradientOrientation.flatten(), bins=9, range=(-90,90), density=True)

plt.figure(11)
plt.hist(mandrillGradientOrientation.flatten(), bins=9, range=(-90,90), density=True, weights=mandrillGradient.flatten())
plt.figure(12)
plt.hist(mandrillGaussGradientOrientation.flatten(), bins=9, range=(-90,90), density=True, weights=mandrillGaussGradient.flatten())

"""
Beim normalen Bild liegen die meisten Orientationen zwischen -25 und 25 Grad.
Beim weichgezeichneten Bild liegen die meisten Orientationen bei entweder -90 bis -75, 75 bis 90, oder um 0 Grad.
Dies bedeutet, dass beim weichgezeichneten Bild überwiegend keine Kanten, oder starke Kanten
existieren, aber weniger "schwache" Kanten.

Wenn "weights" auf die Gradientenstärke gesetzt wird, verstärken sich die Trends im Histogramm, also
sind beim normalen Bild deutlich mehr Orientationen im Bereich zwischen -25 und 25 Grad und
beim weichgezeichneten Bild noch mehr bei entweder -90 bis -75, 75 bis 90, oder um 0 Grad.
"""
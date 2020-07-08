# -*- coding: utf-8 -*-
"""
Aufgabenblatt 9, Aufgabe 2
"""

import numpy as np
from skimage.io import imread
import skimage.filters, skimage.util
import matplotlib.pyplot as plt

#1.
sigma = 6       # Für Aufgabe 4, sonst sigma = 3

mandrill = imread("./mandrill.png")/255
mandrillGauss = skimage.filters.gaussian(mandrill, sigma)
mandrillNoise = skimage.util.random_noise(mandrill, var=0.01)

plt.figure(1)
plt.imshow(mandrill, cmap="Greys_r")
plt.figure(2)
plt.imshow(mandrillGauss, cmap="Greys_r")
plt.figure(3)
plt.imshow(mandrillNoise, cmap="Greys_r")

#2.
mandrillLaplace = skimage.filters.laplace(mandrill)
mandrillGaussLaplace = skimage.filters.laplace(mandrillGauss)
mandrillNoiseLaplace = skimage.filters.laplace(mandrillNoise)

plt.figure(4)
plt.imshow(mandrillLaplace)
plt.figure(5)
plt.imshow(mandrillGaussLaplace)
plt.figure(6)
plt.imshow(mandrillNoiseLaplace)

"""
Der Laplace-Filter ist noch empfindlicher als der Sobel-Filter gegenüber Rauschen,
weshalb im verauschtn Bild auch nur wieder Rauschen zu sehen ist.
Im normalen Bild werden alle Haare als Kanten erkannt, weshalb auch im normalen Bild
überwiegend Rauschen zu erkennen ist, wobei aber noch die Ansätze von den Augen und Nase erkennbar sind,
da es sich dabei um relativ homogene Flächen mit sauberen Kanten handelt.
Die Kanten im weichgezeichneten Bild lassen sich erkennen, da feinere Kanten (Haar) im Originalbild
durch das Weichzeihnen entfernt wurden sind und der Laplace-Filter somit nur noch
die stärkeren Kanten im Haar, sowie bei Augen, Nase und Nasenpartieen erkennt.
"""

#3.
mandrillNoiseGauss = skimage.filters.gaussian(mandrillNoise, 3)
mandrillNoiseGaussLaplace = skimage.filters.laplace(mandrillNoiseGauss)

plt.figure(7)
plt.imshow(mandrillNoiseGaussLaplace)

"""
Mit einen gleichen Sigma wie beim eigentlich weichgezeichneten Bild, erhält
man ein änhlich gutes Ergebnis der Kanten, wobei der Noise noch leicht zu
erkennen ist.
"""

#4.
threshold = 0.0006       # Bei einer Varianz von 3: 0.005
mandrillGaussLaplaceEdges = np.zeros_like(mandrillGaussLaplace)
for y in range(mandrillGaussLaplace.shape[0]-2):                                    # Ränder werden nicht betrachtet, Positionen müssen um 1 geshiftet werden
    for x in range(mandrillGaussLaplace.shape[1]-2):
        if(mandrillGaussLaplace[y+1,x+1-1] * mandrillGaussLaplace[y+1,x+1+1] < 0):  # links und rechts
            if(abs(mandrillGaussLaplace[y+1,x+1-1] - mandrillGaussLaplace[y+1,x+1+1]) > threshold):
                mandrillGaussLaplaceEdges[y+1,x+1] = 1
        elif(mandrillGaussLaplace[y+1-1,x+1] * mandrillGaussLaplace[y+1+1,x+1] < 0):# oben und unten
            if(abs(mandrillGaussLaplace[y+1-1,x+1] - mandrillGaussLaplace[y+1+1,x+1]) > threshold):
                mandrillGaussLaplaceEdges[y+1,x+1] = 1
        elif(mandrillGaussLaplace[y+1-1,x+1-1] * mandrillGaussLaplace[y+1+1,x+1+1] < 0):# oben-links und unten-rechts
            if(abs(mandrillGaussLaplace[y+1-1,x+1-1] - mandrillGaussLaplace[y+1+1,x+1+1]) > threshold):
                mandrillGaussLaplaceEdges[y+1,x+1] = 1
        elif(mandrillGaussLaplace[y+1+1,x+1-1] * mandrillGaussLaplace[y+1-1,x+1+1] < 0):# unten-links und oben-rechts
            if(abs(mandrillGaussLaplace[y+1+1,x+1-1] - mandrillGaussLaplace[y+1-1,x+1+1]) > threshold):
                mandrillGaussLaplaceEdges[y+1,x+1] = 1
        
plt.figure(8)
plt.imshow(mandrillGaussLaplaceEdges)

"""
Es gelingt die wichtigsten Kanten zu erkennen, wobei das Ergebnis noch nicht optimal ist.
Eine Varianz von 6 mit einen Threshod von 0.0006 bietet gute Ergebnisse.
"""

mandrillSobel = skimage.filters.sobel(mandrillGauss) > 0.016    # Sobel auf weichgezeichnete Version
#mandrillSobel = skimage.filters.sobel(mandrill) > 0.15          # Sobel auf normale Version

plt.figure(9)
plt.imshow(mandrillSobel)

"""
Bei der Anwendung des Sobel-Filters auf das weichgezeichnete Bild, sind die Kanten
dicker und ungenauer, beim normalem Bild werden mehr Haare als Kanten erkannt,
im Vergleich zum Laplace-Filter.
Außerdem zeigt der Laplace-Filter auch kleinere Kanten an, wie z.B. die Rillen
in den Nasenpartien.
"""
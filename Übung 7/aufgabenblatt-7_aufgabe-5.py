# -*- coding: utf-8 -*-
"""
Aufgabenblatt 7, Aufgabe 5
"""

import numpy as np
from skimage.io import imread
import skimage.filters, skimage.segmentation
import matplotlib.pyplot as plt

#1.
einstein = imread("./einstein.png")
einsteinGauss = skimage.filters.gaussian(einstein, sigma=8)

plt.figure(1)
plt.imshow(einstein, cmap="Greys_r")
plt.figure(2)
plt.imshow(einsteinGauss, cmap="Greys_r")

"""
Bis zu einen Sigma von 8 bis 10 kann man Einstein noch erkennen.
Erkennbar sind noch Augen und Augenbrauen, Nase und Bart.
Verloren gingen sämtliche Falten, Mund, Ohren und einzelne Details der Haare.
"""

#2.
ballon = imread("./ballon.png")
ballonGauss = skimage.filters.gaussian(ballon, sigma=20, multichannel=True)

plt.figure(3)
plt.imshow(ballon)
plt.figure(4)
plt.imshow(ballonGauss)

"""
Beim ungefilterten Bild erkennt man die Kanten zwischen den farbigen Flächen,
sowie einen bunten, aber sehr dunklen Boden und eine Person, welche vor dem Ballon steht.
Nach angewendeten Filter ist die Person nicht mehr zu erkennen und der Boden nur noch
eine dunkle homogene Fläche. Der Ballon selbst sieht nun wie eine durchgehende
Farbspirale ohne harte Kanten und einzelnen Flächen aus.
"""

#3.
gletscher = imread("./gletscher.png")
gletscherSliced = np.zeros_like(gletscher)
gletscherSliced[gletscher > 120] = 128
gletscherSliced[gletscher > 190] = 255

plt.figure(5)
plt.imshow(gletscher, cmap="Greys_r")
plt.figure(6)
plt.imshow(gletscherSliced, cmap="Greys_r")

"""
Das Problem mit dem intensity-level slicing ist, dass die einzelnen Bereiche
keine relativ homogenen Flächen sind, sondern einzelne Ausreißer besitzen und
somit die Ausreißer eines Bereiches in die Farbe eines anderen Bereiches eingefärbt
werden, wodurch eine Art Rauschen entsteht.
Dies lässt sich gut bei den Steinen im See und den helleren Steinen der Moräne erkennen.
"""

#4.
gletscherGauss = skimage.filters.gaussian(gletscher, sigma=10)
gletscherGaussSliced = np.zeros_like(gletscherGauss)
gletscherGaussSliced[gletscherGauss > 110/255] = 0.5
gletscherGaussSliced[gletscherGauss > 190/255] = 1

plt.figure(7)
plt.imshow(gletscherGauss, cmap="Greys_r")
plt.figure(8)
plt.imshow(gletscherGaussSliced, cmap="Greys_r")

"""
Durch das Weichzeichnen, werden die einzelnen Ausreißer der Bereiche nun der Umgebung
angepasst und landen durch das intensity-level slicing im richtigen Bereich.

Allerdings kommt es immer noch vor, dass einzelne größere Bereiche die gleiche
Helligkeit besitzen, wie ein anderer Bereich. Dies entstand durch das Weichzeihnen
an der Grenze zwischen den Berg und den Himmel am oberen Bildrand, wodurch der
Bereich, wo hohe (Himmel) und niedrige (Berg) Intensitäten vorkamen, zu mittelhohe,
also graue Pixel weichgezeichnet worden, weshalb der obere Rand des Berges, bzw.
der untere Rand des Himmels grau (See) gezeichnet sind.
"""

#5.
gletscherCompare = skimage.segmentation.mark_boundaries(gletscher, (gletscherGaussSliced*255).astype(np.int)) 

plt.figure(9)
plt.imshow(gletscherCompare)
plt.imsave("gletscherCompare.png", gletscherCompare)

"""
Die Grenzen stimmen überwiegend überein und wenn nicht, sind sie leicht verschoben.
Die Verschiebung kommt daher, dass durch das Weichzeihnen es keine klaren Grenzen
mehr gibt, sondern Übergänge, weshalb je nach Threshold die Grenze nicht perfekt
an der Ursprünglichen Kante gesetzt wird, sondern daneben.
"""
# -*- coding: utf-8 -*-
"""
Aufgabenblatt 6, Aufgabe 5
"""

import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
#import aufgabenblatt-6_aufgabe-4

moon = imread("./moon.png")

def histEqual(img):
    imgHist = np.histogram(img, bins=256, range=(0,256), density=True)
    imgCum = np.cumsum(imgHist[0])
    
    transRights = []
    for cum in imgCum:
        new = (len(imgCum) - 1) * cum
        transRights.append(int(new))
    
    imgEqual = np.copy(img)
    for y in range(imgEqual.shape[0]):
        for x in range(imgEqual.shape[1]):
            imgEqual[y, x] = transRights[img[y, x]]
    
    return imgEqual, transRights

#1.
plt.figure(1)
plt.imshow(moon, cmap="Greys_r", vmin=0, vmax=255)

plt.figure(2)
moonEqual, _ = histEqual(moon)
plt.imshow(moonEqual, cmap="Greys_r", vmin=0, vmax=255)
plt.show()

#2. und 3.
tileSize = 2 # Größe der Kacheln
moonTileEqual = np.copy(moon)

for y in range(int(moonTileEqual.shape[0]/tileSize)):
    for x in range(int(moonTileEqual.shape[1]/tileSize)):
        tileUp = y * tileSize
        tileDown = y * tileSize + tileSize
        tileLeft = x * tileSize
        tileRight = x * tileSize + tileSize
        moonTileEqual[tileUp:tileDown, tileLeft:tileRight], _ = histEqual(moonTileEqual[tileUp:tileDown, tileLeft:tileRight])

plt.figure(3)
plt.imshow(moonTileEqual, cmap="Greys_r", vmin=0, vmax=255)

"""
Zu Teilaufgabe 2:.
Der Kontrast im Bereich einer einzelnen Kachel wird verstärkt, wobei jede
einzelne Kachel dies unterschiedlich tut, weshalb die Flächen unterschiedlich hell wirken.
Während der Inhalt einer einzelnen Kachel nun besser erkennbar ist, wirkt das
gesamte Bild nur noch schwer erkennbar.

Zu Teilaufgabe 3:
Bei immer kleiner werdenen Kachelgröße verstärkt sich der Effekt aus Teilaufgabe 2,
so ist ab einer Kachelgröße von 16x16 der Mond kaum noch mehr zu erkennen.

Ebenfalls entsteht ab einer Kachelgröße von 8x8 das Problem, dass gar nicht mehr
jeder Wert abgebildet werden kann, wodurch nicht nur kleinere Helligkeitsunterschiede
in einer Kachel verloren gehen, sondern auch global nur eine gewisse Anzahl an Intensitäten
benutzt werden kann, welches die Qualität des Bildes stark verringert.

Zusätzlich kann es bei kleinen Kachelgrößen dazu kommen, dass diese überwiegend aus
weißen Pixel bestehen, da durch den Histogrammausgleich der größte
Wert immer zu Weiß wird, wodurch Informationen verloren gehen, da die
Mondoberfläche überwiegend grau ist mit wenigen weißen Stellen.
"""
# -*- coding: utf-8 -*-
"""
Aufgabenblatt 3, Aufgabe 3
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

#1. und 2.
ohneFehler = imread("./ohneFehler.png").astype(np.float)
mitFehler = imread("./mitFehler.png").astype(np.float)

threshold = 1  # Jede Änderung soll erkannt werden
changes = abs(ohneFehler - mitFehler) > threshold
plt.imshow(changes, cmap="Greys_r")

#3a.
changeCoord = np.argwhere(changes == 1)

#3b.
changeAreas = 0
"""
Man startet bei einen zufälligen geänderten Pixel aus changes und geht durch alle durch,
indem man bereits besuchte Pixel markiert (auf schwarz setzt?).
Wenn man auf ein Pixel kommt, färbt man es ein. Dann prüft man, welche Nachbarn es erreichen kann
und geht diese ab... man muss sich aber irgendwie alle Nachbarn merken, also rekursiv rangehen?
Wenn man keine unmarkierten Nachbarn mehr finden kann, ist der Bereich abgesucht und man
erhöht die Anzahl an geänderten Bereichen um 1...
I don't know, ich finde nichs im Internet...
"""

#3c.
print("Anzahl veränderter Bereiche: " + str(changeAreas))
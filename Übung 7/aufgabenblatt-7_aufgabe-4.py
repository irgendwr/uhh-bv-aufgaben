# -*- coding: utf-8 -*-
"""
Aufgabenblatt 7, Aufgabe 4
"""

import numpy as np
import matplotlib.pyplot as plt

#1.
img = [1, 2, 5, 9, 8, 3, 6, 7, 9, 9]

plt.figure(1)
plt.plot(range(len(img)), img)

#2.
kernel = np.array([1, 1, 1, 1, 1])/5
imgZeroPad = [0, 0] + img + [0, 0]          # Padding: (5-1)/2 = 2

def convolve(img):
    imgConv = []
    for x in range(len(img) - 4):
        wsum = 0
        shift = 0
        for w in kernel:
            wsum += (img[x + shift]) * w
            shift += 1
        imgConv.append(wsum)
    
    return imgConv

imgZeroPadConv = convolve(imgZeroPad)       # zero-Padding
plt.plot(range(len(imgZeroPadConv)), imgZeroPadConv)

"""
Das zero-Padding sorgt dafür, dass die Werte der Randbereiche kleiner werden, da nun mindestens
ein Teil der erzeugten Nullen mit in das Ergebnis einfließt und den Wert verringert.
"""

#3.
imgNinePad = [9, 9] + img + [9, 9]          # Padding mit 9
imgNinePadConv = convolve(imgNinePad)
plt.plot(range(len(imgNinePadConv)), imgNinePadConv)

"""
Die Werte im Randbereich sind mit einen konstanten Padding von 9 nun größer, da das
Ergebnis der Faltung nicht mehr zum Teil von einen kleinen, sondern von einen
großen Wert (der größte in der Liste) abhängig ist, und sich somit die Randwerte erhöhen.
"""

#4.
imgRepPad = [1, 1] + img + [9, 9]           # replicate-Padding
imgRepPadConv = convolve(imgRepPad)
plt.plot(range(len(imgRepPadConv)), imgRepPadConv)

"""
Mit einen replicate-Padding nähern sich die Randbereiche an den Wert des Randes an, da
nun ein (Groß)-Teil der Werte für die Faltung den gleichen Wert haben wie der Rand.
In unseren Fall geht der linke Rand Richtung 1, während der rechte Rand Richtung 9 geht.
"""

#5.
imgMirPad = [2, 1] + img + [9, 9]           # mirror-Padding
imgMirPadConv = convolve(imgMirPad)
plt.plot(range(len(imgMirPadConv)), imgMirPadConv)

"""
Mit einen mirror-Padding nähern sich die Randbereiche an den Wert des gesamten Randebereiches an, da
nun ein (Groß)-Teil der Werte für die Faltung den gleichen Wert haben wie der Randbereich.
"""

#6.
imgRefPad = [5, 2] + img + [9, 7]           # reflection-Padding
imgRefPadConv = convolve(imgRefPad)
plt.plot(range(len(imgRefPadConv)), imgRefPadConv)

"""
Mit einen reflection-Padding nähern sich die Randbereiche an die Werte innerhalb der Liste an, da
nun ein (Groß)-Teil der Werte für die Faltung aus dem inneren der Liste (Vom Rand aus) kommen
und nicht direkt vom Rand, da der Randwert nicht für das Padding genutzt wird, sondern
nur die Bereiche vom Rand aus.
"""

"""
Plot-Farben:
    Blau    - Original
    Orange  - zero-Padding
    Grün    - Padding mit 9
    Rot     - replicate-Padding
    Lila    - mirror-Padding
    Braun   - reflection-Padding
"""
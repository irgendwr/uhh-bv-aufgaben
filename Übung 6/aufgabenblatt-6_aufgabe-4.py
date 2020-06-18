# -*- coding: utf-8 -*-
"""
Aufgabenblatt 6, Aufgabe 4
"""

import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

bild1 = imread("./bild1.png")
bild2 = imread("./bild2.png")

#1.
def showHist():
    bild1Hist = np.histogram(bild1, bins=256, range=(0,256), density=True)
    plt.figure(1)
    plt.imshow(bild1, cmap="Greys_r", vmin=0, vmax=255)
    plt.figure(2)
    plt.hist(bild1.flatten(), bins=256, range=(0,256), density=True)
    
    bild2Hist = np.histogram(bild2, bins=256, range=(0,256), density=True)
    plt.figure(3)
    plt.imshow(bild2, cmap="Greys_r", vmin=0, vmax=255)
    plt.figure(4)
    plt.hist(bild2.flatten(), bins=256, range=(0,256), density=True)
    
    return bild1Hist, bild2Hist

bild1Hist, bild2Hist = showHist()

#2.
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

def showEqual():
    bild1Equal, _ = histEqual(bild1)
    bild2Equal, _ = histEqual(bild2)
    
    plt.figure(1)
    plt.imshow(bild1Equal, cmap="Greys_r", vmin=0, vmax=255)
    plt.figure(2)
    plt.hist(bild1Equal.flatten(), bins=256, range=(0,256), density=True)
    plt.figure(3)
    plt.imshow(bild2Equal, cmap="Greys_r", vmin=0, vmax=255)
    plt.figure(4)
    plt.hist(bild2Equal.flatten(), bins=256, range=(0,256), density=True)

def compare():
    bild1Equal, _ = histEqual(bild1)
    plt.figure(1)
    plt.hist(bild1.flatten(), bins=256, range=(0,256), density=True)
    plt.hist(bild1Equal.flatten(), bins=256, range=(0,256), density=True)
    
    bild2Equal, _ = histEqual(bild2)
    plt.figure(2)
    plt.hist(bild2.flatten(), bins=256, range=(0,256), density=True)
    plt.hist(bild2Equal.flatten(), bins=256, range=(0,256), density=True)

"""
Bei bild1 wurden überwiegend die dunklen Bereiche im Bild auf hellere Werte gemappt,
während die helleren Bereiche fast unverändert blieben, wodurch das Bild zwar heller,
aber nicht überbelichtet wurde.

Bei bild2 wurden die Werte auf den gesammten Wertebereich gestreckt, wodurch sich
der Kontrast erhöht.
"""

#3.
def f(x):
    return (255**0.8) * (x**0.2)

def g(x):
    what = np.e**((x / 255)*16-10)
    oben = 255 * what
    unten = 1 + what
    return oben/unten

def transRights():
    _, transRights1 = histEqual(bild1)
    _, transRights2 = histEqual(bild2)
    
    plt.figure(1)
    plt.plot(range(len(transRights1)), transRights1)
    plt.plot(range(len(transRights1)), list(map(f, range(len(transRights1)))))
    plt.figure(2)
    plt.plot(range(len(transRights2)), transRights2)
    plt.plot(range(len(transRights2)), list(map(g, range(len(transRights2)))))
    plt.show()

"""
Die Musterlösung von bild1 aus Aufgabe 4.1 sieht insgesammt heller und kontrastärmer aus.
Dies lässt sich damit erklären, dass die Intensitätstransformation (besonders bei den dunklen Bereichen)
steiler ansteigt, als unsere Transformationsfunktion, und somit weniger dunklere Bereiche im
Endbild vorkommen.

Die Musterlösung von bild2 aus Aufgabe 4.1 besitzt weniger Kontrast und Noise.
Dies lässt sich damit erklären, dass bei unserer Transformationsfunktion nur der
signifikante Bereich stark gestreckt wird, während bei der Intensitätstransformation
ein größerer Bereich leichter gestreckt wird.
"""
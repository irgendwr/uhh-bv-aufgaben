# -*- coding: utf-8 -*-
"""
Aufgabenblatt 6, Aufgabe 2
"""

import numpy as np
from skimage.io import imread
import time

mandrill = imread("./mandrill.png").astype(np.float)

npMean = np.mean(mandrill)      # Vergleichswert für Mittelwert
npVariance = np.var(mandrill)   # Vergleichswert für Varianz

#1. (Zwei Durchläufe)
def variance1(img):
    mean1 = 0
    for y1 in range(img.shape[0]):
        for x1 in range(img.shape[1]):
            mean1 += img[y1, x1]
    mean1 = mean1 / (img.shape[0] * img.shape[1])
    
    variance1 = 0
    for y2 in range(img.shape[0]):
        for x2 in range(img.shape[1]):
            variance1 += (img[y2, x2] - mean1)**2
    variance1 = variance1 / (img.shape[0] * img.shape[1])
    
    return variance1

#2. (Ein Durchlauf)
def variance2(img):
    mean2 = 0
    variance2 = 0
    for y3 in range(img.shape[0]):
        for x3 in range(img.shape[1]):
            mean2 += img[y3, x3]
            variance2 += (img[y3, x3])**2                                       # Does the fucky wucky sometimes... idk why tho
    mean2 = mean2 / (img.shape[0] * img.shape[1])
    variance2 = variance2 / (img.shape[0] * img.shape[1]) - mean2**2
    
    return variance2

#3.
def compare():
    start1 = time.time()
    for i in range(10):
        variance1(mandrill)
    end1 = time.time()
    print("Zehn Wiederholungen über zwei Drchläufe: " + str(end1 - start1))
    
    start2 = time.time()
    for i in range(10):
        variance2(mandrill)
    end2 = time.time()
    print("Zehn Wiederholungen über einen Drchläufe: " + str(end2 - start2))

"""
Die abweichenden Ergebnisse lassen sich dadurch erklären, dass bei der ersten Variante
die Subtraktion vor der Quadrierung durchgeführt wird, wodurch sehr kleine Werte entstehen können,
welche zu Ungenauigkeiten bei der Quadrierung führen.
Dies passiert bei der zweiten Variante nicht, da zuerst Quadriert und dann Subtrahiert wird.

Zehn Wiederholung für die Variante mit zwei Durchläufen brauchen 2.39 Sekunden,
zehn Wiederholung für die Variante mit einen Durchlauf hingegen nur 2.12 Sekunden.
Der Grund liegt darin, dass bei der zweiten Variante sich eine Doppelschleife gesparrt wird.
"""
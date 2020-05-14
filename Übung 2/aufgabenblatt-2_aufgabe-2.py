# -*- coding: utf-8 -*-
"""
Aufgabenblatt 2, Aufgabe 2
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#import scipy.stats

mu = 0      #µ
sigma = 1   #σ

# Gauss-Funktion, Laufzeitoptimierung wurde zu gunsten der Lesbarkeit ignoriert
def gauss(x):
    x = x/(50/10) - 5   # Umkonvertierung der Spalten 0 bis 50 in den Definitionsbereich von -5 bis 5
    fx = (1/math.sqrt(2 * math.pi * (sigma**2))) * math.exp(-(((x - mu)**2)/2 * (sigma**2)))    #Gauss-Funktion
    fx = fx * (math.sqrt(2 * math.pi * (sigma**2))) * 255   #Skalierung auf 0 bis 255
    fx = round(fx)     # Kaufmännisches Runden
    return fx

# Erzeugt eine Zeile, welche an 51 Punkten die Gauss-Funktion abtastet
line = np.zeros((51))
for x in range(51):
    line[x] = gauss(x)

# Erzeugt ein Bild mit 100 Zeilen aus einer Zeile
image = np.array(line)
for i in range(99):     # Nur 99 Wiederholung, da die erste Zeile bereits vorhanden ist
    image = np.vstack((image, line))

plt.imshow(image, cmap="Greys_r")

'''
mu (µ) verschiebt die Gauss-Verteilung auf der x-Achse,
wobei negative Werte nach links und positve nach rechts verschieben.
    
sigma (σ) streckt, bzw. staucht die Gauss-Verteilung über die x-Achse,
wobei Werte zwischen 0 und 1 (aber nicht gleich 0) strecken und Werte über 1 stauchen (Negative Werte verhalten sich wie positive).
'''
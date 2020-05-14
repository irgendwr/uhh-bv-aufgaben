# -*- coding: utf-8 -*-
"""
Aufgabenblatt 2, Aufgabe 5
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

mandrill = imread("./mandrill.png")
plt.imshow(mandrill, cmap="Greys_r")    # Zeigt mandrill als Referenz an

# Fügt Gaußsches Rauschen zu mandrill hinzu
def gaussNoise(sigma):
    image = mandrill.copy()     # Erzeugt Kopie, um nicht das Originalbild z bearbeiten
    image = image.astype(np.float)  # Vermeidet Wrap der Werte bei Überlauf
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            noise = np.random.normal(0, sigma) # Erzeugt Noise nach Normalverteilung
            image[y][x] += noise
    image = np.clip(image, 0, 255)      # Clippt das Bild in den Wertebereich von 0 bis 255
    plt.imshow(image, cmap="Greys_r")

# Fügt Salt and Pepper Rauschen zu mandrill hinzu, Wahrscheinlichkeit nicht in Prozent: 50% --> 0.5
def saltPepper(probability):
    image = mandrill.copy()
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if (probability > np.random.rand()):    # Prüft, ob Noise angewendet werden soll
                if (0.5 > np.random.rand()):
                    image[y][x] = 0
                else:
                    image[y][x] = 255
    plt.imshow(image, cmap="Greys_r")

"""
Die Standardabweichung beim Gaußschen Rauschen ändert die Menge des Noises. Eine geringere Standardabweichung
sorgt für relativ wenig Rauschen, eine hohe Standardabweichung sorgt für relativ viel Rauschen.

Die Wahrscheinlichkeit beim Salt and Pepper Noise ändert die Menge des Noises. Eine geringere Wahrscheinlichkeit
sorgt für relativ wenig Rauschen, eine hohe Wahrscheinlichkeit sorgt für relativ viel Rauschen.
"""
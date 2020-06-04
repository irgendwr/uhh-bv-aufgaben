# -*- coding: utf-8 -*-
"""
Aufgabenblatt 5, Aufgabe 5
"""

import numpy as np
#import matplotlib.pyplot as plt
from skimage.io import imread
import skimage.color

flower1 = imread("./image_02881.jpg")
flower1mask = imread("./image_02881_maske.png")
flower2 = imread("./image_02890.jpg")
flower2mask = imread("./image_02890_maske.png")
flower3 = imread("./image_04650.jpg")
flower3mask = imread("./image_04650_maske.png")
flower4 = imread("./image_04666.jpg")
flower4mask = imread("./image_04666_maske.png")

#1.
flower1Gray = skimage.color.rgb2gray(flower1)
flower2Gray = skimage.color.rgb2gray(flower2)
flower3Gray = skimage.color.rgb2gray(flower3)
flower4Gray = skimage.color.rgb2gray(flower4)

flower1Masked = np.ma.array(flower1Gray, mask = 1 - flower1mask)
flower1Mean = np.ma.mean(flower1Masked)
flower2Masked = np.ma.array(flower2Gray, mask = 1 - flower2mask)
flower2Mean = np.ma.mean(flower2Masked)
flower3Masked = np.ma.array(flower3Gray, mask = 1 - flower3mask)
flower3Mean = np.ma.mean(flower3Masked)
flower4Masked = np.ma.array(flower4Gray, mask = 1 - flower4mask)
flower4Mean = np.ma.mean(flower4Masked)

#2.
flower1Hue = skimage.color.rgb2hsv(flower1)[:,:,0]
flower2Hue = skimage.color.rgb2hsv(flower2)[:,:,0]
flower3Hue = skimage.color.rgb2hsv(flower3)[:,:,0]
flower4Hue = skimage.color.rgb2hsv(flower4)[:,:,0]

flower1HueMasked = np.ma.array(flower1Hue, mask = 1 - flower1mask)
flower1HueMean = np.ma.mean(flower1HueMasked)
flower2HueMasked = np.ma.array(flower2Hue, mask = 1 - flower2mask)
flower2HueMean = np.ma.mean(flower2HueMasked)
flower3HueMasked = np.ma.array(flower3Hue, mask = 1 - flower3mask)
flower3HueMean = np.ma.mean(flower3HueMasked)
flower4HueMasked = np.ma.array(flower4Hue, mask = 1 - flower4mask)
flower4HueMean = np.ma.mean(flower4HueMasked)

#3.
"""
Die Mittelwerte von Grau- und Farbwert liegen für Blume 1 und Blume 2, als auch
Blume 3 und Blume 4 jeweils relativ nah, zwischen den jeweiligen Blumenarten aber
weit auseinander, weshalb man in diesen Fall beide Blumenarten außeinander halten kann.

Allgemein ist aber der Grauwert kein gutes Kriterium, da dieser nur auf die Helligkeit
achtet, weshalb zwei unterschiedlich farbige Blumen, aber mit gleicher Helligkeit
den selben Grauwert erhalten und somit nicht voneinander trennbar sind.
Dazu können die selben Blumen zwei unterschiedliche Grauwerte, je nach Beleuchtung
haben.

Der Farbwert eignet sich deshalb besser, da selbst unterschiedlich belichtete Blumen
den gleichen Farbwert haben und nur Blumen der gleichen Farbe den selben Farbwert haben können.
"""
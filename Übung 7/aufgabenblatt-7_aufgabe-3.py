# -*- coding: utf-8 -*-
"""
Aufgabenblatt 7, Aufgabe 3
"""

import numpy as np
from skimage.io import imread
import skimage.filters, skimage.util
import matplotlib.pyplot as plt
import scipy.ndimage

#1.
einstein = imread("./einstein.png")/255
einsteinNoise = skimage.util.random_noise(einstein, mode='gaussian', var=0.01)

plt.figure(1)
plt.imshow(einstein, cmap="Greys_r")

plt.figure(2)
plt.imshow(einsteinNoise, cmap="Greys_r")

#2.
def absDiff(img0, img1):
    diff = np.abs(img0 - img1)
    diffMean = np.mean(diff)
    
    return diffMean

diff = absDiff(einstein, einsteinNoise)

"""
Die mittlere Differenz zwischen Original und dem verauschten Bild
beträgt ungefähr 0.0725
"""

#3.
def boxFilter(img, kernelSize):
    kernel = np.full((kernelSize, kernelSize), 1/kernelSize)
    imgConv = scipy.ndimage.convolve(img, kernel)
    
    return imgConv

# Testen, weche Größe die geringste Differenz erzeugt.
test1 = []
for size in range(3, 13, 2):
    test1.append(absDiff(einstein, boxFilter(einsteinNoise, size)))
print("Geringste Differenz bei einer Größe von: " + str((np.argmin(test1)*2)+3))

diffBox = np.min(test1)

plt.figure(3)
plt.imshow(boxFilter(einsteinNoise, (np.argmin(test1)*2)+3), cmap="Greys_r")

"""
Die geringste mittlere Differenz wird durch einen 3x3 Filterkern erzeugt.
Dabei ist die mittlere Differenz aber immer noch höher, als bei einen ungefalteten Bild.
"""

#4.
def gaussFilter(img, var):
    imgGauss = scipy.ndimage.gaussian_filter(img, var)
    
    return imgGauss

# Testen, weche Varianz die geringste Differenz erzeugt.
test2 = []
for var in range(1, 21):
    test2.append(absDiff(einstein, gaussFilter(einsteinNoise, var/10)))
print("Geringste Differenz bei einer Varianz von: " + str((np.argmin(test2) + 1)/10))

diffGauss = np.min(test2)

plt.figure(4)
plt.imshow(gaussFilter(einsteinNoise, (np.argmin(test2) + 1)/10), cmap="Greys_r")

"""
Die geringste mittlere Differenz wird durch eine Varianz von 1 erzeugt.
Die mittlere Differenz von Gauss-Filter ist geringer, als die des Box-Filters.
Es lässt sich kein wirklicher Unterschied zwischen dem Box-Filter und dem Gauss-Filter erkennen.
"""

#5.
einsteinNoiseSP = skimage.util.random_noise(einstein, mode='s&p', amount=0.1)

plt.figure(5)
plt.imshow(einsteinNoiseSP, cmap="Greys_r")

#Testen, weche Varianz die geringste Differenz erzeugt.
test3 = []
for var in range(1, 21):
    test3.append(absDiff(einstein, gaussFilter(einsteinNoiseSP, var/10)))
print("Geringste Differenz bei einer Varianz von: " + str((np.argmin(test3) + 1)/10))

diffGaussSP = np.min(test3)

plt.figure(6)
plt.imshow(gaussFilter(einsteinNoiseSP, (np.argmin(test3) + 1)/10), cmap="Greys_r")

"""
Die geringste mittlere Differenz wird durch eine Varianz von 1 erzeugt.
Die mittlere Differenz zwischen Original und dem verauschten Bild
beträgt ungefähr 0.047
"""

#6.
def medianFilter(img):
    img = np.copy(einsteinNoiseSP)
    imgPadded = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
    imgPadded[1:imgPadded.shape[0]-1, 1:imgPadded.shape[1]-1] = img
    
    new = np.zeros_like(img)
    for y in range(new.shape[0]):
        for x in range(new.shape[1]):
            median = []
            median.append(imgPadded[y, x])
            median.append(imgPadded[y, x+1])
            median.append(imgPadded[y, x+2])
            median.append(imgPadded[y+1, x])
            median.append(imgPadded[y+1, x+1])
            median.append(imgPadded[y+1, x+2])
            median.append(imgPadded[y+2, x])
            median.append(imgPadded[y+2, x+1])
            median.append(imgPadded[y+2, x+2])
            new[y, x] = np.median(median)
    
    return new

diffMedianSP = absDiff(einstein, medianFilter(einsteinNoiseSP))

plt.figure(7)
plt.imshow(medianFilter(einsteinNoiseSP), cmap="Greys_r")

"""
Die mittlere Differenz über den Median-Filter ist deutlich geringer, als über
den Gauss-Filter. Visuell kann man beim Gauss-Filter noch den Salt&Pepper erkennen,
während beim Median-Filter das gefilterte Bild fast gleich den Ursprungsbild aussieht.
"""
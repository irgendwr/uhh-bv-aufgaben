# -*- coding: utf-8 -*-
"""
Aufgabenblatt 5, Aufgabe 3
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import math

mandrill = imread("./mandrillFarbe.png").astype('float64')
mandrill = mandrill/255
plt.imshow(mandrill)

def rgb2cmy(img):
    img = np.copy(img)
    img[:,:,0] = 1 - img[:,:,0]
    img[:,:,1] = 1 - img[:,:,1]
    img[:,:,2] = 1 - img[:,:,2]
    return img

def cmy2rgb(img):
    img = np.copy(img)
    img[:,:,0] = 1 - img[:,:,0]
    img[:,:,1] = 1 - img[:,:,1]
    img[:,:,2] = 1 - img[:,:,2]
    return img

img = np.copy(mandrill)
#def rgb2hsi(img):
red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

I = (red + green + blue)/3
S = 1 - ((3/(red + green + blue)) * min(red, min(green, blue)))
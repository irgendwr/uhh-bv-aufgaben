# -*- coding: utf-8 -*-
"""
Aufgabenblatt 5, Aufgabe 3
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import math

mandrill = imread("./mandrillFarbe.png").astype(np.float)
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
S = np.zeros((img.shape[0], img.shape[1]))
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if(red[y, x] == green[y, x] == blue[y, x] == 0):
            S[y, x] = 1
        else:
            S[y, x] = 1 - ((3/(red[y, x] + green[y, x] + blue[y, x])) * min(red[y, x], min(green[y, x], blue[y, x])))

theta = np.zeros((img.shape[0], img.shape[1]))
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        if(red[y, x] == green[y, x] == blue[y, x]):
            theta[y, x] = 0
        else:
            theta[y, x] = math.acos((0.5 * ((red[y, x] - green[y, x]) + (red[y, x] - blue[y, x]))) / math.pow((math.pow((red[y, x] - green[y, x]), 2) + ((red[y, x] - blue[y, x]) * (green[y, x] - blue[y, x]))), 0.5))
            theta[y, x] = math.degrees(theta[y, x])


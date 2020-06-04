# -*- coding: utf-8 -*-
"""
Aufgabenblatt 5, Aufgabe 3
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import math

mandrill = imread("./mandrillFarbe.png")
plt.imshow(mandrill)

def rgb2cmy(image):
    img = np.copy(image).astype(np.float)
    img = img/255
    img[:,:,0] = 1 - img[:,:,0]
    img[:,:,1] = 1 - img[:,:,1]
    img[:,:,2] = 1 - img[:,:,2]
    img = (img*255).astype(np.uint8)
    return img

def cmy2rgb(image):
    img = np.copy(image)
    img = np.copy(image).astype(np.float)
    img = img/255
    img[:,:,0] = 1 - img[:,:,0]
    img[:,:,1] = 1 - img[:,:,1]
    img[:,:,2] = 1 - img[:,:,2]
    img = (img*255).astype(np.uint8)
    return img

def rgb2hsi(image):
    img = np.copy(image).astype(np.float)
    img = img/255
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    
    theta = np.zeros((img.shape[0], img.shape[1]))
    H = np.zeros((img.shape[0], img.shape[1]))
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if(red[y, x] == green[y, x] == blue[y, x]):
                theta[y, x] = 0
                H[y, x] = theta[y, x]
            else:
                theta[y, x] = math.acos((0.5 * ((red[y, x] - green[y, x]) + (red[y, x] - blue[y, x]))) / math.pow((math.pow((red[y, x] - green[y, x]), 2) + ((red[y, x] - blue[y, x]) * (green[y, x] - blue[y, x]))), 0.5))
                theta[y, x] = np.degrees(theta[y, x])
                if blue[y, x] > green[y, x]:
                    H[y, x] = 360 - theta[y, x]
                else:
                    H[y, x] = theta[y, x]
    
    S = np.zeros((img.shape[0], img.shape[1]))
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if(red[y, x] == green[y, x] == blue[y, x] == 0):
                S[y, x] = 1
            else:
                S[y, x] = 1 - ((3/(red[y, x] + green[y, x] + blue[y, x])) * min(red[y, x], min(green[y, x], blue[y, x])))
    
    I = (red + green + blue)/3
      
    return np.dstack((H, S, I))

def hsi2rgb(image):
    img = np.copy(image)
    H = img[:,:,0]
    S = img[:,:,1]
    I = img[:,:,2]
    
    red = np.zeros((img.shape[0], img.shape[1]))
    green = np.zeros((img.shape[0], img.shape[1]))
    blue = np.zeros((img.shape[0], img.shape[1]))
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if(0 <= H[y, x] < 120):
                hue = H[y, x]
                blue[y, x] = I[y, x] * (1 - S[y, x])
                red[y, x] = I[y, x] * (1 + ((S[y, x] * math.cos(np.radians(hue))) / (math.cos(np.radians(60 - hue)))))
                green[y, x] = (3 * I[y, x]) - (red[y, x] + blue[y, x])
            
            elif(120 <= H[y, x] < 240):
                hue = H[y, x] - 120
                red[y, x] = I[y, x] * (1 - S[y, x])
                green[y, x] = I[y, x] * (1 + ((S[y, x] * math.cos(np.radians(hue))) / (math.cos(np.radians(60 - hue)))))
                blue[y, x] = (3 * I[y, x]) - (red[y, x] + green[y, x])
            
            elif(240 <= H[y, x] < 360):
                hue = H[y, x] - 240
                green[y, x] = I[y, x] * (1 - S[y, x])
                blue[y, x] = I[y, x] * (1 + ((S[y, x] * math.cos(np.radians(hue))) / (math.cos(np.radians(60 - hue)))))
                red[y, x] = (3 * I[y, x]) - (green[y, x] + blue[y, x])
    
    return (np.dstack((red, green, blue)) * 255).astype(np.uint8)

"""
Funktion, um aus Spaß den Farbwert eines RGB-Bilds zu ändern ^^
"""
def changeHue(image, shift):
    img = np.copy(image)
    img = rgb2hsi(img)
    img[:,:,0] = (img[:,:,0] + shift) % 360
    img = hsi2rgb(img)
    return img
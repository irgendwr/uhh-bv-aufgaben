# -*- coding: utf-8 -*-
"""
Aufgabenblatt 1, Aufgabe 5
"""

import numpy as np
from skimage.io import imread
import time

#1.
mandrill = imread("./mandrill.png")

def loop(img):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y, x] > 99 and img[y, x] < 200:
                pass

#2.
def broadcast(img):
    a = img > 99
    b = img < 200
    #c = a * b       #Zusammenfügen beider Arrays, für >99 UND <200
    
#3.
def timeDiff(img):
    startLoop = time.time()
    for i in range(100):
        loop(img)
    endLoop = time.time()
    print("Zeit mit Schleifen: " + str(endLoop - startLoop))
    
    startBroacast = time.time()
    for i in range(100):
        broadcast(img)
    endBroadcast = time.time()
    print("Zeit mit Broadcast: " + str(endBroadcast - startBroacast))
    print("Zeitdifferenz: " + str((endLoop - startLoop) - (endBroadcast - startBroacast)))

"""
Zeit mit Schleifen: 67.02881479263306
Zeit mit Broadcast: 0.030027151107788086
Zeitdifferenz: 66.99878764152527
"""
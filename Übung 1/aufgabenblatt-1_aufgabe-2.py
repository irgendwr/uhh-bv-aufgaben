# -*- coding: utf-8 -*-
"""
Aufgabenblatt 1, Aufgabe 2
"""

import numpy as np

#1.
u = np.zeros((100))

#2.
v = np.array([0,1,2,3,4,5,6,7,8,9,10,11])

#3.
m = np.reshape(v, (3,4))        #v in 3 Zeilen und 4 Spalten

#4.
m = m * 1.2

#5.
m = m.astype(np.int)

#6.
m = m * 1.2     #Matrix wird wieder vom Datentyp float64

#7.
mxm = m * m
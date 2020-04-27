# -*- coding: utf-8 -*-
"""
Aufgabenblatt 1, Aufgabe 6
"""

import numpy as np
from skimage.io import imread

#1.
mandrill = imread("./mandrill.png")

#2.
minimum = np.min(mandrill)
print("Minimum: " + str(minimum))
maximum = np.max(mandrill)
print("Maximum: " + str(maximum))
mean = np.mean(mandrill)
print("Durchschnitt: " + str(mean))
stdev = np.std(mandrill)
print("Standardabweichung: " + str(stdev))
print()

#3.
y,x = np.unravel_index(np.argmin(mandrill), mandrill.shape)
print("Minimum bei x: " + str(x) + " und y: " + str(y))

y,x = np.unravel_index(np.argmax(mandrill), mandrill.shape)
print("Maximum bei x: " + str(x) + " und y: " + str(y))
print()

#4.
mandrillBinary = mandrill % 2       #Gerade Zahlen werden zu 0, ungerade zu 1
even = (mandrill.shape[0] * mandrill.shape[1]) - np.count_nonzero(mandrillBinary)     #Zieht Anzahl ungerader Pixel von Gesamtpixlanzahl ab
print("Anzahl gerader Werte: " + str(even))
odd = np.count_nonzero(mandrillBinary)
print("Anzahl ungerader Werte: " + str(odd))
print()

#5.
"""
Dies braucht vielleicht ein wenig Erklärung...
Mit argwhere kann man die Indize von non-zero Elementen erhalten. Über die Modulo-Operation
sind alle geraden Werte gleich 0. Folglich muss das Array invertiert werden. Da der
Datentyp aber uint8 ist, ist das Inverse von 0 aber 255, weshalb der Datentyp zu bool geändert werden muss.
"""
mandrillBinaryInv = mandrillBinary.astype(bool)
mandrillBinaryInv = np.invert(mandrillBinaryInv)        #Invertiert gerade zu ungerade Werte
evenArray = np.argwhere(mandrillBinaryInv == 1)
print("Koordinaten aller geraden Werte:")
print(evenArray)
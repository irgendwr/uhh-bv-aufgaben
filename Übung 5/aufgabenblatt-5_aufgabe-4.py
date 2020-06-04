# -*- coding: utf-8 -*-
"""
Aufgabenblatt 5, Aufgabe 4
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import skimage.color

#1.
mandrill = imread("./mandrillFarbe.png")
plt.imshow(mandrill)

#2.
mandrillInv = np.invert(mandrill)
plt.imshow(mandrillInv)

"""
Eine Invertierung der einzelnen Farkbanäle im RGB-Modell ist wie eine Konvertierung
ins CMY-Modell, also wird jedes Rot zu Cyan, Grün zu Magenta und Blau zu Gelb.
"""

#3.
mandrillRed = mandrill[:,:,0]
plt.imshow(mandrillRed, cmap="Greys_r")

mandrillGreen = mandrill[:,:,1]
plt.imshow(mandrillGreen, cmap="Greys_r")

mandrillBlue = mandrill[:,:,2]
plt.imshow(mandrillBlue, cmap="Greys_r")

"""
Die einzelnen Graustufenbilder zeigen an, wie hoch der jeweilige Farbwert
an einer Position ist, wobei Schwarz keine Farbe und Weiß viel der jeweiligen
Farbe bedeutet. 
"""

#4.
mandrillBGR = np.dstack((mandrillBlue, mandrillGreen, mandrillRed))
plt.imshow(mandrillBGR)

"""
Da nun die Farbwerte des jeweils anderen Kanals genommen werden, sind nun alle
Bereiche, die vorher Rot waren Blau und vorher Blau nun Rot.
"""

#5.
mandrillGray = np.mean(np.array((mandrillRed, mandrillGreen, mandrillBlue)), axis=0)
plt.imshow(mandrillGray, cmap="Greys_r")

#6.
mandrillHSV = skimage.color.rgb2hsv(mandrill)
mandrillHSV[:,:,1] = 1
mandrillSat = skimage.color.hsv2rgb(mandrillHSV)
plt.imshow(mandrillSat)

mandrillHSV = skimage.color.rgb2hsv(mandrill)
mandrillHSV[:,:,1] = 0
mandrillSat = skimage.color.hsv2rgb(mandrillHSV)
plt.imshow(mandrillSat)

"""
Bei voller Sättigung ist das Bild farbiger, da immer ein Farbkanal auf 0 gesetzt wird,
weshalb sich nach den additiven Farbmodell kein Grau bilden kann, während die beiden
anderen Kanäle hochgesetzt werden.
Bei komplett heruntergedrehter Sättigung sieht das Bild wie ein Graustufenbild aus,
da alle Farbkanäle auf den selben Wert gebracht werden.
"""

#7.
mandrillHSV = skimage.color.rgb2hsv(mandrill)
mandrillHSV[:,:,0] = (mandrillHSV[:,:,0] + 60/360) % 1
mandrillHue60 = skimage.color.hsv2rgb(mandrillHSV)
plt.imshow(mandrillHue60)

mandrillHSV = skimage.color.rgb2hsv(mandrill)
mandrillHSV[:,:,0] = (mandrillHSV[:,:,0] + 120/360) % 1
mandrillHue120 = skimage.color.hsv2rgb(mandrillHSV)
plt.imshow(mandrillHue120)

mandrillHSV = skimage.color.rgb2hsv(mandrill)
mandrillHSV[:,:,0] = (mandrillHSV[:,:,0] + 240/360) % 1
mandrillHue240 = skimage.color.hsv2rgb(mandrillHSV)
plt.imshow(mandrillHue240)

"""
Entsprechend eines Farbkreis, wo
0° bzw 360°: Rot
60°: Gelb
120°: Grün
180°: Cyan
240°: Blau
300°: Magenta

Bei einer Verschiebung um 60° wird Rot zu Gelb, Grün zu Cyan und Blau zu Magenta eingefärbt.
Bei einer Verschiebung um 120° wird Rot zu Grün, Grün zu Blau und Blau zu Rot eingefärbt.
Bei einer Verschiebung um 240° wird Rot zu Blau, Grün zu Rot und Blau zu Grün eingefärbt.
"""
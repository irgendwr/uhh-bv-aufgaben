# -*- coding: utf-8 -*-
"""
Aufgabenblatt 9, Aufgabe 5
"""

import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

#1.
mandrill = imread("./mandrill_hBars.png")

mandrillDFT = np.fft.fft2(mandrill)
mandrillDFTShifted = np.fft.fftshift(mandrillDFT)
mandrillDFTShiftedReal = np.abs(mandrillDFTShifted)
mandrillDFTShiftedPhase = np.angle(mandrillDFTShifted)

plt.figure(1)
plt.imshow(mandrill, cmap="Greys_r")
plt.figure(2)
plt.imshow(np.log(mandrillDFTShiftedReal), cmap="Greys_r")  # Logarithmische Darstellung
#plt.imsave("./mandrillDFTShiftedReal.png", np.log(mandrillDFTShiftedReal), cmap="Greys_r")
plt.figure(3)
plt.imshow(mandrillDFTShiftedPhase, cmap="Greys_r")

"""
Die Vier Punkte, bei denen die Störung sichtbar ist, befinden sich Vertikal in der
Mitte des Bildes (x=256), bei ungefähr y= 51, 154, 358 und 461
Der Abstand zwischen den zwei nächsten Punkten zum Zentrum beträgt folglich ungefähr 102.

Um jeden Pixel des Spektrums mit einen größeren Abstand auf 0 zu setzen, wird
eine Maske mit einen Kreis genutzt, dessen Radius der Abstand ist.
"""

def circle(posX, posY, radius):
    xx, yy = np.mgrid[:radius*2,:radius*2]
    circle = (xx - radius)**2 + (yy - radius)**2
    circle = circle < radius**2
    circle = circle[1:,1:]
    
    img = np.zeros((512,512))
    img[posX-radius:posX+radius-1, posY-radius:posY+radius-1] = circle
    
    return img

mask = circle(256,256,102-10)
mandrillDFTShiftedRealNew1 = mandrillDFTShiftedReal * mask

mandrillDFTShiftedNew1 = mandrillDFTShiftedRealNew1 * np.exp(1j*mandrillDFTShiftedPhase)
mandrillNew1 = np.fft.ifftshift(mandrillDFTShiftedNew1)
mandrillNew1 = np.fft.ifft2(mandrillNew1)
mandrillNew1 = np.real(mandrillNew1)

plt.figure(4)
plt.imshow(np.log(mandrillNew1), cmap="Greys_r")

"""
Während die horizontalen Linien nicht mehr sichtbar sind, wurde das gesamte Bild
stark aufgehellt.
Effektiv wurde ein (ideal-)low-pass-Filter angewendet, weil alle hohen Frequenzen auf
0 gesetzt wurden.
"""

#2.
def gauss2d(x, y, mx, my, s):
    return 1. / (2. * np.pi * s * s) * np.exp(-((x - mx)**2. / (2. * s**2.) + (y - my)**2. / (2. * s**2.)))

weights = np.zeros_like(mandrillDFTShiftedReal)
for y in range(mandrillDFTShiftedReal.shape[0]):
    for x in range(mandrillDFTShiftedReal.shape[1]):
        weights[y,x] = gauss2d(x,y,256,256,30)

mandrillDFTShiftedRealNew2 = mandrillDFTShiftedReal * weights

mandrillDFTShiftedNew2 = mandrillDFTShiftedRealNew2 * np.exp(1j*mandrillDFTShiftedPhase)
mandrillNew2 = np.fft.ifftshift(mandrillDFTShiftedNew2)
mandrillNew2 = np.fft.ifft2(mandrillNew2)
mandrillNew2 = np.real(mandrillNew2)

plt.figure(5)
plt.imshow(np.log(mandrillNew2), cmap="Greys_r")

"""
Die horizontalen Linien sind entfernt und das Bild wird weniger aufgehellt,
allerdings wirkt es jetzt ein wenig weichgezeichnet.
Effektiv wurde ein Gaussian-low-pass-Filter angewendet.
"""

#3.
mandrillDFTShiftedRealNew3 = np.copy(mandrillDFTShiftedReal)
mandrillDFTShiftedRealNew3[51-10:52+10,256-10:257+10] = 0
mandrillDFTShiftedRealNew3[154-10:155+10,256-10:257+10] = 0
mandrillDFTShiftedRealNew3[358-10:359+10,256-10:257+10] = 0
mandrillDFTShiftedRealNew3[461-10:462+10,256-10:257+10] = 0

mandrillDFTShiftedNew3 = mandrillDFTShiftedRealNew3 * np.exp(1j*mandrillDFTShiftedPhase)
mandrillNew3 = np.fft.ifftshift(mandrillDFTShiftedNew3)
mandrillNew3 = np.fft.ifft2(mandrillNew3)
mandrillNew3 = np.real(mandrillNew3)

plt.figure(6)
plt.imshow(mandrillNew3, cmap="Greys_r")
#plt.imsave("./mandrill_hBars_corrected.png", mandrillNew3, cmap="Greys_r")
#plt.figure(7)
#plt.imshow(np.log(mandrillDFTShiftedRealNew3), cmap="Greys_r")     # Zeigt bearbeitetes Fourierspektrum an

"""
Als Ergebniss entsteht ein scharfes Bild, der (unfgefähr) gleichen Helligkeit,
aber ohne (bzw. mit kaum erkennbaren) horizontalen Linien.
Effektiv wurde ein Notch-Filter angewendet.
"""
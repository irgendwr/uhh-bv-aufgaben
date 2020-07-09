# -*- coding: utf-8 -*-
"""
Aufgabenblatt 9, Aufgabe 4
"""

import numpy as np
import skimage.filters
import matplotlib.pyplot as plt

#1.
def square(posX, posY, width, height):
    img = np.zeros((256,256))
    img[posX-int(np.floor(width/2)):posX+int(np.ceil(width/2)),posY-int(np.floor(height/2)):posY+int(np.ceil(height/2))] = 1
    
    return img

square = square(128,128,10,5)   # Aufgabe 1 bis 3
#square = square(128,128,5,10)   # Aufgabe 4.1
#square = square(128,128,20,20)   # Aufgabe 4.2

plt.figure(1)
plt.imshow(square, cmap="Greys_r")

#2.
squareDFT = np.fft.fft2(square)

"""
F(0,0) = 50
Der Wert an der Stelle sagt an, dass die Amplitude der ersten Basisfunktion 50 beträgt.
"""

#3.
squareDFTShifted = np.fft.fftshift(squareDFT)
squareDFTShiftedReal = np.abs(squareDFTShifted)
squareDFTShiftedPhase = np.angle(squareDFTShifted)

plt.figure(2)
plt.imshow(squareDFTShiftedReal, cmap="Greys_r")
plt.figure(3)
plt.imshow(squareDFTShiftedPhase, cmap="Greys_r")

"""
Im Fourierspektrum erkennt man hohen Intensitäten in der Mitte, welche sich
vertikal und horizontal abgeschwächt wiederholen.

Im Phasenspektrum erkennt man eine hellere (oben) und dunklere (unten) Hälfte,
mit einzelnen kleinen Kreisen in beiden Hälften.

Das Fourierspektrum lässt sich so interpretieren, dass es sehr viele niedrige
Frequenzen, also überwiegend homogene Flächen, gibt, während der Mangel an
hohen Frequenzen (Intensitäten in den Ecken) auf wenige Kanten hinweist.
Außerdem sind alle vorhandene Kanten entweder horizontal, oder vertikal, weil
es nur weitere intensitäten auf der Horizontalen/Vertikalen gibt. Gäbe es
schräge Kanten, würden im Spektrum diagonale Flächen/Linien entstehen.
"""

#4.
"""
Veränderte Bilder in Zeile 18 und 19.

Bei vertauschter Höhe und Breite sind beide Spektren um 90 Grad gedreht.
Dies lässt sich dadurch erklären, dass durch das Vertauschen von Höhe und Breite
das Rechteck letzlich ebenfalls um 90 Grad gedreht wurde.

Bei einen Rechteck der Größe 20x20 befinden sich die meisten Intensitäten
in der Mitte und sind gleich groß, da es nun "gleich viele" horizontale,
wie vertikale Kanten existieren.
Das Phasenspektrum ist immer noch in zwei Hälften geteilt, allerdings geht die
Trennung nun diagonal, statt horizontal/vertikal durch das Spektrum.
"""

#5.
def circle(posX, posY, radius):
    xx, yy = np.mgrid[:radius*2,:radius*2]
    circle = (xx - radius)**2 + (yy - radius)**2
    circle = circle < radius**2
    circle = circle[1:,1:]
    
    img = np.zeros((256,256))
    img[posX-radius:posX+radius-1, posY-radius:posY+radius-1] = circle
    
    return img

circle = circle(128,128,10)

plt.figure(4)
plt.imshow(circle, cmap="Greys_r")

#circle = skimage.filters.gaussian(circle, 10)   # Weichzeichnung für Aufgabe 5

circleDFT = np.fft.fft2(circle)
circleDFTShifted = np.fft.fftshift(circleDFT)
circleDFTShiftedReal = np.abs(circleDFTShifted)
circleDFTShiftedPhase = np.angle(circleDFTShifted)

plt.figure(5)
plt.imshow(circleDFTShiftedReal, cmap="Greys_r")
#plt.imshow(np.log(circleDFTShiftedReal), cmap="Greys_r")    # Logarithmische Darstellung
plt.figure(6)
plt.imshow(circleDFTShiftedPhase, cmap="Greys_r")

"""
Beim normalen Kreis breiten sich im Fourierspektrum die intensitäten vom Mittelpunkt
wellenmäßig nach außen aus und werden schwächer.
Das Phasenspektrum besitzt ein sich wiederholendes Muster, welches um 45 Grad
gedreht ist und erneut aus vielen kleinen Kreisen besteht.

Nach Anwendung des Gauss-Filters befindet sich im Fourierspektrum nur noch
ein weißer Punkt in der Mitte, ohne das Wellenmuster.
Dies lässt sich dadurch erklären, dass durch das Weichzeichnen keine starken
Kanten im Bild mehr vorhanden sind, wodurch die Frequenzen kleiner wurden und
sich die intensitäten nun mehr in der Mitte des Spektrums aufhalten.
Effektiv wurde durch das Weichzeihnen ein Low-pass-Filter angewendet.

Das Phasenspektrum besitzt zusätzlich zum wiederholenden Muster nun anstatt
der Kreise kleinere Vierecke, welche horizontal und vertikal durch das Spektrum verlaufen.
"""
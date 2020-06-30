# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 8

### Aufgabe 3

1. Die Operatoren sind entsprechend ihrer Himmelsrichtung angerichtet (Norden oben, Osten rechts, etc.):

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 8\aufgabenblatt-8_aufgabe-3_1.jpg" style="zoom: 33%;" />

   <div style="page-break-after: always;"></div>

2. Mit Sobel-Operatoren kann die Gradientenrichtung erkannt werden, indem man sie nach folgenden Muster aufbaut:
   Beispiel für "Norden":

<img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 8\aufgabenblatt-8_aufgabe-3_2.jpg" style="zoom:50%;" />



Falls der Gradient nach Norden zeigt, bedeutet dies, dass über dem Kern des Filters ein höherer Wert steht, als unter ihm. Durch die Anwendung des Filters entsteht also nur ein hohes Ergebnis, wenn dieser Fall eintrifft, da prinzipiell ein ein kleiner Wert (dunkel) von einen hohen (hell) abgezogen wird.

Um es auf den Sobel-Filter zu übertragen, werden die Gewichte 2, bzw. -2 benutzt, um die Ableitung zu bilden, sowie zwei benachbarten 1, bzw. -1 um das Bild zusätzlich zu glätten.

Generell gilt: Die 2 liegt an der Stelle im Filter, auf welche Orientierung man prüfen will. Benachbart am Rand kommen dann die zwei Einsen neben die zwei. Gespiegelt an beiden Achsen kommen dann die invertierten Gewichte. Die übrigen Werte im Filter werden auf 0 gesetzt.
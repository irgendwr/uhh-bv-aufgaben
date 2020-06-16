# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 6

### Aufgabe 1

1. Ermittelt das nicht normierte Histogramm mit 8 bins (0, 1, . . . 7) und zeichnet es auf.

   |  Bin   |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |
   | :----: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
   | Anzahl |  2   |  2   |  1   |  4   |  3   |  0   |  1   |  3   |

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 6\aufgabenblatt-6_aufgabe-1_1.jpg" style="zoom: 25%;" />

2. Normiert das erzeugte Histogramm nun und stellt es ebenfalls grafisch dar.

   |        Bin        |   0   |   1   |   2    |  3   |   4    |  5   |   6    |   7    |
   | :---------------: | :---: | :---: | :----: | :--: | :----: | :--: | :----: | :----: |
   | Anzahl (normiert) | 0.125 | 0.125 | 0.0625 | 0.25 | 0.1875 |  0   | 0.0625 | 0.1875 |

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 6\aufgabenblatt-6_aufgabe-1_2.jpg" style="zoom: 25%;" />

   

   

3. Berechnet auf Basis des normierten Histogramms das kumulierte Histogramm und skizziert es ebenfalls.

   |        Bin         |   0   |  1   |   2    |   3    |  4   |  5   |   6    |  7   |
   | :----------------: | :---: | :--: | :----: | :----: | :--: | :--: | :----: | :--: |
   | Anzahl (kumuliert) | 0.125 | 0.25 | 0.3125 | 0.5625 | 0.75 | 0.75 | 0.8125 |  1   |

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 6\aufgabenblatt-6_aufgabe-1_3.jpg" style="zoom: 25%;" />

4. Berechnet aus einem der Histogramme den Mittelwert des Bildes und notiert dabei euren Rechenweg.

   Berechnung mit Histogramm aus 1.: $(2 \cdot 0 + 2 \cdot 1 + 1 \cdot 2 + 4 \cdot 3 + 3 \cdot 4 + 0 \cdot 5 + 1 \cdot 6 + 3 \cdot 7) / 16 = 3.4375$
   Der Mittelwert beträgt 3.4375.

   

5. Ermittelt aus einem der Histogramme ebenso die Varianz des Bildes und haltet erneut euren Rechenweg fest.

   Berechnung mit Histogramm aus 1.:
   $(2 \cdot (0 - 3.4375)^2 + 2 \cdot (1 - 3.4375)^2 + 1 \cdot (2 - 3.4375)^2 + 4 \cdot (3 - 3.4375)^2 + 3 \cdot (4 - 3.4375)^2 + 0 \cdot (5 - 3.4375)^2 +\\ 1 \cdot (6 - 3.4375)^2 + 3 \cdot (7 - 3.4375)^2) / 16 \Rightarrow$

   $(2 \cdot 11.8164 + 2 \cdot 5.9414 + 1 \cdot 2.0664 + 4 \cdot 0.1914 + 3 \cdot 0.3164 + 0 \cdot 2.4414 + 1 \cdot 6.5664 + 3 \cdot 12.6914) / 16 \Rightarrow$

   $(23,6328 + 11.8828 + 2.0664 + 0.7656 + 0.9492 + 0 + 6.5664 + 38.0742) / 16 \approx 5.2460$

   Die Varianz beträgt 5.2460.

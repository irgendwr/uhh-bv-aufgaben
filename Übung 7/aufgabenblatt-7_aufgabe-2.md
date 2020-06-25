# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 6

### Aufgabe 2

1.

Die Normierung auf 1 von Glättungsfilterkernen wird durchgeführt, damit die Helligkeit (Mittelwert) des Bildes erhalten bleibt und nicht dunkler/heller wird.



Beispiel 1: Würde der Kern auf beispielsweise 0.5 normiert werden, würde sich der Mittelwert halbieren und das Ergebnis wäre dunkler.

Bild: 0 | 2  5  9  3  1 | 0, mit Mittelwert 4

Kernel: | 1  1  1 |, normiert auf 0.5: | 1/6  1/6  1/6 |

Gefaltetes Bild| 7/6  16/6  17/6  13/6  4/6 |, mit Mittelwert (57/6) / 5 = 1.9



Beispiel 2: Würde der Kern auf beispielsweise 2 normiert werden, würde sich der Mittelwert verdoppeln und das Ergebnis wäre heller.

Bild: 0 | 2  5  9  3  1 | 0, mit Mittelwert 4

Kernel: | 1  1  1 |, normiert auf 2: | 2/3  2/3  2/3 |

Gefaltetes Bild| 14/3  32/3  34/3  26/3  8/3 |, mit Mittelwert (114/3) / 5 = 7.6




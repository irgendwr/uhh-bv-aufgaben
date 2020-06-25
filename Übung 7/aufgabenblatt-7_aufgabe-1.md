# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 6

### Aufgabe 1

Da die Kernel alle der Größe $3 \times 3$ entsprechen, müssen die Bilder um $(3 - 1) / 2$, also um 1 Pixel mit Nullen umrahmt werden:

<img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_1.png" style="zoom:25%;" />



Die normierten Kernels für Korrelation (Oben) und Faltung (Unten):

<img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_2.png" style="zoom:25% ; "/>



$k_1$ bildet den Mittelwert der benachbarten Pixel und zeichnet somit das Bild weich.

$k_2$ produziert einen Effekt ähnlich der Bewegungsunschärfe. indem ein Pixel zu $\frac23$ aus den momentanen und zu $\frac13$ aus den links bzw. rechts benachbarten Pixel besteht.

$k_3$ ersetzt den momentanen Pixel durch den rechts (bzw. links) benachbarten Pixel und verschiebt dadurch das gesamte Bild nach links.



1. $k_1 \star f$ und $k_1 ☆ f$:

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_3.png" style="zoom:25%;"/>

   Faltung und Korrelation sind bei diesen Kernel äquivalent.

   

2. $k_1 \star g$ und $k_1 ☆ g$:

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_4.png" style="zoom:25%;" />

   Faltung und Korrelation sind bei diesen Kernel äquivalent.

   

3. $k_2 \star f$ und $k_2 ☆ f$:

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_5.png" style="zoom:25%;" />

   
   
   


4. $k_2 \star g$ und $k_2 ☆ g$:

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_6.png" style="zoom:25%;" />

   

5. $k_3 \star f$ und $k_3 ☆ f$:

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_7.png" style="zoom:25%;" />

   

6. $k_3 \star g$ und $k_3 ☆ g$:

   <img src="C:\Users\Maik\Desktop\Uni\Semester 4\Bildverarbeitung\Übung\Übung 7\aufgabenblatt-7_aufgabe-1_8.png" style="zoom:25%;" />


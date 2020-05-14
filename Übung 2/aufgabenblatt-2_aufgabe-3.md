# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 2

### Aufgabe 3

1. Ist das Abtasttheorem im Sinne der zeitlichen Abtastung der Propellerdrehung durch die Kamera erfüllt?

   Das Abtasttheorem besagt, dass ein Signal exakt wiedererlangt werden kann, wenn es mit einer Frequenz abgetastet wird, welche mindestens gleich der doppelten maximalen Frequenz $f_{max}$ des Signales entspricht.

   Da sich der Propeller 1000 mal die Minute dreht, beträgt die Frequenz:
   $f_{max} = \frac{1000}{1 ~\text{Minute}} = \frac{1000}{60 ~\text{Sekunden}} = 16,\overline{66} ~\text{Hz}$
   Das doppelte von $f_{max}$ beträgt folglich $33,\overline{33} ~\text{Hz}$.

   Die Kamera nimmt 30 Bilder pro Sekunde auf, besitzt also eine Abtastrate von $30 ~\text{Hz}$.

   Da die Abtastrate der Kamera ($30 ~\text{Hz}$) geringer ist, als das doppelte von $f_{max}$ ($33,\overline{33} ~\text{Hz}$), ist das Abtasttheorem nicht erfüllt.

   

2. Was wird schätzungsweise auf dem Video erkennbar sein und was nicht?

   Wahrscheinlich wird man einen Effekt erkennen, in welchen es so aussieht, als ob sich der Propeller relativ langsam dreht, da die Kamera den Propeller immer leicht verzögert aufnimmt, relativ zur letzten Umdrehung des Propellers im letzten Bild. Nach jeden Bild sieht es also so aus, als ob der Propeller nur ungefähr eine 1/9 Umdrehung gemacht hätte.

   

3. Ändert sich etwas, wenn eure Kamera statt 30 Bilder nun 60 Bilder pro Sekunde aufnehmen kann?

   Wenn die Kamera nun mit 60 Bildern pro Sekunde aufnimmt, erhöht sich die Frequenz auf $60 ~\text{Hz}$.
   Das doppelte von $f_{max}$ beträgt aber weiterhin $33,\overline{33} ~\text{Hz}$, weshalb nun das Abtasttheorem erfüllt ist, und man nun die richtige Rotation des Propellers erkennen kann.

   
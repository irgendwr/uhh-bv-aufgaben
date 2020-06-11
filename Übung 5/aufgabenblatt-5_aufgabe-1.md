# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 5

### Aufgabe 1

1. Beschreibt die Farbe jeweils natürlichsprachlich.

   a) Helles rosa: Jeder Farbkanal ist relativ hoch, weshalb die Farbe insgesamt hell ist. Da Grün und Blau gleich hoch sind, Rot aber höher, wird die Farbe einen leichten Rotstich haben, folglich ein helles rosa.

   b) Gesättigtes blau-türkis. Die Farbe besitzt einen sehr starken Blauanteil und einen schwächeren Grünanteil, weshalb der Farbton türkis mit stärkerer Tendenz zu blau ist. Der geringe Rot-Anteil im Vergleich zum hohen Blau-Anteil sorgt für eine hohe Saturation, folglich ist die Farbe ein gesättigtes blau-türkis.

   c) Dunkles Terrakotta. Die Magenta- und Gelb-Anteile erzeugen zusammen ein relativ ungesättigtes rot. Da CMY ein subtraktives Farbmodell ist, wird durch das hinzufügen von Cyan die Farbe insgesamt dunkler, ohne den Farbton zu ändern.

   

2. Rechnet die Farbwerte in den jeweils anderen Farbraum (RGB bzw. CMY) um.

   a) $[C, M, Y] = [256, 256, 256] - [R, G, B] \Rightarrow [256, 256, 256] - [256, 192, 192] = [0, 64, 64]$. Farbe `a` hat den CMY-Wert $[0, 64, 64]$.

   b) $[C, M, Y] = [256, 256, 256] - [R, G, B] \Rightarrow [256, 256, 256] - [64, 128, 256] = [192, 128, 0]$. Farbe `b` hat den CMY-Wert $[192, 128, 0]$.

   c) $[R, G, B] = [256, 256, 256] - [C, M, Y] \Rightarrow [256, 256, 256] - [128, 192, 192] = [128, 64, 64]$. Farbe `c` hat den RGB-Wert $[128, 64, 64]$.

   

3. Berechnet den Farbton, die Sättigung und die Intensität der Farbwerte im HSI-Modell.

   Vorbedingung: Alle Werte werden in den Intervall [0,1] normiert.
   $$
   I = \frac13(R + G + B)\\
   S = 1 - \frac{3}{(R + G + B)}[min(R, G, B)]\\
   H = \theta ~\text{wenn} ~ B \leq G \text{, sonst} ~ 360 - \theta\\
   \theta = cos^{-1}(\frac{\frac12 ((R - G) + (R - B))}{((R - G)^2 + (R - B) \cdot (G - B))^\frac12})
   $$
   

   a)
   $$
   I = \frac13(1 + 0.75 + 0.75) = \frac56 = 0.8\overline3\\
   S = 1 - \frac{3}{(1 + 0.75 + 0.75)} \cdot 0.75 = 0.1\\
   \theta = cos^{-1}(\frac{\frac12 ((1 - 0.75) + (1 - 0.75))}{((1 - 0.75)^2 + (1 - 0.75) \cdot (0.75 - 0.75))^\frac12}) = 0\\
   H = \theta ~\text{wenn} ~ B \leq G \text{, sonst} ~ 360 - \theta = 0
   $$
   Farbe `a` besitzt den HSI-Wert $[0, 0.1, 0.8\overline3]$, bzw. $[0, 25, 213]$.

   

   b)
   $$
   I = \frac13(0.25 + 0.5 + 1) = \frac{7}{12} = 0.58\overline3\\
   S = 1 - \frac{3}{(0.25 + 0.5 + 1)} \cdot 0.25 = \frac{4}{7} = 0.5714\\
   \theta = cos^{-1}(\frac{\frac12 ((0.25 - 0.5) + (0.25 - 1))}{((0.25 - 0.5)^2 + (0.25 - 1) \cdot (0.5 - 1))^\frac12}) = 139.1\\
   H = \theta ~\text{wenn} ~ B \leq G \text{, sonst} ~ 360 - \theta = 360 - 139.1 = 220.9
   $$
   Farbe `b` besitzt den HSI-Wert $[220, 0.5714, 0.58\overline3]$, bzw. $[220, 146, 149]$.

   

   c)
   $$
   I = \frac13(0.5 + 0.25 + 0.25) = \frac13 = 0.\overline3\\
   S = 1 - \frac{3}{(0.5 + 0.25 + 0.25)} \cdot 0.25 = 0.25\\
   \theta = cos^{-1}(\frac{\frac12 ((0.5 - 0.25) + (0.5 - 0.25))}{((0.5 - 0.25)^2 + (0.5 - 0.25) \cdot (0.25 - 0.25))^\frac12}) = 0\\
   H = \theta ~\text{wenn} ~ B \leq G \text{, sonst} ~ 360 - \theta = 0
   $$
   Farbe `c` besitzt den HSI-Wert $[0, 0.25, 0.\overline3]$, bzw. $[0, 64, 85]$.


# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 5

### Aufgabe 2

CMY zu HSI:
$$
I = \frac13((1 - C) + (1 - M) + (1 - Y))\\~\\
S = 1 - \frac{3}{(1 - C) + (1 - M) + (1 - Y)}[min((1 - C), (1 - M),(1 - Y))]\\~\\
H = \theta ~\text{wenn} ~ (1 - Y) \leq (1 - M) \text{, sonst} ~ 360 - \theta\\~\\
\theta = cos^{-1}(\frac{\frac12 (((1 - C) - (1 - M)) + ((1 - C) - (1 - Y)))}{(((1 - C) - (1 - M))^2 + ((1 - C) - (1 - Y)) \cdot ((1 - M) - (1 - Y)))^\frac12})
$$


HSI zu CMY:

Für Rot-Grün Sektor $(0^° \leq H \leq 120^°)$:
$$
Y = 1 - (I \cdot (1-S))\\
C = 1 - (I \cdot (1 + \frac{S \cdot cos(H)}{cos(60^° - H)}))\\
M = 1 - (3I - ((1 - C) + (1 - Y)))
$$
Für Grün-Blau Sektor $(120^° \leq H \leq 240^°)$:
$$
H = H - 120^°\\
C = 1 - (I \cdot (1-S))\\
M = 1 - (I \cdot (1 + \frac{S \cdot cos(H)}{cos(60^° - H)}))\\
Y = 1 - (3I - ((1 - C) + (1 - M)))
$$
Für Blau-Rot Sektor $(240^° \leq H \leq 360^°)$:
$$
H = H - 120^°\\
M = 1 - (I \cdot (1-S))\\
Y = 1 - (I \cdot (1 + \frac{S \cdot cos(H)}{cos(60^° - H)}))\\
C = 1 - (3I - ((1 - M) + (1 - Y)))
$$

# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 4

### Aufgabe 2

1. Gebt zu den drei Szenarien in Abbildung 2 die jeweilige Transformationsmatrix an.

a)
Spiegelung an der Y-Achse und Translation um X-1, Y+2:
$$
T =
\begin{bmatrix}
1 & 0 & -1\\
0 & 1 & 2\\
0 & 0 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
-1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
-1 & 0 & -1\\
0 & 1 & 2\\
0 & 0 & 1
\end{bmatrix}
$$
b)
Horizontale Scherung um 2, Vertikale Scherung um 2, Translation um X+1, Y+1:
$$
T =
\begin{bmatrix}
1 & 0 & 1\\
0 & 1 & 1\\
0 & 0 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
1 & 2 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
1 & 0 & 0\\
2 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 1\\
0 & 1 & 1\\
0 & 0 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
5 & 2 & 0\\
2 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
5 & 2 & 1\\
2 & 1 & 1\\
0 & 0 & 1
\end{bmatrix}
$$

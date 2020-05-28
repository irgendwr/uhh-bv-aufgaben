# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 4

### Aufgabe 3

Bildet die inversen Transformationsmatrizen.

1.
$$
\begin{bmatrix}
1 & 1 & 1\\
0 & 1 & 1\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z1 - Z2\\
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 1\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & -1 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z2 - Z3\\
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & -1 & 0\\
0 & 1 & -1\\
0 & 0 & 1
\end{bmatrix}\\
\text{Die Inverse Matrix von}
\begin{bmatrix}
1 & 1 & 1\\
0 & 1 & 1\\
0 & 0 & 1
\end{bmatrix}
\text{lautet}
\begin{bmatrix}
1 & -1 & 0\\
0 & 1 & -1\\
0 & 0 & 1
\end{bmatrix}
$$
2.
$$
\begin{bmatrix}
-2cos(\pi) & 2sin(\pi) & 2\\
sin(\pi) & -cos(\pi) & 0\\
0 & 0 & 1
\end{bmatrix}\\
\begin{bmatrix}
2 & 0 & 2\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z1 \cdot 0.5\\
\begin{bmatrix}
1 & 0 & 1\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
0.5 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z1 -Z3\\
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
0.5 & 0 & -1\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}\\
\text{Die Inverse Matrix von}
\begin{bmatrix}
-2cos(\pi) & 2sin(\pi) & 2\\
sin(\pi) & -cos(\pi) & 0\\
0 & 0 & 1
\end{bmatrix}
\text{lautet}
\begin{bmatrix}
0.5 & 0 & -1\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
0.5sin(\pi) & 0 & 1\\
0 & sin(\pi) & 0\\
0 & 0 & 1
\end{bmatrix}
$$
3.
$$
\begin{bmatrix}
1 & 0 & 2\\
2 & 3 & 4\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z2 - 2 \cdot Z1\\
\begin{bmatrix}
1 & 0 & 2\\
0 & 3 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z1 - 2 \cdot Z3\\
\begin{bmatrix}
1 & 0 & 0\\
0 & 3 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -2\\
-2 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
Z2 \cdot \frac13\\
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & -2\\
\frac{-2}3 & \frac13 & 0\\
0 & 0 & 1
\end{bmatrix}\\
\text{Die Inverse Matrix von}
\begin{bmatrix}
1 & 0 & 2\\
2 & 3 & 4\\
0 & 0 & 1
\end{bmatrix}
\text{lautet}
\begin{bmatrix}
1 & 0 & -2\\
\frac{-2}3 & \frac13 & 0\\
0 & 0 & 1
\end{bmatrix}
$$


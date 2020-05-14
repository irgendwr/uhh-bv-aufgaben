# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 2

### Aufgabe 4

Beweist, dass der Erwartungswert $E$ des Ergebnisses $\overline{g}(x,y)$ wiederum dem Bild $f(x,y)$ entspricht: $E(\overline{g}(x,y)) = f(x,y)$

Wenn $E(\overline{g}(x,y)) = f(x,y)$ gilt und $\overline{g}(x,y) = \frac{1}{M} \sum^M_{m=1} g_m(x,y)$, dann bedeutet dies, dass sich durch Nehmen des Mittelwertes das Rauschen $\eta(x,y)$ aller Bilder $g_m(x,y)$ gegenseitig aufhebt. Also:
$\lim \limits_{m \to \infty} \sum \eta_m(x,y) = 0$
Diese Annahme kann aufgrund des Gesetzes der großen Zahlen genommen werden, weil für das Gaußsche Rauschen der Erwartungswert $\eta = 0$ gesetzt wurde, folglich sich über viele $\eta(x,y)$ sich der Wert an 0 annähert.

Dadurch gelte: $f(x,y) + 0 = g_m(x,y)$ und folglich $E(\overline{g}(x,y)) = f(x,y)$, da in
$\overline{g}(x,y) = \frac{1}{M} \sum^M_{m=1} g_m(x,y)$ alle $g_m(x,y)$ gleich $f(x,y)$ entsprechen und der Mittelwert von $m ~f(x,y)$ identisch zu $f(x,y)$ ist.
# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 3

### Aufgabe 1

Beweist, dass $\sigma^2_{\overline g(x,y)} = \frac{1}{M} \sigma^2_{\eta(x,y)}$
$$
\sigma^2_{\overline g(x,y)} =
\sigma^2 (\frac{1}{M} \sum^M_{m=1} g_m(x,y)) =
\sigma^2 (\frac{1}{M} \sum^M_{m=1} f(x,y) + \eta_m(x,y)) =
\\
\sigma^2 (\frac{1}{M} \sum^M_{m=1} f(x,y)) +  \sigma^2 (\frac{1}{M} \sum^M_{m=1} \eta_m(x,y)) = 
\sigma^2 (f(x,y)) + \frac{1}{M} \sigma^2 (\sum^M_{m=1} \eta_m(x,y)) =
\\
0 + \frac{1}{M} \sigma^2 (\sum^M_{m=1} \eta_m(x,y))) = \frac{1}{M} \sigma^2_{\eta(x,y)}
$$


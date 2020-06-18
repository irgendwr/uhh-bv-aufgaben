# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 6

### Aufgabe 2

$$
\sigma^2 = \frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}}[I(x, y) - \mu_I]^2 \Rightarrow\\~\\~\\

\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}}[I(x, y)^2 - 2I(x, y) \cdot \mu_I + \mu_I^2] \Rightarrow\\~\\~\\

[\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} I(x, y)^2] - [\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} 2I(x, y) \cdot \mu_I] + [\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} \mu_I^2] \Rightarrow\\~\\~\\

[\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} I(x, y)^2] - [\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} 2I(x, y) \cdot \mu_I] + \mu_I^2 \Rightarrow\\~\\~\\

[\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} I(x, y)^2] - [2\mu \cdot \mu] + \mu_I^2 \Rightarrow\\~\\~\\

[\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} I(x, y)^2] - 2\mu^2 + \mu_I^2 \Rightarrow\\~\\~\\

[\frac{1}{N_{cols}N_{rows}} \sum_{x = 1}^{N_{cols}} \sum_{y = 1}^{N_{rows}} I(x, y)^2] - \mu_I^2
$$


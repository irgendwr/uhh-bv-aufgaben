# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 1

### Aufgabe 1

1. Wie kann die Anzahl der Zeilen und Spalten eines NumPy-Arrays bestimmt werden?

   Mit `.shape` kann man das Attribut `shape` eines NumPy-Arrays aufrufen, welches die jeweiligen Dimensionen und deren Größe beinhaltet. Die Anzahl der Zeilen steht an erster Stelle, die Anzahl an Spalten an zweiter Stelle.



2. Was unterscheidet die Funktionen `numpy.array` und `numpy.zeros`?

   `numpy.array` erzeugt ein NumPy-Array basierend auf eine Eingabe von einer Liste bzw. mehreren Listen. Die Anzahl an Listen und deren Inhalt bestimmen die Dimension und den Inhalt des NumPy-Arrays.

   `numpy.zeros` erzeugt ein NumPy-Array, welches komplett mit `0` gefüllt ist. Als Eingabe benötigt es nur die Dimension (Shape) des Arrays.



3. Wie kann der Datentyp eines gegebenen NumPy-Arrays ermittelt werden?

   Mit `.dtype` kann man das Attribut `dtype` eines NumPy-Arrays aufrufen, welches den Datentypen beinhaltet.



4. Was bedeutet `.T` hinter dem Variablennamen eines NumPy-Arrays? Beispielsweise: `a.T`

   Mit `.T` transponiert man eine Matrix, wodurch Zeilen zu Spalten und Spalten zu Zeilen werden.



5. Was machen die Funktionen `xlabel` und `ylabel` aus `matplotlib.pyplot`?

   Die Funktion `xlabel` benennt die X-Achse eines Plots.

   Die Funktion `ylabel` benennt die Y-Achse eines Plots.


# Bildverarbeitung Übung

Finn Jebsen, Jonas Bögle und Maik Simke

## Aufgabenblatt 3

### Aufgabe 5

Schaut euch die acht folgenden Python-Funktionen an und beantwortet zu jeder Funktion, ob es sich dabei um eine Punktoperation, eine Nachbarschaftsoperation, eine geometrische Transformation oder eine globale Operation handelt. Gebt jeweils eine kurze Begründung.

1. Bei der Funktion `a` handelt es sich um eine Punktoperation, da für den Ausgangspixel nur der momentane Wert des Pixel genommen und dieser um 1 erhöht wird.

   

2. Bei der Funktion `b` handelt es sich um eine Punktoperation, da das Ausgangspixel auf nur einen Pixel des Eingabebildes basiert, nämlich auf dem bei `img[x,y-1]`.

   

3. Bei der Funktion `c` handelt es sich um eine globale Operation, da für die Berechnung jedes Ausgangspixel das komplette Eingabebild benutzt werden muss. `np.max(img)` gibt den größten Wert aus dem kompletten Bilde heraus.

   

4. Bei der Funktion `d` handelt es sich um eine geometrische Transformation, genauer gesagt um eine Rotation um 180°.
   Für die Rotation gilt:
   Rotation um $\theta$: $T_{rot} = cos(\theta), -sin(\theta), sin(\theta), cos(\theta) \Rightarrow x' = xcos(\theta) - ysin(\theta),~ y' = ycos(\theta) + sin(\theta)$
   Mit `result[x,y] = img[int(x*cos(pi)-y*sin(pi)),int(x*sin(pi)+y*cos(pi))]` werden also die Intensitäten für die neuen `x,y`-Positionen für eine Rotation um $\pi = 180^°$ berechnet.

   

5. Bei der Funktion `e` handelt es sich um eine Nachbarschaftsoperation, da für das Ergebnis der Subtraktion die Werte der unteren Spalte von der der oberen Spalte abgezogen werden.
   `img[:,1:]` beinhaltet das Bild ohne erste Spalte, `img[:,:-1]` ohne letzte Spalte. Das Ergebnis hängt also von der benachbarten Spalte ab.

   

6. Bei der Funktion `f` handelt es sich um eine globale Operation, da das Ausgangspixel vom gesamten Bild abhängt, da man den Mittelwert des Eingabebildes vom Eingabebild abzieht. `np.full(img.shape,np.mean(img))` erzeugt ein Bild, wessen Pixel alle den Mittelwert des Eingabebildes besitzen.

   

7. Bei der Funktion `g` handelt es sich um eine Punktoperation, da jedes Ausgabepixel nur vom Eingabepixel abhängt. Da `if True` immer wahr ist, wird nur `result[x,y]=a` ausgeführt und weil `a = img[x,y]` wird jedes Eingabepixel direkt den Ausgabepixel gleich gesetzt.

   

8. Bei der Funktion `h` handelt es sich um eine Nachbarschaftsoperation, da für die Berechnung jedes Ausgabepixel die die komplette Spalte des Eingabebildes benutzt wird.
   `np.mean(img[:,y])` gibt den Mittelwert der momentanen Spalte zurück.
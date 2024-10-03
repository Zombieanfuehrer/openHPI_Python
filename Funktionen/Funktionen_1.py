# A1 ----
# Schreibe eine Funktion mit dem Namen `anzahl_verdoppeln`.
# Diese soll für eine Eingabe das Doppelte des Betrags zurückgeben.
# Negative Zahlen sollen positiv werden.
# Nutze dafür gerne die eingebaute Betragsfunktion (engl: absolute value)
# Den Parameternamen darfst du frei wählen (nutze deine Freiheit sinnvoll^^).
# Es geht hier um die Struktur einer Funktion, der Inhalt ist hier sehr kurz.

def anzahl_verdoppeln(verdopple):
    return abs(verdopple) * 2


# Wenn du die Funktion geschrieben hast, kannst du sie hiermit testen:
# (Einfach die Kommentarzeichen entfernen)
print("doppelt1:", anzahl_verdoppeln(-5.5) ) # soll 11 sein
print("doppelt2:", anzahl_verdoppeln(7)    ) # soll 14 sein
# Für die Bewertung wird deine Funktion mit weiteren Eingaben geprüft.


# A2 ----
# Nehmen wir mal an, für eine amerikanische Bäckerei zu arbeiten.
# Dort wird zur Dosierung  mal in gramm und mal in ounces (oz) gemessen.
# Ja, das ist eine schlechte Idee - aber für uns Programmierer kein Problem!
# Schreibe für das Backinformationssystem (BIS) eine Konvertierungsfunktion
# namens `oz2g`, die die Grammzahl auf eine Nachkommastelle gerundet zurückgibt.
# Hinweis: 1 ounce = 28.3495 gramm
# Hinweis: Falls runden für dich neu ist, einfach "Python runden" online suchen.
# Das ist generell beim Programmieren eine wichtige Fähigkeit!! :)

def oz2g(oz):
    g = oz * 28.3495
    return round(g, 1)

# Das folgende Beispiel einfach unkommentieren, wenn du soweit bist :)
print("unz:", oz2g(25)) # 708.7


# A3 ----
# Erstelle eine Funktion `quadratsummenwurzel` mit zwei Parametern.
# Sie soll die Wurzel der Summe zweier Quadratzahlen berechnen (und zurückgeben).
# In mathematischer Notation: sqrt(a^2 + b^2)  <- dies ist kein Python code!
# Hier kannst du frei wählen, ob du math.sqrt oder ** verwendest.

import math
def quadratsummenwurzel(no_1, no_2):
    a = no_1 ** 2
    b = no_2 ** 2
    return math.sqrt(a + b)

print("qsw1:", quadratsummenwurzel(13,8)) # 15.26... (Anzahl Kommastellen egal)
print("qsw2:", quadratsummenwurzel(3,4)) # 5.0

"""
Übrigens: wenn nicht anders angegeben, ist die Anzahl der Nachkommastellen egal.
In den Beispielen kürze ich oft einige weg, um auf die Struktur zu fokussieren.
"""

# Weiter geht's im nächsten Skript :)

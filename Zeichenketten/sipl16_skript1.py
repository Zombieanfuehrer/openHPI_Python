# A1 ----
# Wie viele Zeichen enthält die folgende Zeichenkette?
mary = 'Superkalifragilisticexpialigetisch'
anzahl_zeichen = len(mary)
print("az:", anzahl_zeichen)


# A2 ----
# Nutze ein F-String um die erwünschte Zeichenkette `ausgabe` zu erzeugen.
einrichtung = "Ernst von Bergmann Klinikum"
patienten = 973
ausgabe = f"Im Krankenhaus {einrichtung} sind derzeit {patienten} Patienten."
print(ausgabe)


# A3 ----
# Schreibe eine Funktion, die eine Zeichenkette als Eingabe erhält.
# Beginnt diese Zeichenkette mit einem Zeichen, das im Alphabet vor "M" kommt?
# Hinweis: dafür musst du keine Teilmenge der Zeichenkette betrachten.
# Beachte die Reihenfolge von Groß- und Kleinbuchstaben in Python:
print("d" < "Z") # False, weil "123" < "GROSS" < "klein"

def kleiner_als_M(eingabe):
    if eingabe[0].upper() < "M":
        return True
    else:
        return False
print("Anna vor M:", kleiner_als_M("Anna")) # soll True ausgeben
print("Rita vor M:", kleiner_als_M("Rita")) # soll False ausgeben

# Weiter geht's im nächsten Skript :)

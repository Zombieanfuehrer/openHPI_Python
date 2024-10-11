# Bonusaufgaben zur Vertiefung - nur bearbeiten, wenn du Zeit dafür hast.

# A8 -----
# `ist_patient` soll zeigen, ob die eingegebene ID zu einem Patienten gehört.
# Diese haben "pat" an den Buchstaben 3-5, siehe den Beispielen unten.
def ist_patient(i):
    return i[2:5] == "pat"
print("ip1:", ist_patient("H2doc73tk6z")) # False
print("ip2:", ist_patient("22pat0210_5")) # True
print("ip3:", ist_patient("222pat3")) # False (ist beim vierten Buchstaben)


# A9 ----
# `erste_buchstaben` soll von der eingegebenen Zeichenkette
# - die ersten drei Buchstaben anzeigen (print)
# - und angeben, ob die ersten beiden "wo" sind (Großschreibung ignorierend).
def erste_buchstaben(zk):
    tmp = zk.lower()[0:2]
    print(zk[0:3])
    return True if tmp == "wo" else False
print("eb1:",erste_buchstaben("wot52rl")) # wot + True
print("eb2:",erste_buchstaben("WOD52rl")) # WOD + True
print("eb3:",erste_buchstaben("skt83ws")) # skt + False


# A10 ----
# Lies den Witz in "sipl16_witz.txt" in Python ein.
# Erstelle eine Zeichenkette mit dem Namen `witz`, die den ganzen Inhalt enthält.
# Verwende Code, bei dem die Datei niemals geöffnet bleibt.
import os
path = os.path.join(".", "sipl16_witz.txt")
with open(path, "r") as file:
    witz = file.read()
print("witz:", witz)
# A11 ----
# Wie häufig kommt das Wort "Cent" im Witz vor?
# Hinweis: diese Aufgabe baut auf A10 auf.
# Der Witz soll nicht erneut eingelesen werden.
# Hinweis: collections.Counter ist für Listen, nicht Zeichenketten.
# Zeichenketten haben eine Count methode, die wir im Video noch nicht behandelt haben.
anzahl_cent = witz.count("Cent")
print("ac:", anzahl_cent)

# Heute gibt es viele Bonusaufgaben - im nächsten Skript noch einige weitere :)
# Alle sind optional und du darfst gerne mit der nächsten Lektion weitermachen.

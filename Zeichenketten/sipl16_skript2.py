# A4 ----
# Schreibe eine Funktion, die einen Satz als Zeichenkette entgegen nimmt.
# Teile den Satz in einzelne Worte auf (trennen an Leerzeichen).
def satz_zu_worten(satz):
    return satz.split(" ")
print("szw:", satz_zu_worten("Python ist cool.")) # ['Python', 'ist', 'cool.']


# A5 ----
# `anzahl_p` soll zählen, wie häufig der Buchstabe 'p' in der Eingabe vorkommt
# (ungeachtet ob groß oder klein geschrieben).
# Erinnerung: Methoden können verkettet werden!
# Hinweis: in Lektion 1.2 haben wir schonmal Buchstaben zählen lassen.
def anzahl_p(eingabe):
    return eingabe.upper().count("P")
print("ap:", anzahl_p("Python Programmierung: perfekt für Projekte")) # soll 4 sein


# A6 ----
# Schreibe eine Funktion, die die letzten 8 Zeichen der Eingabe zurückgibt.
def letzten_acht(eingabe):
    return eingabe[-8:]
print("la:", letzten_acht("asdfghjklqwert")) # soll jklqwert sein


# A7 ----
# Schreibe eine Funktion, die überprüft, ob die Eingabe "berry" enthält.
def hat_berry(eingabe):
    return "berry" in eingabe
print("hb1:", hat_berry("Apfel, Melone, Banane")) # False
print("hb2:", hat_berry("Erdbeere heißt auf Englisch 'strawberry'")) # True


# Die Bonusaufgaben in den nächsten Skripten bitte nur lösen, wenn du Zeit hast.
# Ansonsten hast du die erste (und schwerste) Woche geschafft!
# Nächste Woche bauen wir auf die bisherigen Inhalte auf - bis dann :)

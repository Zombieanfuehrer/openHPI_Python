# Weitere Bonusaufgaben - nur bearbeiten, wenn du Zeit dafür hast.

# Zeichenketten haben noch viel mehr Methoden als in der Lektion präsentiert.
# Siehe zB https://www.w3schools.com/python/python_ref_string.asp
# Die nächsten Aufgaben gehen über den Folieninhalt hinaus! (nutze den Link)

# Wir wollen digitalisierte Notizen aus einem Krankenhaus verarbeiten.
# `ist_op1` soll zeigen, ob ein Eintrag Bezug nimmt auf Operationssaal 1.
# Du kannst in diesen Aufgaben Methoden verketten!

def ist_op1(i):
    if i[0] == "0":
        i = i.replace("0", "o")
    if i.lower().replace(" ", "").startswith("op1"):
        return True
    if i.lower().replace(" ", "").startswith("operation1"):
        return True
    else:
        return False

# A12 ----
# Beginnt die Eingabe mit "op1"?
# Schreibe deinen Code in die Funktion oben (niemals mehrfach definieren).
# Hier ist eine kleine TestFunktion die dir hilft, deine Lösung zu entwickeln: 
def print_test_op1(i):
    print(ist_op1(i), " (", i, ")", sep="")
print_test_op1("op1: fertig") # Soll True sein
print_test_op1("Medikament verabreicht") # False

# A13 ----
# Auch wenn "OP1" groß geschrieben ist, soll es identifiziert werden.
# Füge oben die entsprechende Methode verkettet hinzu.
# Hinweis: die Reihenfolge ist wichtig: 
# zuerst alles klein schreiben lassen, danach schauen, ob es mit op1 beginnt.
print_test_op1("OP1 gereinigt") # True

# A14 ----
# Auch ein ausgeschriebenes "operation1" soll erkannt werden.
# Hinweis: Zeichenkettenteile ersetzen ist hier hilfreich.
# Schreibe auch dies oben in den Code, definiere die Funktion nicht mehrfach!
print_test_op1("Operation1 Dr Koch heute dran") # True

# A15 ----
# Die Digitalisierung hat manchmal den Buchstaben o als Zahl 0 interpretiert.
# Auch dann soll True herauskommen.
print_test_op1("0p1 morgen gesperrt!") # True

# A16 ----
# Von der OCR erkannte Leerzeichen sollen ignoriert werden.
# Tipp: eine regular expression (re Modul) ist möglich, aber nicht nötig.
print_test_op1("operation 1 braucht neue Handschuhe") # True
print_test_op1("OP  1 - Freigabe 13:15 Uhr") # True

# A17 ----
# Niemand will horizontal scrollen. 
# Dein Code oben soll nicht breiter als 80 Zeichen sein.
# Für Zeilenumbrüche siehe zB https://stackoverflow.com/q/4768941
# Im echten Leben verwendet man übrigens linter um Code-style zu prüfen.

# Dank eleganter Verkettung und eingebauter Zechenketten-Methoden passt die 
# gesamte Lösung für diese mittelkomplexe Aufgabe auf 2 Zeilen Inhalt (Körper).

# Spätestens jetzt viel Erfolg bei der nächsten Lektion :)

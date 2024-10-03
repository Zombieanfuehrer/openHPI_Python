# Die nachfolgende ist eine optionale Bonus-aufgabe.
# Bearbeite sie nur, wenn du die Zeit dafür hast!

# A5 ----
# Wir simulieren mal, dass eine Funktion (neben einer Berechnung) auch
# Information in eine Log-datei schreiben soll.
# Wir werden das der Einfachheit halber erstmal nur in der Konsole anzeigen.
# Die folgende Funktion soll zwei Dinge tun:
# - _print_ "Objekt ist eine Zahl: True" (oder False)
# - _return_ Die Klasse des Objekts.
# Hinweis: es gibt mehrere Zahlentypen (ganze, Fließkomma oder komplexe).
# Hinweis: if-else bedingte Code-ausführung ist hier NICHT erforderlich.

def geloggte_klasse(obj):
    result = isinstance(obj, (int, float, complex))
    print("Objekt ist eine Zahl:", result)
    return type(obj)


rueckgabe = geloggte_klasse(46)  # zeigt an:   Objekt ist eine Zahl: True
print("ausg1:", rueckgabe)  # <class 'int'>
rueckgabe = geloggte_klasse("46")  # Objekt ist eine Zahl: False
print("ausg2:", rueckgabe)  # <class 'str'>

# Spätestens jetzt viel Erfolg bei der nächsten Lektion :)

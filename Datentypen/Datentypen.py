# Hinweis: nutze die Tastenkürzel ALT + R und ALT + S für Ausführen / Bewerten.
# A1 ----
ergebnis_input_aufruf = "24.9"
# Ohne die obige Zeile zu ändern, konvertiere das Objekt zu einer "echten" Zahl

ergebnis_input_aufruf = float(ergebnis_input_aufruf)

# A2 ----
# Was ist jeweils der Datentyp der folgenden Objekte?
obj1 = "python"
obj2 = 42
obj3 = obj2 > 7

klasse1 = type(obj1) # verändere diesen Code um den Datentyp herauszufinden
klasse2 = type(obj2)
klasse3 = type(obj3)

print(klasse1)
print(klasse2)
print(klasse3)


# A3 ----
ein_objekt = False
# Überprüfe, ob das gegebene Objekt eins der folgenden Typen ist:
# Ganzzahl, logischer Wert oder Zeichenkette.
# Verwende die elegante Funktion von den Folien, keine Oder-Verknüpfungen.
# Für das Bewertungsskript: überprüfe in der gegebenen Reihenfolge der 3 Typen.

is_type_int_float_string = isinstance(ein_objekt, (int, bool, str))
print("ein_objekt ist: ", is_type_int_float_string)
# Diese Lektion ist kurz  - viel Erfolg bei der nächsten Einheit :)

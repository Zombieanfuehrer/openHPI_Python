# Ab dieser Lektion wird für viele Aufgaben eine Funktion verlangt.
# Dies ermöglicht dir viel Freiheit bei der Lösung.
# In den meisten Fällen wird der Funktionsname wie unten vorgegeben.
# Danach folgen im Normalfall einige Testbeispiele mit der gewünschten Ausgabe.
# Falls eine Aufgabe unklar ist (bitte im Forum melden), können die oft helfen.
from fileinput import filename


# A4 ----
# Die Funktion `zahl_lesen` soll einen Dateinamen als Eingabe annehmen und
# - den Inhalt der angegebenen Datei lesen (vgl. Google, Refcard, Lektion 1.2),
# - ihn zu einer Dezimalzahl konvertieren und anzeigen (print), formtiert als
# - "Die Zahl in <dateiname> ist <zahl>". Siehe die Beispiele unten.
# Hinweis: erwünscht ist eine "gedruckte" Ausgabe (print), keine zurückgegebene (return).
import decimal
def zahl_lesen(fn):
    with open(fn, "r") as f:
        line = f.readline().strip()
        decimal_number = decimal.Decimal(line)
        if decimal_number == decimal_number.to_integral():
            print("Die Zahl in", fn, "ist", f"{decimal_number:.1f}")
        else:
            print("Die Zahl in", fn, "ist", f"{decimal_number}")

zahl_lesen("sipl14_zone1.txt") # "Die Zahl in sipl14_zone1.txt ist 42.0"
zahl_lesen("sipl14_zone2.txt") # "Die Zahl in sipl14_zone2.txt ist 99.6"


# Du bist jetzt mit den Aufgaben für diese Lektion fertig.
# Es gibt im nächsten Skript noch eine Bonus-Aufgabe.
# Löse die nur, wenn du Zeit hast und noch etwas mehr lernen möchtest.
# Ansonsten schon mal viel Erfolg bei der nächsten Lektion!

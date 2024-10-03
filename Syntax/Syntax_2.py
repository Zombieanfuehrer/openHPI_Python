# Hinweis: nutze die Tastenkürzel ALT + R und ALT + S für Ausführen / Bewerten.

# A4 ----
# Multipliziere die Zahlen 42 und 7 und subtrahiere danach 15 vom Produkt.
# Speichere das Endergebnis im Objekt 'berechnung'.

berechnung = (42 * 7) -15

# A5 ----
# Dividiere 0,3 durch 4 und multipliziere das mit der Quadratwurzel von 313600.
# Weise das Resultat dem Objekt 'ergebnis_wurzel' zu.
import math
buff_ergebnis_wurzel = (.3 / 4) * (math.sqrt(313600))

# Ab jetzt ist normalerweise der geünschte Objektname vorgegeben:
ergebnis_wurzel = buff_ergebnis_wurzel # ersetze einfach die 0 mit dem Ergebnis
# Meistens habe ich auch einen print Aufruf eingetragen.
# Der ist nur für dich und für die Bewertung irrelevant.
print("ew:", ergebnis_wurzel)

# A6 ----
# Berechne den Sinus von pi/3. Speichere das Ergebnis als 'sinus_pi_drittel'.
# Sowohl die Sinus-Funktion als auch das Pi-Objekt sind im math Modul verfügbar.
sinus_pi_drittel = math.sin(math.pi / 3)
print("spd:", sinus_pi_drittel)

# Weiter geht's im nächsten Skript :)

# A1 ----
# Berechne den arithmetischen Mittelwert der folgenden Werte
# mit der mean Funktion aus dem Modul statistics.
import statistics
zahlen = [19, 59, 78, 82, 68, 35, 72, 24, 85, 62, 25, 88, 80, 87, 23, 22]
mittelwert = statistics.mean(zahlen)
print("mw:", mittelwert) # 56.8125


# A2 ----
# Importiere aus der gegebenen Datei sipl15_tracker.py 
# die Funktion 'initialisieren' und die Zeichenkette 'version'.
# Generiere mit den beiden Objekten dann eine Beschreibung des Trackers.
import sipl15_tracker
fitness_tracker_beschreibung = sipl15_tracker.initialisieren(sipl15_tracker.version)
print("ftb:", fitness_tracker_beschreibung) # FitnessTrackerB2500, Version 3.6.2


# A3 ----
# Verwende das 'random'-Modul, um eine Dezimalzahl (Kommazahl) zu generieren,
# die zwischen 1 (inklusive) und 10 (exklusive) liegt.
# Hinweis: random.random() liegt zwischen 0 und 1, also. 0.0 <= random() < 1.0.
import random

def zahl_1_bis_10():
    rnd_value = random.random()
    return rnd_value + float(random.randrange(1,10))
print("n1-10:", zahl_1_bis_10())

# Im nächsten Skript gibt es noch Bonus-Aufgaben, falls du Zeit und Interesse hast.
# Ansonsten schon mal viel Erfolg bei der nächsten Lektion!

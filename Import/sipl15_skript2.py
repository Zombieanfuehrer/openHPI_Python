# Bonusaufgaben - nur lösen, wenn du Zeit hast, tiefer ins Thema einzusteigen :)

# A4 ----
# Wer einen Modul- oder Dateinamen als Zeichenkette verwenden möchte, 
# braucht importlib.import_module:
import importlib
import sys

module = importlib.import_module("math", package=None)
print("math funktionen:", dir(module)[10:17])

# `ist_genom_definiert` soll einen "Dateinamen.py" als Input annehmen.
# Achtung: auch import_module erwartet den Dateinamen ohne Endung.
# Schaue gerne online nach, wie du eine Dateiendung aus dem Namen los wirst.
# Die Funktion soll ausgeben, ob ein "genom" Objekt in der Datei definiert wird.
import importlib.util
import os
import sys

def ist_genom_definiert(fn):
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = os.path.join(script_dir, fn)
    module_name = os.path.splitext(fn)[0]

    if not os.path.isfile(file_path):
        print(f"Datei {fn} nicht gefunden")
        return 0

    specs = importlib.util.spec_from_file_location(module_name, file_path)
    if specs is None:
        print(f"Fehler beim Laden der Spezifikation für {fn}")
        return 0

    module_ = importlib.util.module_from_spec(specs)
    sys.modules[module_name] = module_
    specs.loader.exec_module(module_)

    if hasattr(module_, 'genom'):
        print("genom gefunden")
        return True
    else:
        print("genom nicht gefunden")
        return False


print("igd1: ", ist_genom_definiert("sipl15_z_hat_g.py"))  # True
print("igd2: ", ist_genom_definiert("sipl15_z_kein_g.py"))  # False


# A5 ----
# `read_count` soll Worte einer Datei einlesen (Leerzeichengetrennt) und zählen.
# Hinweis: die Trennung mit split machen, nicht mit splitlines, siehe Lektion 1.6.
# Die Ausgabe soll ein Tupel für jedes Wort sein, sortiert nach der Häufigkeit.
# In den Folien dieser Lektion ist hierfür eine hilfreiche Funktion empfohlen :)
import collections
def read_count(fn):
    with open(fn, "r") as f:
        list_ = f.read().split()
        list_cnt = collections.Counter(list_).most_common()
    return list_cnt
print("rc1:", read_count("sipl15_z_words.txt")) # [('the', 4), ('text.', 2), ('This', 1), ...
print("rc2:", read_count("sipl15_z_kein_g.py")[:5]) # [('kein', 3), ('genom', 2), ...

# Spätestens jetzt viel Erfolg bei der nächsten Lektion :)


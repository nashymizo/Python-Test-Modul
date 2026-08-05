# Ein Programm welches einen Euro-Betrag in die größt möglichen Scheine und Münzen zerlegt.
# Als Ergebnis soll die Anzahl der Geldstücke ausgeben werden.
# Die Unterscheidung zwischen Schein und Münze ist egal
#
# Eingabe: 1123.88
# ```
# Ausgabe:
#     2x 500 €
#     0x 200 €
#     1x 100 €
#     0x 50 €
#     1x 20 €
#     0x 10 €
#     0x 5 €
#     1x 2 €
#     1x 1 €
#     1x 0.5 €
#     1x 0.2 €
#     1x 0.1 €
#     1x 0.05 €
#     1x 0.02 €
#     1x 0.01 €
# ```
#
# 1. Zeichne ein Struktogramm für den Algorithmus (kommt eigentlich nicht mehr vor)
# 2. Zeichne ein Programmablaufplan für den Algorithmus
# 3. Setze das Programm in Python um

print(round(1188 / 500))
stueckelung = [
    500, 200, 100, 50, 20, 10, 5,
    2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
]

def geld_teiler(betrag):
    # auf Cent wegen rundungsfehler
    betrag_cent = betrag * 100

    for item in stueckelung:
        # auf Cent wegen rundungsfehler
        item_cent = item * 100

        # Rechnung
        anzahl_scheine = int(betrag_cent // item_cent)
        rest_cent = betrag_cent % item_cent
        betrag_cent = rest_cent


        print(f"{anzahl_scheine} x {item} €")


geld_teiler(1241.98)







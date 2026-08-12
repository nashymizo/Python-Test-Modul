import telefonbuch_logik

def kontakt_aufnehmen():

    while True:

        name = input("Gib einen Namen ein (Bsp: 'Max Mustermann'):")

        if telefonbuch_logik.pruefe_text(name):
            break

        else:
            print("Ungültige Eingabe! Bitte nur Buchstaben (max. 32 Zeichen).")


    while True:

        nummer = input("Gib einen Nummer ein (Bsp: '0174 / 232322'):")

        if telefonbuch_logik.pruefe_nummer(nummer):
            break

        else:
            print("Ungültige Eingabe! Bitte nur Zahlen eingeben(Bsp: '0174 / 232322')")

    print(f"Erfasst: {name} -> {nummer}")
    neuer_kontakt = {"name": name, "nummer": nummer}
    return neuer_kontakt


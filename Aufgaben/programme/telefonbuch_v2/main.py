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


def hauptprogramm():
    while True:
        print("\n" + "=" * 35)
        print("        📖 HAUPTMENÜ 📖        ")
        print("=" * 35)
        print("  [1] ➕ Eintrag anlegen")
        print("  [2] ❌ Eintrag löschen")
        print("  [3] 📋 Telefonbuch anzeigen")
        print("  [0] 🚪 App beenden")
        print("=" * 35)

        menu_auswahl = input("    Wähle eine Operation:")

        if menu_auswahl == "1":
            neuer_kontakt = kontakt_aufnehmen()
            telefonbuch_logik.kontakt_speichern(neuer_kontakt)
            telefonbuch_logik.kontakte_sortieren()


        elif menu_auswahl == "2":

            name_loeschen = input("Gib einen Name ein, z.B (Max Mustermann): ")

            telefonbuch_logik.kontakte_loeschen(name_loeschen)
            print(f"✅ Der Kontakt '{name_loeschen}' wurde erfolgreich gelöscht!")


        elif menu_auswahl == "3":
            kontakte = telefonbuch_logik.kontakte_laden()
            print("-" * 5 + " TELEFONBUCH " + "-" * 5)


            # ODER json.dumps(..., indent=4)
            for kontakt in kontakte:
                print(f"👤 Name: {kontakt['name']} | 📞 Nummer: {kontakt['nummer']}")

        elif menu_auswahl == "0":
            print("Telefonbuch-App beendet")
            break


    return



if __name__ == "__main__":
    hauptprogramm()
import telefonbuch_logik_1a
import json


def kontakt_aufnehmen():

    while True:

        name = input("Gib einen Namen ein (Bsp: 'Max Mustermann'):")

        if telefonbuch_logik_1a.pruefe_text(name):
            break

        else:
            print("Ungültige Eingabe! Bitte nur Buchstaben (max. 32 Zeichen).")


    while True:

        nummer = input("Gib einen Nummer ein (Bsp: '0174 / 232322'):")

        if telefonbuch_logik_1a.pruefe_nummer(nummer):
            break

        else:
            print("Ungültige Eingabe! Bitte nur Zahlen eingeben(Bsp: '0174 / 232322')")

    print(f"Erfasst: {name} -> {nummer}")
    neuer_kontakt = {"name": name, "nummer": nummer}
    return neuer_kontakt


def kontakt_speichern(neuer_kontakt):

    try:
        with open("kontakte.json", "a", encoding="utf-8") as datei:
            json.dump(neuer_kontakt, datei, ensure_ascii=False)
            datei.write("\n")

        kontakt_text = json.dumps(neuer_kontakt, ensure_ascii=False, indent=4)
        print(f"Neuer Kontakt:\n{kontakt_text}\n erfolgreich gespeichert.")

    except Exception as e:
        print(f"Kontakt: {neuer_kontakt} konnte nicht erfolgreich gespeichert werden. ({e})")



neuer_eintrag = kontakt_aufnehmen()
kontakt_speichern(neuer_eintrag)





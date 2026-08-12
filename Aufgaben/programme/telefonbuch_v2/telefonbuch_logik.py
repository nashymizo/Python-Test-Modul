import re
import json

def pruefe_text(text : str) -> bool:

    pattern = r"^[a-zA-ZäöüÄÖÜß ]{1,32}$"
    return bool(re.match(pattern, text))



def pruefe_nummer(nummer : str) -> bool:

    pattern = r"^\d+ / \d+$"
    return bool(re.match(pattern, nummer))





def kontakt_speichern(neuer_kontakt):

    try:
        with open("kontakte.json", "a", encoding="utf-8") as datei:
            json.dump(neuer_kontakt, datei, ensure_ascii=False)
            datei.write("\n")

        kontakt_text = json.dumps(neuer_kontakt, ensure_ascii=False, indent=4)
        print(f"Neuer Kontakt:\n{kontakt_text}\n erfolgreich gespeichert.")

    except Exception as e:
        print(f"Kontakt: {neuer_kontakt} konnte nicht erfolgreich gespeichert werden. ({e})")


def kontakte_sortieren(dateiname="kontakte.json"):
    try:
        kontakte = []

        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if zeile:
                    kontakt = json.loads(zeile)
                    kontakte.append(kontakt)

        kontakte.sort(key=lambda x: x["name"].lower())

        with open(dateiname, "w", encoding="utf-8") as datei:
            for kontakt in kontakte:
                json.dump(kontakt, datei, ensure_ascii=False)
                datei.write("\n")

        print("Kontakte wurden erfolgreich alphabetisch sortiert!")

    except Exception as e:
        print(f"Fehler beim Sortieren: {e}")


def kontakte_laden():

    kontakte = []

    try:
        with open("kontakte.json", "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if zeile:
                    kontakt = json.loads(zeile)
                    kontakte.append(kontakt)

    except Exception as e:
        print(f"Fehler beim Anzeigen: {e}")

    return kontakte


def kontakte_loeschen(kontakt):

    kontakte = kontakte_laden()

    for person in kontakte:
        if person["name"] == kontakt:
            kontakte.remove(person)
            break

    try:
        with open("kontakte.json", "w", encoding="utf-8") as datei:
            for person in kontakte:
                json.dump(person, datei, ensure_ascii=False)
                datei.write("\n")

    except Exception as e:
        print(f"Fehler beim Löschen: {e}")

    return kontakte

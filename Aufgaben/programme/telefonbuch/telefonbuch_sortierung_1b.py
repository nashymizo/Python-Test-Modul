import json


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


if __name__ == "__main__":
    kontakte_sortieren()
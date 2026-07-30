"""

    Ein Lebenslaufgenerator

    # Eingabe
    - Daten im JSON Format ablegen
    - (evtl. eine Word Vorlage mit eigenen Stilen)

    # Daten in Word oder PDF aufbereiten
    - Daten (Text)
    - Kopfzeile & Fußzeile (Grafik)
    - Bild/Foto

    # Anforderungen
    - Persönliche Daten
    - Schulischer Werdegang
    - Beruflicher Werdegang (Ausbildung)
    - Kenntnisse und Fähigkeiten

    - Die Daten in eine extra Datei (JSON oder Python)

"""
import json
from docx import Document

meineDaten = {
    "personal": {
        "firstname": "Nico",
        "lastname": "Kehl",
        "birthday": "06.07.1992",
        "address": {
            "postal code": "66271",
            "city": "Kleinblittersdorf",
            "street": "Saargemünder Str. 135"
        },
        "Kontakt": {
            "email": "Nico.Kehl92@web.de",
            "phone": "0174/1706642"
        }
    },

    "education": [
        {
            "school": "Grundschule",
            "degree": "Abschluss",
            "start_date": "1998",
            "end_date": "2002"
        },
        {
            "school": "Weiterführende Schule",
            "degree": "Abschluss",
            "start_date": "2002",
            "end_date": "2006"
        }
    ],

    "experience": [
        {
            "company": "",
            "position": "",
            "start_date": "",
            "end_date": ""
        },
        {
            "company": "",
            "position": "",
            "start_date": "",
            "end_date": ""
        }
    ],

    "skills" : [
        "Python",
        "Git",
        "SQL"
    ]
}



def daten_speichern(liste):
    try:
        with open ("Lebenslauf_Daten.json", "w", encoding="utf-8") as file:
            json.dump(liste, file, ensure_ascii=False, indent=4)
            print("Daten wurden erfolgreich gespeichert werden.")

    except Exception as e:
        print(f"Daten konnten nicht gespeichert werden, Fehlermeldung: {e}")


def daten_laden(dateipfad="Lebenslauf_Daten.json"):
    try:
        with open("Lebenslauf_Daten.json", "r", encoding="utf-8") as file:
            daten = json.load(file)
            return daten

    except Exception as e:
        print(f"Datei Upload fehlgeschlagen, Fehlermeldung: {e}")


def kopfzeile_erstellen(doc, personal_daten):
    name = f"{personal_daten['firstname']} {personal_daten['lastname']}"
    doc.add_heading(name, level=1)

    address = personal_daten['address']
    address_text = f"{address['postal code']}, {address['city']}, {address['street']}"

    kontakt = personal_daten['Kontakt']

    info_text = (
        f"Geburtsdatum: {personal_daten['birthday']}\n"
        f"Adresse: {address_text}\n"
        f"Email Adresse: {kontakt['email']} I Tel: {kontakt['phone']}"
    )
    doc.add_paragraph(info_text)


meine_daten = daten_laden()
mein_doc = Document()
kopfzeile_erstellen(mein_doc, meine_daten["personal"])
mein_doc.save("Lebenslauf.docx")

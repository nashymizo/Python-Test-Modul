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

meinedaten = {
    "personal": {
        "firstname": "Nico",
        "lastname": "Kehl",
        "birthday": "06.07.1992",  # Komma nicht vergessen
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
        }
    ]
}




print(meinedaten)
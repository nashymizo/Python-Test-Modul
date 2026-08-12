import json
import random
import winsound
from pathlib import Path


# __file__ enthält den Speicherort dieser Python-Datei.
# Mit .resolve().parent erhalten wir den Ordner, in dem die Datei liegt.
PROGRAMM_ORDNER = Path(__file__).resolve().parent

# Alle weiteren Dateien werden in diesem Ordner gesucht oder gespeichert.
HIGHSCORE_DATEI = PROGRAMM_ORDNER / "highscore.json"
GEWINN_SOUND = PROGRAMM_ORDNER / "applause.wav"
VERLIERER_SOUND = PROGRAMM_ORDNER / "lose.wav"


def highscore_laden():
    """Lädt den bisher gespeicherten Highscore.

    Returns:
        int | None: Bisher beste Anzahl an Versuchen oder None,
        wenn noch kein Highscore vorhanden ist.
    """
    if not HIGHSCORE_DATEI.exists():
        return None

    try:
        with HIGHSCORE_DATEI.open("r", encoding="utf-8") as datei:
            daten = json.load(datei)

        return daten.get("beste_versuche")

    except (OSError, json.JSONDecodeError):
        print("Der Highscore konnte nicht gelesen werden.")
        return None


def highscore_speichern(versuche):
    """Speichert einen neuen Highscore.

    Args:
        versuche (int): Anzahl der benötigten Versuche.
    """
    daten = {
        "beste_versuche": versuche
    }

    try:
        with HIGHSCORE_DATEI.open("w", encoding="utf-8") as datei:
            json.dump(
                daten,
                datei,
                ensure_ascii=False,
                indent=4
            )

    except OSError:
        print("Der Highscore konnte nicht gespeichert werden.")


def sound_abspielen(sounddatei):
    """Spielt eine WAV-Datei unter Windows ab.

    Args:
        sounddatei (Path): Vollständiger Pfad zur WAV-Datei.
    """
    if not sounddatei.exists():
        print(f"Die Sounddatei wurde nicht gefunden: {sounddatei}")
        return

    try:
        winsound.PlaySound(
            str(sounddatei),
            winsound.SND_FILENAME
        )

    except RuntimeError:
        print(f"Die Sounddatei konnte nicht abgespielt werden: {sounddatei}")


def ratespiel(untergrenze=1, obergrenze=20, maximale_versuche=5):
    """Startet das Zahlen-Ratespiel.

    Args:
        untergrenze (int): Kleinste mögliche Zufallszahl.
        obergrenze (int): Größte mögliche Zufallszahl.
        maximale_versuche (int): Maximale Anzahl der Rateversuche.

    Returns:
        bool: True bei einem Sieg, sonst False.
    """
    if untergrenze >= obergrenze:
        raise ValueError(
            "Die Untergrenze muss kleiner als die Obergrenze sein."
        )

    if maximale_versuche <= 0:
        raise ValueError(
            "Die Anzahl der Versuche muss größer als 0 sein."
        )

    gesuchte_zahl = random.randint(
        untergrenze,
        obergrenze
    )

    highscore = highscore_laden()

    print("=" * 45)
    print("              ZAHLEN-RATESPIEL")
    print("=" * 45)
    print(
        f"Ich habe eine Zahl zwischen {untergrenze} "
        f"und {obergrenze} ausgewählt."
    )
    print(f"Du hast maximal {maximale_versuche} Versuche.")

    if highscore is None:
        print("Es wurde noch kein Highscore gespeichert.")
    else:
        print(f"Aktueller Highscore: {highscore} Versuch(e)")

    print("-" * 45)

    for versuch in range(1, maximale_versuche + 1):
        while True:
            try:
                tipp = int(
                    input(
                        f"Versuch {versuch}/{maximale_versuche} – "
                        "dein Tipp: "
                    )
                )

                if not untergrenze <= tipp <= obergrenze:
                    print(
                        f"Bitte eine Zahl zwischen {untergrenze} "
                        f"und {obergrenze} eingeben."
                    )
                    continue

                break

            except ValueError:
                print(
                    "Ungültige Eingabe. "
                    "Bitte eine ganze Zahl eingeben."
                )

        if tipp == gesuchte_zahl:
            print("\nRichtig geraten! Glückwunsch!")
            print(f"Du hast {versuch} Versuch(e) benötigt.")

            if highscore is None or versuch < highscore:
                highscore_speichern(versuch)
                print("Neuer Highscore!")

            sound_abspielen(GEWINN_SOUND)
            return True

        if tipp < gesuchte_zahl:
            print("Dein Tipp ist zu klein.\n")
        else:
            print("Dein Tipp ist zu groß.\n")

    print("-" * 45)
    print("Leider verloren.")
    print(f"Die gesuchte Zahl war: {gesuchte_zahl}")

    sound_abspielen(VERLIERER_SOUND)
    return False


if __name__ == "__main__":
    ratespiel()
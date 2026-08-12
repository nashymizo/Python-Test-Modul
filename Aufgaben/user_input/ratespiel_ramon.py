"""
Ein Ratespiel

Es soll eine Zufallszahl generiert werden, die erraten werden soll.

- Es sollen maximal 5 Versuche möglich sein eine Zahl zu raten
- Nach dem 5. Versuch hat man verloren und das Programm wird beendet
- Wenn man verloren hat soll die gesuchte Zahl angezeigt werden
- Vor dem raten soll eine Hilfe angezeigt werden, die anzeigt in welchen Bereich die Zufallszahl liegt
- Der Bereich der Zufallszahl soll einstellbar sein und erstmal zwischen 1 - 20

Erweiterung
- sound abspielen
- highscore speichern
"""

import os
import random
import winsound

MIN_BEREICH = 1
MAX_BEREICH = 20
MAX_VERSUCHE = 5
HIGHSCORE_DATEI = "highscore.txt"


def spiele_sound(typ="applause.wav"):
    """
    Spielt einen Sound ab, je nach Typ

    :param typ: typ des Sounds (applause.wav, lose.wav)
    :return: void
    """
    try:
        if typ == "win":
            winsound.PlaySound(
                "applause.wav",
                winsound.SND_FILENAME
            )

        elif typ == "lose":
            winsound.PlaySound(
                "lose.wav",
                winsound.SND_FILENAME
            )

    except Exception:
        pass


def lade_highscore():
    """Lädt den Highscore aus der Datei, falls vorhanden."""
    if os.path.exists(HIGHSCORE_DATEI):
        with open(HIGHSCORE_DATEI, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return None
    return None


def speichere_highscore(versuche):
    """Speichert den Highscore, falls er besser ist als der bisherige."""
    bester = lade_highscore()
    if bester is None or versuche < bester:
        with open(HIGHSCORE_DATEI, "w") as f:
            f.write(str(versuche))
        print(f"NEUER HIGHSCORE: {versuche} Versuch(e)!")
    elif bester is not None:
        print(f"Bisheriger Highscore liegt bei {bester} Versuchen.")


geheime_zahl = random.randint(MIN_BEREICH, MAX_BEREICH)
gewonnen = False


print("=" * 45)
print("          ### WILLKOMMEN BEIM RATESPIEL ###          ")
print("=" * 45)
print(
    f"HILFE: Die gesuchte Zahl liegt zwischen {MIN_BEREICH} und {MAX_BEREICH}!"
)
print(f"Du hast maximal {MAX_VERSUCHE} Versuche.")
print("-" * 45)


for versuch in range(1, MAX_VERSUCHE + 1):
    tipp = int(
        input(f"Versuch {versuch}/{MAX_VERSUCHE} - Gib deinen Tipp ein: ")
    )

    if tipp == geheime_zahl:
        print(
            f"\r\nRichtig! Du hast die Zahl in {versuch} Versuch(en) erraten!"
        )
        spiele_sound("win")
        speichere_highscore(versuch)
        gewonnen = True
        break
    elif tipp < geheime_zahl:
        print("Die gesuchte Zahl ist GRÖSSER.")

    else:
        print("Die gesuchte Zahl ist KLEINER.")

    print("-" * 30)


if not gewonnen:
    print("\r\nLeider verloren! Du hast alle Versuche verbraucht.")
    print(f"Die gesuchte Zahl war: {geheime_zahl}")
    spiele_sound("lose")

print("=" * 45)
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
from random import randint
import winsound


def user_input(a, b):

    while True:
        try:
            zahl_user = int(input(f"Bitte eine Zahl zwischen {a} und {b} eingeben: "))

            if a <= zahl_user <= b:
                return zahl_user
            else:
                print(f"Die Zahl muss zwischen {a} und {b} liegen!")

        except ValueError:
            print("Bitte gib eine Ganzzahl ein.")


def random_number (min_wert=1, max_wert=20):
    random_zahl = randint(min_wert, max_wert)
    return random_zahl


def ratespiel():
    min_bereich = 1
    max_bereich = 20
    zahl_zufall = random_number(min_bereich, max_bereich)
    print(f"Die gesuchte Zahl liegt zwischen [{min_bereich} und {max_bereich}]. Viel Erfolg!")

    for i in range(5):
        user_zahl = user_input(min_bereich, max_bereich)

        if user_zahl < zahl_zufall:
            print(f"Die Zahl ist zu klein")
            winsound.PlaySound("nope.wav", winsound.SND_FILENAME)

        elif user_zahl > zahl_zufall:
            print("Die Zahl ist zu groß")
            winsound.PlaySound("nope.wav", winsound.SND_FILENAME)

        else:
            anzahl_versuche = i + 1
            print("Du hast Gewonnen!")
            print(f"Du hast {anzahl_versuche} Versuch(e) gebraucht!")
            winsound.PlaySound("applause.wav", winsound.SND_FILENAME)

            with open("Highscore.txt", "a") as file:
                file.write(f"Versuche: {anzahl_versuche}\n")

            break


    else:
        print(f"Die gesuchte Zahl lautet: {zahl_zufall}")
        winsound.PlaySound("lose.wav", winsound.SND_FILENAME)
    return

ratespiel()

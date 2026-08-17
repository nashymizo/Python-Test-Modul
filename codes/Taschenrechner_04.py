import os

def main():
    while True:
        # Bildschirm aufräumen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("======================================")
        print("   DEIN PROFIS-RECHNER & TRAINER V3   ")
        print("======================================")
        print("1: Addition (+)")
        print("2: Subtraktion (-)")
        print("3: Multiplikation (*)")
        print("4: Division (/)")
        print("5: Beenden")
        print("--------------------------------------")
        
        wahl = input("Deine Wahl (1-5): ")

        if wahl == "5":
            print("Programm wird beendet. Bis bald!")
            break
        
        if wahl not in ["1", "2", "3", "4"]:
            print("\n[!] FEHLER: Ungültige Auswahl!")
            input("Drücke Enter, um es erneut zu versuchen...")
            continue

        try:
            # Zahlen abfragen
            print("")
            zahl1 = float(input("Erste Zahl: "))
            zahl2 = float(input("Zweite Zahl: "))
            print("--------------------------------------")

            # Rechenlogik
            if wahl == "1":
                ergebnis = zahl1 + zahl2
                symbol = "+"
            elif wahl == "2":
                ergebnis = zahl1 - zahl2
                symbol = "-"
            elif wahl == "3":
                ergebnis = zahl1 * zahl2
                symbol = "*"
            elif wahl == "4":
                if zahl2 == 0:
                    print("FEHLER: Division durch Null ist nicht erlaubt!")
                    input("\nDrücke Enter für das Menü...")
                    continue
                ergebnis = zahl1 / zahl2
                symbol = "/"

            # Schicke Ausgabe mit f-String
            print(f"ERGEBNIS: {zahl1} {symbol} {zahl2} = {ergebnis}")
            
            # Pause für den Benutzer
            print("--------------------------------------")
            input("Rechnung fertig. Drücke Enter für das Menü...")

        except ValueError:
            print("\n[!] FEHLER: Bitte gib nur gültige Zahlen ein!")
            input("Drücke Enter, um zum Menü zurückzukehren...")

if __name__ == "__main__":
    main()
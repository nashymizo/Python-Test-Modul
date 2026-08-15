import os
import random

def main():
    while True:
        # Hauptmenü
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================================")
        print("==== HARRY POTTER UND DIE MAGISCHEN ZAHLEN ====")
        print("===============================================")
        print("Bitte wähle eine Grundrechenart:")
        print(" (1) - für ADDIEREN (+) ")
        print(" (2) - für SUBTRAHIEREN (-) ")
        print(" (3) - MAGISCHE ZAHLEN ENTZAUBERN - BEENDEN ")

        wahl = input("\nDeine Wahl (1-3): ")

        if wahl == "3":
            print("Die Magie schwindet... Bis bald!")
            break

        if wahl in ["1", "2"]:
            # --- INNERE SCHLEIFE FÜR DIE AUFGABEN ---
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                # Zahlen würfeln
                z1 = random.randint(1, 100)
                z2 = random.randint(1, 100)

                if wahl == "1":
                    operator = "+"
                    korrekt = z1 + z2
                else:
                    operator = "-"
                    # Sicherstellen, dass kein negatives Ergebnis kommt
                    if z2 > z1: z1, z2 = z2, z1
                    korrekt = z1 - z2

                print(f"--- Modus: {'Addition' if wahl == '1' else 'Subtraktion'} ---")
                print(f"\nDie magische Rechnung lautet: {z1} {operator} {z2}")
                
                try:
                    eingabe = input("Das magische Ergebnis lautet: ")
                    
                    # Prüfen, ob der Nutzer zurück ins Menü will
                    if eingabe.lower() == 'm':
                        break
                    
                    tipp = int(eingabe)
                    
                    if tipp == korrekt:
                        print("✨ Richtig! Ein wahrer Zauberer! ✨")
                    else:
                        print(f"💥 Oh weh! Das richtige Ergebnis wäre {korrekt} gewesen. 💥")
                
                except ValueError:
                    print("💥 Muggel-Alarm! Bitte gib nur echte Zahlen ein! 💥")

                # Hier ist der Trick: Einfach Enter drücken lässt die Schleife weiterlaufen
                weiter = input("\n[Enter] für nächste Aufgabe | [m] für Menü: ")
                if weiter.lower() == 'm':
                    break

# DER ANLASSER
if __name__ == "__main__":
    main()
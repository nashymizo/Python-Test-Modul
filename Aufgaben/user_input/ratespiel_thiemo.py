import random
import json
import os
# import pygame # Deaktiviert für Sandbox-Umgebung

# Initialisiere Pygame Mixer für Sound (Deaktiviert für Sandbox-Umgebung)
# pygame.mixer.init()

HIGHSCORE_FILE = 'highscore.json'

def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, 'r') as f:
            return json.load(f)
    return []

def save_highscores(highscores):
    with open(HIGHSCORE_FILE, 'w') as f:
        json.dump(highscores, f)

# def play_sound(sound_file): # Deaktiviert für Sandbox-Umgebung
#     try:
#         pygame.mixer.music.load(sound_file)
#         pygame.mixer.music.play()
#     except pygame.error as e:
#         print(f"Fehler beim Abspielen des Sounds: {e}")

def play_game(min_num=1, max_num=20, max_attempts=5):
    secret_number = random.randint(min_num, max_num)
    print(f"Willkommen zum Ratespiel! Ich habe mir eine Zahl zwischen {min_num} und {max_num} ausgedacht.")
    print(f"Du hast maximal {max_attempts} Versuche, um die Zahl zu erraten.")

    highscores = load_highscores()
    print("\n--- Highscores ---")
    if highscores:
        for score in sorted(highscores, key=lambda x: x['attempts']):
            print(f"Name: {score['name']}, Versuche: {score['attempts']}")
    else:
        print("Noch keine Highscores vorhanden.")
    print("------------------\n")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Versuch {attempt}: Rate die Zahl: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")
            continue

        if guess < secret_number:
            print("Meine Zahl ist größer.")
            # play_sound('low.wav') # Placeholder for sound
        elif guess > secret_number:
            print("Meine Zahl ist kleiner.")
            # play_sound('high.wav') # Placeholder for sound
        else:
            print(f"Glückwunsch! Du hast die Zahl {secret_number} in {attempt} Versuchen erraten!")
            # play_sound('win.wav') # Placeholder for sound
            player_name = input("Gib deinen Namen für den Highscore ein: ")
            highscores.append({'name': player_name, 'attempts': attempt})
            save_highscores(highscores)
            return True

    print(f"Leider hast du die Zahl nicht erraten. Die gesuchte Zahl war {secret_number}.")
    # play_sound('lose.wav') # Placeholder for sound
    return False

if __name__ == "__main__":
    play_game()

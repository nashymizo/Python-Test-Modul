"""

Passwort analysieren

Prüfe, ob ein Passwort

mindestens 8 Zeichen lang ist,
mindestens einen Großbuchstaben enthält,
mindestens einen Kleinbuchstaben enthält,
mindestens eine Zahl enthält.

"""

passwort = "MeinGeheimes&§123"
#
def password_analysis(password):
    up_letter = False
    low_letter = False
    min_letter = False
    zahl_letter = False


    for zeichen in password:
        if zeichen.isupper():
            up_letter = True

        if zeichen.islower():
            low_letter = True

        if zeichen.isdigit():
            zahl_letter = True

        if len(password) > 8:
            min_letter = True


    if up_letter and low_letter and min_letter and zahl_letter:
        print("Du hast alle Anforderungen erfüllt.")
        print("Status:")
        return True
    else:
        print("Du hast nicht alle Anforderungen erfüllt.")
        print("Status:")
        return False


print(password_analysis(passwort))


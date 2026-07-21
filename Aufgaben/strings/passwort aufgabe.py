"""

Passwort analysieren

Prüfe, ob ein Passwort

mindestens 8 Zeichen lang ist,
mindestens einen Großbuchstaben enthält,
mindestens einen Kleinbuchstaben enthält,
mindestens eine Zahl enthält.

"""

# passwort = "MeinGeheimes&§123"



def pruefe_passwort(passwort):
    if len(passwort) <= 7:
        return 0

    punkte = 1

    hat_ziffer = False
    hat_gross = False
    hat_klein = False
    hat_sonder = False

    for zeichen in passwort:
        if zeichen.isdigit():
            hat_ziffer = True

        if zeichen.isupper():
            hat_gross = True

        if zeichen.islower():
            hat_klein = True

        if not zeichen.isalnum():
            hat_sonder = True

    if hat_ziffer == True:
        punkte = punkte + 1

    if hat_gross and hat_klein == True:
        punkte += 1

    if hat_sonder == True:
        punkte += 1

    print("""# - Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
    # - Enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
    # - Enthält zumindest eine Ziffer: +1 Punkt
    # - Enthält zumindest ein Sonderzeichen: +1 Punkt""")
    print(f"Dein {passwort} hat eine Bewertung von '{punkte}' erhalten")

    return punkte

print(pruefe_passwort("asdadas42&dasd"))
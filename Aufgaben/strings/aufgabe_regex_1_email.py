import re

# Es dürfen nur Emails mit der Endung meinefirma.de matchen


emails = [
    "test@meinefirma.de",  # ok
    "TEST@meinefirma.de",  # ok
    "test123@meinefirma.de",  # ok
    "v.nachname@meinefirma.de", # ok
    "v-nachname@meinefirma.de", # ok
    "v_nachname@meinefirma.de", # ok
    "nicht gut@meinefirma.de", # falsch
    "nicht @meinefirma.de",  # falsch
    "ok@meinefirma.de " , # falsch
    " ok@meinefirma.de " , # falsch
    "thomas:eses@meinefirma.de " , # falsch
]

import re


for email in emails:
    ergebnis = re.findall(r"^[a-zA-Z0-9._-]+@meinefirma\.de$", email)

    if ergebnis:
        print(f"✅ Erfüllt:       '{email}'")
    else:
        print(f"❌ Nicht erfüllt: '{email}'")



# muster = r"^[a-zA-Z0-9._-]+@meinefirma\.de$
# ^ = ab hier beginnt der text
# a-z = kleinbuchst
# A-Z = GROß
# 0-9 = zahlen
# ._- = zulässige sonderzeichen
# + = rechts muss was folgen
# meinefirma = muss genauso da stehen
# \. = punkt
# de = muss genauso da stehen
# $ = hier endet der Text
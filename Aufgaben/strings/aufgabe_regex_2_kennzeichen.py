
# Erkennung eines deutschen KFZ Kennzeichens
import re

kennzeichen = [
    "WÜ AB 12",  # falsch
    "B M 1",  # true
    "B MW 1",  # true
    "WES A 1000",  # true
    "WES A 1000E",  # true
    "DU ME 123" ,  # true
    "DU ME 123H",   # true
    " DU ME 123H ",   # falsch
    " DU ME 12-3H ",  # falsch
    " ABC A 123"      # falsch
]


import re
for item in kennzeichen:

    ergebnis =re.findall(r"^[A-Z]{1,3} [A-Z]{1,2} [A-Z0-9]{1,5}$", item)


    if  ergebnis:
        print(f"{item} ist ein kennzeichen")

    else:
        print(f"{item} ist kein kennzeichen")




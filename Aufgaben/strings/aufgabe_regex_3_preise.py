# Betrag in € (optional 2 Kommastellen), mit 1.000er-Trennzeichen 
# Bsp: 10.000,00 €  => true
# Bsp: 10.000 €  => true
# Bsp: 10000 €  => true
# Bsp: 10000,00 €  => true
# Bsp: 10.000 => false
# Bsp: 10000 => false
import re 

zahlen = [
    "10.000,00 €", # ok
    "10.000 €", # ok
    "10000 €", # ok
    "10000,00 €", # ok
    "10.000", # None
    "10000", # None

    "0,90 €"  # Ok
    " 1000", # None
    "222 2", # None
    "0900",  # None
]

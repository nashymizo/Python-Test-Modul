"""
Programmieraufgabe (Rabatte & Zusatzkosten beim Online-Einkauf)

	1. Der Warenwert (in €) ist gegeben.

	2. Vom Warenwert werden folgende Rabatte und Zuschläge berechnet:
	Mengenrabatt: 10 %
	Sonderrabatt: 5 %
	Versandkosten: 4,90 € (fester Betrag)
	Verpackungskosten: 2 %

	3. Auf den neuen Betrag nach Abzügen und Zuschlägen kommt zusätzlich die Mehrwertsteuer von 19 % drauf.

	Ausgabe:

	Das Programm soll am Ende übersichtlich ausgeben:
	- den eingegebenen Warenwert,
	- den abgezogenen Mengenrabatt,
	- den abgezogenen Sonderrabatt,
	- die hinzugerechneten Versandkosten,
	- die hinzugerechneten Verpackungskosten,
	- die berechnete Mehrwertsteuer,
	- den Endpreis nach allen Abzügen und Zuschlägen.
	
"""

def Kassenbon(warenwert):

    warenwert = float(warenwert)

    mengenrabatt = warenwert * 0.1
    sonderrabatt = warenwert * 0.05
    versandkosten = 4.90
    verpackungskosten = warenwert * 0.02
    mehrwertsteuer = 0.19

    zwischensumme = warenwert - mengenrabatt - sonderrabatt + versandkosten + verpackungskosten

    berechnete_mehrwertsteuer = zwischensumme * mehrwertsteuer

    endsumme = zwischensumme + berechnete_mehrwertsteuer

    return warenwert, mengenrabatt, sonderrabatt, versandkosten, verpackungskosten, berechnete_mehrwertsteuer, endsumme


# MÖGLICHKEIT OHNE TUPEL
# 1. Wir rufen die Funktion auf und fangen ALLE 7 Rückgabewerte der Reihe nach auf:
# wert, m_rabatt, s_rabatt, v_kosten, verp_kosten, steuer, summe = Kassenbon(200)

dein_einkauf = int(input("Wie hoch ist dein Warenwert?"))

mein_bon = Kassenbon(dein_einkauf)

print(f"----- IHR EINKAUF -----")
print(f"{'Einkauf:':<26} {mein_bon[0]:.2f} €")
print(f"{'Mengenrabatt:':<26} -{mein_bon[1]:.2f} €")
print(f"{'Sonderrabatt:':<26} -{mein_bon[2]:.2f} €")
print(f"{'Versandkosten:':<26} +{mein_bon[3]:.2f} €")
print(f"{'Verpackungskosten:':<26} +{mein_bon[4]:.2f} €")
print(f"{'Mehrwertsteuer:':<26} +{mein_bon[5]:.2f} €")
print(f"{'ENDBETRAG:':<24} = {mein_bon[6]:.2f} €")
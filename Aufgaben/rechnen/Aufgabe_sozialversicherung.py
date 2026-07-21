######################################################################
# Ein Programm zur Berechnung der Sozialversicherung
#	
#	Gegeben sind folgende Werte
#	- Bruttolohn in Euro
#	- Arbeitslosenversicherung in %	
#	- Rentenversicherung in %	
#	- Krankenversicherung in %	
#	- Pflegeversicherung in %	
#	- (Version 2: Die Angabe der Anzahl der Kinder)
#
#	Als Ergebnis sollen folgende Werte angezeigt werden:
#	- Bruttolohn in Euro 
#	- Betrag der für die Arbeitslosenversicherung abgezogen wird	
#	- Betrag der für die Rentenversicherung abgezogen wird	
#	- Betrag der für die Krankenversicherung abgezogen wird	
#	- Betrag der für die Pflegeversicherung abgezogen wird	
#	- Das zu versteuernde Einkommen
#
#	Die Beitragsbemessungsgrenze soll ert mal nicht betrachtet werden 
#   Dies kann in einer weiteren Verion eingebaut werden 
#
#	Die Kirchensteuer soll nicht betrachtet werden.
#	Dies kann in einer weiteren Verion eingebaut werden 
#
######################################################################


def sozialversicherung(brutto, kinder):

    satz_rv = 0.093
    satz_av = 0.013
    satz_kv = 0.073
    satz_pv1 = 0.017
    satz_pv0 = 0.023
    satz_pv25= 0.017 - ((kinder - 1) *  0.0025)


    abzug_rv = brutto * satz_rv
    abzug_av = brutto * satz_av
    abzug_kv = brutto * satz_kv

    if kinder == 0:
        abzug_pv = brutto * satz_pv0
    elif kinder == 1:
        abzug_pv = brutto * satz_pv1
    else:
        abzug_pv = brutto * satz_pv25

    netto = brutto - (abzug_rv + abzug_av + abzug_kv + abzug_pv)

    return netto, abzug_rv, abzug_av, abzug_kv, abzug_pv




bruttolohn = int(input("Bitte gib deinen Bruttolohn ein:"))
kinder = int(input("Wie oft gings über die 1 Minute Marke ?"))

netto, abzug_rv, abzug_av, abzug_kv, abzug_pv = sozialversicherung(bruttolohn,kinder)

print((5*"-")+"Der eine Nettorechner"+(5*"-"))
print(f"Dein Monatsgehalt lautet: {bruttolohn}€")
print("Die folgenden Beträge werden abgezogen:")
print(f"{'Rentenversicherung:':<26} {abzug_rv:>10.2f}€")
print(f"{'Arbeitslosenversicherung:':<26} {abzug_av:>10.2f}€")
print(f"{'Krankenversicherung:':<26} {abzug_kv:>10.2f}€")
print(f"{'Pflegeversicherung:':<26} {abzug_pv:>10.2f}€")
print("Dadurch ergibt sich folgender Nettobetrag:")
print(f"{'Netto Monatsgehalt:':<26} {netto:>10.2f}€")
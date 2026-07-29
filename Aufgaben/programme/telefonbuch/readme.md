# Telefonbuch

## Szenario

Ein Unternehmen benötigt ein Tool für die Erfassung von Telefonnummern per Konsole die in einer alten Telefonanlage benutzt wird.

## Aufgabe

### Aufgabe 1a
Schreibe ein kleines Telefonbuch welches Vornamen, Nachnamen und Telefonnummer speichert.
- Der Eintrag soll über die Konsole erfolgen
- Nach dem Eintragen der Daten sollen die Daten in einer Datei im JSON Format gespeichert werden

### Aufgabe 1b
Schreibe ein zweites Programm, welches das Telefonbuch nach Vornamen sortiert anzeigt
- Falls Zeit ist, sogar mit einer kleinen suche

### Aufgabe 2
Für die die erweiterten Programmierer
Ferner soll ein Menü hinzugefügt werden, welches folgende Operationen ermöglicht (die dann zu implementieren sind)

1. Neuen Eintrag hinzufügen
2. Eintrag löschen
3. Telefonbuch anzeigen

## Herausforderung
Validierung der Benutzereingaben durch eigene Funktionen, die testbar sein sollen realisieren.

- Vorname, Nachname
  - Nur Buchstaben erlaubt 
  - nur leerzeichen erlaubt
  - nur deutsche umlaute erlaubt
  - nicht länger als 32 Zeichen je Eintrag
- Telefonnummer
  - Format: 02023 / 123456  
  - Vorwahl / Nummer

## Implementierung

Bitte die Business Funktionalitäten in einer eigen Datei auslagern, damit diese getestet werden können.

## Technologien

- Dateien lesen und schreiben
- json Modul
- user input
- unittest
  - testen der business funktionen
  - testen der Usereingaben Validierung
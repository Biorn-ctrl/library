Dit project is een eenvoudig bibliotheekbeheersysteem geschreven in Python.  
Het gebruikt **SQLite** als database en een CLI-interface om boeken en genres te beheren.

---

## Functionaliteiten

- Boeken toevoegen
- Genres toevoegen
- Zoeken op titel of auteur (hoofdletterongevoelig)
- Lenen en terugbrengen van boeken
- Overzicht in tabelvorm via *tabulate*
- Exporteren naar CSV
- Automatische aanmaak van de database bij eerste opstart


Toevoegen van boeken kan pas nadat er een genre aangemaakt geweest is.


---

##  Configuratiebestand (`config.json`)

Dit bestand vertelt het programma waar de database moet komen.
Bestand wordt in de hoofd library map geplaatst.

Gebruik dit formaat:

json

{
  "database_path": "data/library.db"
}

---


## Project starten
Start altijd vanuit de rootmap van het project:
python -m app.main

Exporteren naar CSV komt het CSV bestand in de hoofd library map terecht.

Voorbeelddatabase wordt meegestuurd, lege database wordt aangemaakt indien database nog niet bestaat. Deze moet in de app\db folder geplaatst worden.

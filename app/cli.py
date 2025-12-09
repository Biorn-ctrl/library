# -*- coding: utf-8 -*-

import csv
from tabulate import tabulate

class CLI:
    def __init__(self, repo):
        self.repo = repo

    # -------------------------------
    # Helpers
    # -------------------------------
    def vraag_int(self, prompt):
        value = input(prompt)
        if not value.isdigit():
            print("❌ Gelieve een getal in te geven.")
            return None
        return int(value)

    def boek_bestaat(self, book_id):
        return any(b.id == book_id for b in self.repo.get_books())

    def genre_bestaat(self, genre_id):
        return any(g.id == genre_id for g in self.repo.get_genres())

    # -------------------------------
    # Menu
    # -------------------------------
    def menu(self):
        while True:
            print("\n=== Bibliotheek Systeem ===")
            print("1. Toon alle boeken")
            print("2. Voeg een boek toe")
            print("3. Voeg een genre toe")
            print("4. Markeer als uitgeleend")
            print("5. Markeer als teruggebracht")
            print("6. Exporteer naar CSV")
            print("7. Zoek op titel")
            print("8. Zoek op auteur")
            print("0. Stoppen")

            keuze = input("Keuze: ").strip()

            match keuze:
                case "1": self.toon_boeken()
                case "2": self.voeg_boek_toe()
                case "3": self.voeg_genre_toe()
                case "4": self.markeer_uitgeleend()
                case "5": self.markeer_terug()
                case "6": self.export_csv()
                case "7": self.zoek_op_titel()
                case "8": self.zoek_op_auteur()
                case "0":
                    print("Programma afgesloten.")
                    break
                case _:
                    print("❌ Ongeldige keuze.")

    # -------------------------------
    # Functies
    # -------------------------------
    def toon_boeken(self):
        boeken = self.repo.get_books()
        if not boeken:
            print("ℹ️ Er staan geen boeken in de database.")
            return

        table = [{
            "ID": b.id,
            "Titel": b.title,
            "Auteur": b.author,
            "Genre ID": b.genre_id,
            "Uitgeleend": "Ja" if b.is_borrowed else "Nee"
        } for b in boeken]

        print(tabulate(table, headers="keys", tablefmt="grid"))

    def voeg_genre_toe(self):
        name = input("Naam van genre: ").strip().lower()

        if name == "":
            print("❌ Naam mag niet leeg zijn.")
            return

        if self.repo.genre_exists_by_name(name):
            print("❌ Dit genre bestaat al.")
            return

        self.repo.add_genre(name)
        print("✔ Genre toegevoegd.")

    def voeg_boek_toe(self):
        title = input("Titel: ").strip().lower()
        author = input("Auteur: ").strip().lower()

        if title == "" or author == "":
            print("❌ Titel en auteur mogen niet leeg zijn.")
            return

        if self.repo.book_exists(title, author):
            print("❌ Dit boek bestaat al.")
            return

        genres = self.repo.get_genres()
        if not genres:
            print("❌ Voeg eerst een genre toe.")
            return

        print("Beschikbare genres:")
        for g in genres:
            print(g)

        genre_id = self.vraag_int("Genre ID: ")
        if genre_id is None or not self.genre_bestaat(genre_id):
            print("❌ Ongeldig Genre ID.")
            return

        self.repo.add_book(title, author, genre_id)
        print("✔ Boek toegevoegd.")

    def markeer_uitgeleend(self):
        book_id = self.vraag_int("Boek ID: ")
        if book_id is None or not self.boek_bestaat(book_id):
            print("❌ Boek niet gevonden.")
            return

        self.repo.set_borrowed(book_id, 1)
        print("✔ Gemarkeerd als uitgeleend.")

    def markeer_terug(self):
        book_id = self.vraag_int("Boek ID: ")
        if book_id is None or not self.boek_bestaat(book_id):
            print("❌ Boek niet gevonden.")
            return

        self.repo.set_borrowed(book_id, 0)
        print("✔ Boek teruggebracht.")

    def export_csv(self):
        boeken = self.repo.get_books()
        if not boeken:
            print("❌ Geen boeken om te exporteren.")
            return

        with open("export.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Titel", "Auteur", "Genre ID", "Uitgeleend"])

            for b in boeken:
                writer.writerow([b.id, b.title, b.author, b.genre_id, b.is_borrowed])

        print("✔ CSV geëxporteerd als export.csv")

    def zoek_op_titel(self):
        keyword = input("Titel of deel van titel: ").strip().lower()

        results = self.repo.search_by_title(keyword)
        if not results:
            print("❌ Geen boeken gevonden.")
            return

        table = [{
            "ID": b.id,
            "Titel": b.title,
            "Auteur": b.author,
            "Genre ID": b.genre_id,
            "Uitgeleend": "Ja" if b.is_borrowed else "Nee"
        } for b in results]

        print(tabulate(table, headers="keys", tablefmt="grid"))

    def zoek_op_auteur(self):
        keyword = input("Auteur of deel van naam: ").strip().lower()

        results = self.repo.search_by_author(keyword)
        if not results:
            print("❌ Geen boeken gevonden.")
            return

        table = [{
            "ID": b.id,
            "Titel": b.title,
            "Auteur": b.author,
            "Genre ID": b.genre_id,
            "Uitgeleend": "Ja" if b.is_borrowed else "Nee"
        } for b in results]

        print(tabulate(table, headers="keys", tablefmt="grid"))


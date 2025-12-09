# -*- coding: utf-8 -*-

from app.models.book import Book
from app.models.genre import Genre

class Repository:
    def __init__(self, db):
        self.db = db

    # ---------- Genres ----------
    def add_genre(self, name):
        self.db.execute("INSERT INTO genres (name) VALUES (?)", (name,))

    def genre_exists_by_name(self, name):
        rows = self.db.query("""
            SELECT * FROM genres WHERE LOWER(name) = LOWER(?)
        """, (name,))
        return len(rows) > 0

    def get_genres(self):
        rows = self.db.query("SELECT * FROM genres")
        return [Genre(r["id"], r["name"]) for r in rows]

    # ---------- Books ----------
    def add_book(self, title, author, genre_id):
        self.db.execute("""
            INSERT INTO books (title, author, genre_id)
            VALUES (?, ?, ?)
        """, (title, author, genre_id))

    def book_exists(self, title, author):
        rows = self.db.query("""
            SELECT * FROM books
            WHERE LOWER(title)=LOWER(?) AND LOWER(author)=LOWER(?)
        """, (title, author))
        return len(rows) > 0

    def get_books(self):
        rows = self.db.query("SELECT * FROM books")
        return [
            Book(r["id"], r["title"], r["author"], r["genre_id"], r["is_borrowed"])
            for r in rows
        ]

    def set_borrowed(self, book_id, borrowed):
        self.db.execute("UPDATE books SET is_borrowed=? WHERE id=?", (borrowed, book_id))

    # ---------- Search ----------
    def search_by_title(self, title):
        rows = self.db.query("""
            SELECT * FROM books 
            WHERE LOWER(title) LIKE LOWER(?)
        """, (f"%{title}%",))
        return [
            Book(r["id"], r["title"], r["author"], r["genre_id"], r["is_borrowed"])
            for r in rows
        ]

    def search_by_author(self, author):
        rows = self.db.query("""
            SELECT * FROM books 
            WHERE LOWER(author) LIKE LOWER(?)
        """, (f"%{author}%",))
        return [
            Book(r["id"], r["title"], r["author"], r["genre_id"], r["is_borrowed"])
            for r in rows
        ]


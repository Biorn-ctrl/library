# -*- coding: utf-8 -*-

class Book:
    def __init__(self, id, title, author, genre_id, is_borrowed):
        self.id = id
        self.title = title
        self.author = author
        self.genre_id = genre_id
        self.is_borrowed = bool(is_borrowed)

    def __repr__(self):
        status = "Uitgeleend" if self.is_borrowed else "Beschikbaar"
        return f"[{self.id}] {self.title} - {self.author} ({status})"



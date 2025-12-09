# -*- coding: utf-8 -*-

from app.db.database import Database
from app.repository import Repository
from app.cli import CLI

def main():
    db = Database()
    repo = Repository(db)
    cli = CLI(repo)
    cli.menu()

if __name__ == "__main__":
    main()


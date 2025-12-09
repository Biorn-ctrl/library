# -*- coding: utf-8 -*-

import sqlite3
import os
import json

class Database:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            cfg = json.load(f)

        self.db_path = cfg["database_path"]
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

        self.initialize_schema()

    def initialize_schema(self):
        with open("app/db/schema.sql", "r") as f:
            schema = f.read()
        self.conn.executescript(schema)
        self.conn.commit()

    def execute(self, query, params=()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()
        return cur

    def query(self, query, params=()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()


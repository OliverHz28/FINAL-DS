from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional

import sqlite3

DB_PATH = Path("app.db")


def init_db() -> None:
    """
    Inicializa la base de datos SQLite creando la tabla `items`
    si no existe todavía.
    """
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()

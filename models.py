# app/database/models.py

import sqlite3
from datetime import datetime

def log_simulation(capacity, sequence, hits, misses):
    conn = sqlite3.connect('logs/cache_log.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cache_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            capacity INTEGER,
            pages TEXT,
            hits INTEGER,
            misses INTEGER
        )
    ''')

    cursor.execute('''
        INSERT INTO cache_logs (timestamp, capacity, pages, hits, misses)
        VALUES (?, ?, ?, ?, ?)
    ''', (datetime.now(), capacity, str(sequence), hits, misses))

    conn.commit()
    conn.close()

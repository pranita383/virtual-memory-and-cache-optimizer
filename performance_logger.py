import sqlite3
from datetime import datetime

def log_performance(hits, misses):
    conn = sqlite3.connect('performance.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cache_performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hits INTEGER,
            misses INTEGER,
            timestamp TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO cache_performance (hits, misses, timestamp)
        VALUES (?, ?, ?)
    ''', (hits, misses, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    conn.commit()
    conn.close()

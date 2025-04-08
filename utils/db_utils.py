# utils/db_utils.py

import sqlite3
from datetime import datetime

DB_FILE = "data/agri_logs.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT,
            location TEXT,
            soil_type TEXT,
            season TEXT,
            irrigation TEXT,
            weather TEXT,
            expert TEXT,
            market TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_interaction(farmer, weather, expert, market):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO interactions
        (crop, location, soil_type, season, irrigation, weather, expert, market, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        farmer['Crop'], farmer['Location'], farmer['Soiltype'], farmer['Season'], farmer['irrigation'],
        str(weather), str(expert), str(market),
        datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()

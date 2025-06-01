import sqlite3
import json
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect("shared_memory.db", check_same_thread=False)
cursor = conn.cursor()

# Create the memory_log table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        format TEXT,
        intent TEXT,
        timestamp TEXT,
        extracted TEXT
    )
""")
conn.commit()

# Log a new entry into the memory table
def log_to_memory(source, file_format, intent, extracted):
    cursor.execute("""
        INSERT INTO memory_log (source, format, intent, timestamp, extracted)
        VALUES (?, ?, ?, ?, ?)
    """, (
        source,
        file_format,
        intent,
        str(datetime.now()),
        json.dumps(extracted)
    ))
    conn.commit()

# Display all memory log entries
def show_memory():
    cursor.execute("SELECT * FROM memory_log")
    logs = cursor.fetchall()
    for row in logs:
        print(row)

from includes import *
import sqlite3

def initialize_database(db_path="tradingbot.db"):
    """Alustaa tietokannan, jos sitä ei ole."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Luo esimerkkitaulu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            action TEXT NOT NULL,
            price REAL NOT NULL,
            amount REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized.")

def save_trade(symbol, action, price, amount):
    """Tallentaa kaupan tietokantaan."""
    conn = sqlite3.connect("tradingbot.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trades (symbol, action, price, amount)
        VALUES (?, ?, ?, ?)
    ''', (symbol, action, price, amount))
    conn.commit()
    conn.close()
    print(f"Trade saved: {action} {amount} of {symbol} at {price}.")

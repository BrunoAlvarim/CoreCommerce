import os
import sqlite3

def create_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "./db/test_mass.db")
    
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS customer(cpf TEXT)") 
    
    cursor.close
    conn.close

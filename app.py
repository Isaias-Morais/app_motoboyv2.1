import sqlite3

conn = sqlite3.connect("Motoboy-Finacias.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table';
""")
resumo = cursor.fetchall()
for i in resumo:
    print i
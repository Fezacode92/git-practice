import sqlite3

conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    cliente TEXT,
    prioridad TEXT
)
""")

# cursor.execute(
#     "INSERT INTO tickets (cliente, prioridad) VALUES (?, ?)",
#     ("Ana", "alta")
# )
# cursor.execute(
#     "INSERT INTO tickets (cliente, prioridad) VALUES (?, ?)",
#     ("Luis", "baja")
# )

cursor.execute(
    "UPDATE tickets SET prioridad = ? WHERE cliente = ?",
    ("alta", "Luis")
)
cursor.execute("DELETE FROM tickets WHERE id > ?", (2,))
conn.commit()

cursor.execute("SELECT * FROM tickets")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conn.close()
print("Database ready")
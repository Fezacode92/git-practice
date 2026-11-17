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

def crear_ticket(cliente, prioridad):
    cursor.execute(
        "INSERT INTO tickets (cliente, prioridad) VALUES (?, ?)",
        (cliente, prioridad)
    )
    conn.commit()

def actualizar_prioridad(cliente, nueva):
    cursor.execute(
        "UPDATE tickets SET prioridad = ? WHERE cliente = ?",
        (nueva, cliente)
    )
    conn.commit()

def buscar_cliente(nombre):
    cursor.execute(
        "SELECT * FROM tickets WHERE cliente = ?",
        (nombre,)
    )
    return cursor.fetchall()

actualizar_prioridad("Marta", "alta")

cursor.execute("SELECT * FROM tickets")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

print(buscar_cliente("Luis"))
conn.close()
print("Database ready")
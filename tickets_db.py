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

def borrar_ticket(id_ticket):
    cursor.execute(
        "DELETE FROM tickets WHERE id = ?",
        (id_ticket,)
    )
    conn.commit()

actualizar_prioridad("Ana", "baja")

cursor.execute("SELECT * FROM tickets ORDER BY cliente DESC")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

print(buscar_cliente("Luis"))
cursor.execute("SELECT prioridad, COUNT(*) FROM tickets GROUP BY prioridad")
print(cursor.fetchall())
conn.close()
print("Database ready")
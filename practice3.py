libro = {"titulo": "1984", "autor": "George Orwell", "año": 1948, "genero": "Novela"}
print(libro["titulo"])
print(libro["autor"])
print(libro["año"])
print(libro["genero"])

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for key, value in persona.items():
    print(f"{key}: {value}")

precios = {"manzana": 0.5, "banana": 0.3, "naranja": 0.4}
total = 0
for fruta, precio in precios.items(): 
    total += precio
print(f"Total: {total} euros")

precios = {"cafe": 1500, "medialuna": 800, "jugo": 2200, "tostadas": 3000}
total = 0
for producto, precio in precios.items():
   if precio > 1000: 
        total += precio
print(f"Total: {total} pesos")

tickets = [
    {"id": 1, "cliente": "Ana", "problema": "No puede entrar", "prioridad": "alta"},
    {"id": 2, "cliente": "Luis", "problema": "Factura duplicada", "prioridad": "media"},
    {"id": 3, "cliente": "Sofía", "problema": "Cambio de contraseña", "prioridad": "baja"},
    {"id": 4, "cliente": "Pedro", "problema": "Error en la app", "prioridad": "alta"}]
total = 0
for ticket in tickets:
   if ticket["prioridad"] == "alta" or ticket["prioridad"] == "media":
        print(f"Cliente: {ticket['cliente']}, Problema: {ticket['problema']}, Prioridad: {ticket['prioridad']}")
        total += 1
print(f"Total de tickets de alta prioridad: {total}")

contar_prioridad = {"alta": 0, "media": 0, "baja": 0}
for ticket in tickets:
    contar_prioridad[ticket["prioridad"]] += 1
print(f"Tickets de alta prioridad: {contar_prioridad['alta']}")
print(f"Tickets de media prioridad: {contar_prioridad['media']}")
print(f"Tickets de baja prioridad: {contar_prioridad['baja']}")

def contar_prioridad(tickets):
    """Counts the number of tickets for each priority level."""
    conteo = {"alta": 0, "media": 0, "baja": 0}
    for ticket in tickets:
        conteo[ticket["prioridad"]] += 1
    return conteo
resultado = contar_prioridad(tickets)
print(f"Alta: {resultado['alta']}")
print(f"Media: {resultado['media']}")
print(f"Baja: {resultado['baja']}")

def filtrar_por_prioridad(tickets, prioridad):
    # 1. start an empty list
    lista = []
    # 2. loop through the tickets
    for ticket in tickets:
        # 3. if the ticket's priority == prioridad, append the ticket
        if ticket["prioridad"] == prioridad:
            lista.append(ticket)
    # 4. return the list (remember the vote box!)
    return lista
urgentes = filtrar_por_prioridad(tickets, "media")
for ticket in urgentes:
    print(f"Ticket {ticket['id']}: {ticket['cliente']} - {ticket['problema']}")

def buscar_cliente(tickets, cliente):
    for ticket in tickets:
        if ticket["cliente"] == cliente:
            print(f"Ticket {ticket['id']}: {ticket['problema']}")

def buscar_cliente(tickets, nombre_cliente):
    for ticket in tickets:
        if ticket["cliente"] == nombre_cliente:
            return f"Ticket {ticket['id']}: {ticket['problema']}"
    return "No se encontró el cliente"
print(buscar_cliente(tickets, "Pedro"))

def filtrar_urgentes(tickets):
    lista = []
    for ticket in tickets:
        if ticket["prioridad"] == "alta" or ticket["prioridad"] == "media":
            lista.append(ticket)
    return lista
urgentes = filtrar_urgentes(tickets)
for ticket in urgentes:
    print(f"Ticket {ticket['id']}: {ticket['cliente']} - {ticket['problema']}")
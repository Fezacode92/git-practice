tickets = [
    {"client": "Ana", "priority": "high"},
    {"client": "Luis", "priority": "low"},
    {"client": "Marta", "priority": "high"},
    {"client": "Pedro", "priority": "medium"},
]

def count_by_priority(ticket_list, priority):
    count = 0
    for ticket in ticket_list:
        if ticket["priority"] == priority:
            count = count + 1
    return count

print(count_by_priority(tickets, "high"))
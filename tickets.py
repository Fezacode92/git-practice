def filter_urgent(tickets):
    urgent_tickets = []
    for ticket in tickets:
        if ticket["priority"] in ["high", "medium"]:
            urgent_tickets.append(ticket)
    return urgent_tickets
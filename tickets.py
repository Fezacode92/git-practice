def filter_urgent(tickets):
    urgent_tickets = []
    for ticket in tickets:
        if ticket["priority"] in ["high", "medium"]:
            urgent_tickets.append(ticket)
    return urgent_tickets




def find_client(tickets, client_name):
    matching_tickets = []
    for ticket in tickets:
        if ticket["client"] == client_name:
            matching_tickets.append(ticket)
    return matching_tickets
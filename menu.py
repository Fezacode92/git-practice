import os

while True:
    os.system("clear")
    print("1. View tickets")
    print("2. Add ticket")
    print("3. Quit")
    print("4. Count tickets")
    print("5. Clear all tickets")
    choice = input("Choose: ")
    os.system("clear")

    if choice == "1":
        with open("tickets.txt", "r") as file:
            for line in file:
                print(line.strip())
    elif choice == "2":
        new_ticket = input("Describe the new ticket: ")
        os.system("clear")
        with open("tickets.txt", "a") as file:
            file.write(new_ticket + "\n")
        print("Ticket added!")
    elif choice == "3":
        print("Goodbye!")
        os.system("clear")
        break
    elif choice == "4": 
        tickets = []
        with open("tickets.txt", "r") as file:
            tickets = [line.strip() for line in file]
        print(f"Total tickets: {len(tickets)}")
    elif choice == "5":
        with open("tickets.txt", "w") as file:
            pass
        print("All tickets cleared!")
    else:
        print("Please choose 1, 2, 3, 4 or 5.")
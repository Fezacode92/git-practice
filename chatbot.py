print("Hi! I'm Jenny, the Jenesis House helper. Type 'bye' to leave.")

while True:
    message = input("You: ").lower()

    if message == "bye":
        print("Jenny: Have a peaceful day!")
        break
    elif "facial" in message:
        print("Jenny: Radiance Renewal Facial is 60 min for $150.")    
    elif "massage" in message:
        print("Jenny: Tranquility Flow Massage is 60 min for $250.")
    elif "reiki" in message:
        print("Jenny: Reiki Restoration is 60 min for $225.")
    else:
        print("Jenny: Sorry, I didn't catch that. Try asking about facials, massage or reiki.")
 
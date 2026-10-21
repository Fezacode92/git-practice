def greet_evens(numbers):
    for number in numbers:
        if number % 2 == 0:
            print("number, " + str(number) + "is even")
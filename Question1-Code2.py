number = input("Insert a number: ")

try:
    number = int(number)
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
except:
    print("Please use a number, not words")
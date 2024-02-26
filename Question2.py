number = input("Insert a number: ")

try:
    number = int(number)
    print("Positive") if number > 0 else print("Negative") if number < 0 else print("Zero")
except:
    print("Please use a number, not words")
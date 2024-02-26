num1 = input("Insert 1st number: ")
num2 = input("Insert 2nd number: ")
num3 = input("Insert 3rd number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    if num1 > num2 and num1 > num3:
        print("Biggest: ", num1)
    elif num2 > num1 and num2 > num3:
        print("Biggest: ", num2)
    elif num3 > num1 and num3 > num2:
        print("Biggest: ", num3)
except:
    print("Please use numbers, not words")
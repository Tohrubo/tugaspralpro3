temp = input("Insert your temprature: ")

try:
    temp = int(temp)
    if temp >= 38:
        print("You are feverish")
    else:
        print("You are not feverish")
except:
    print("Please use numbers, not words")
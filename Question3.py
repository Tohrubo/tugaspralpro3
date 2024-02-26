mth = input("Pick a month (1-12): ")

try:
    mth = int(mth)
    if mth > 12:
        print("This month doesn't exist (Invalid)")
    elif mth == 4 or mth == 6 or mth == 9 or mth == 11:
        print("This month has 30 days")
    elif mth == 2:
        print("This month has 28 days and 29 days on leap years")
    else:
        print("This month has 31 days")
except:
    print("Please use a number, not word(s)")
s1 = input("Insert side 1: ")
s2 = input("Insert side 2: ")
s3 = input("Insert side 3: ")

try:
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    
    if s1 == s2 == s3:
        print("Three sides are equal")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Two sides are the same")
    else:
        print("No sides are equal")
except:
    print("Please use numbers, not words")
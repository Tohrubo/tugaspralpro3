# x = 1
# y = 0

# print(x == y)
# print(x != y)
# print(x > y)
# print(x >= y)
# print(x < y)
# print(x <= y)
# print(x is y)
# print(x is not y)

# a = 0

# if a == 1:    
#     print("Berhasil")
# print("Test")

# t = 5

# if t == 0:
#     print("Nice")
# else:
#     print("What?")
# print("Hello")

# l = 90

# if l == 1:
#     print("Whuh?")
# elif l == 90:
#     print("Ah, ok")
# elif l > 70:
#     print("Hmm...")
# else:
#     print("Nope")

# d = 2
# print("Whuh?") if d == 1 else print("Great") if d > 0 else print("Natha")

# inp = int(input("Angka: "))

inp = input("Angka: ")

try:
    inp = int(inp)
    print("Number ", inp)
except:
    print("Please use number")
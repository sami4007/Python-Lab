Num = int(input("Enter a number: "))

a = 0
b = 1

while a < Num:
    print(a)
    c = a + b
    a = b
    b = c
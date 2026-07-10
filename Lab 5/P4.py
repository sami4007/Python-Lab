index = int(input("Enter the number of elements: "))

numbers = []

for i in range(index):
    num = int(input("Enter element: "))
    numbers.append(num)

search = int(input("Enter the value to search: "))

found = False

for i in range(index):
    if numbers[i] == search:
        print("Value found at index", i)
        found = True
        break

if found == False:
    print("Value not found")
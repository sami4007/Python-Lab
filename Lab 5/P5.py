index = int(input("Enter the number of elements: "))

numbers = []

for i in range(index):
    num = int(input("Enter element: "))
    numbers.append(num)

for i in range(index):
    if numbers[i] == 20:
        numbers[i] = 200

print("Updated List:", numbers)
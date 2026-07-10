index = int(input("Enter the number of elements: "))

numbers = []

for i in range(index):
    num = int(input("Enter element: "))
    numbers.append(num)

new_list = []

for item in numbers:
    if item not in new_list:
        new_list.append(item)

print("List after removing duplicates:", new_list)
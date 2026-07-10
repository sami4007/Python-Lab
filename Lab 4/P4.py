def distinct(list):
    new_list = []

    for item in list:
        if item not in new_list:
            new_list.append(item)

    return new_list

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

result = distinct(numbers)

print("Distinct elements:", result)
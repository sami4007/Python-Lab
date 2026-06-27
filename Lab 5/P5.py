def count_elements(list):
    count = {}

    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1

    for key in count:
        print(key, "=>", count[key])

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

count_elements(numbers)
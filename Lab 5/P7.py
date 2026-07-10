index = int(input("Enter the number of strings: "))

words = []

for i in range(index):
    word = input("Enter a string: ")
    words.append(word)

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Count =", count)
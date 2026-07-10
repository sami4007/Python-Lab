text = input("Enter a string: ")

words = text.split()

result = ""

for word in words:
    result = result + word[::-1] + " "

print(result)
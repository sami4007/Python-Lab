try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise TypeError("Inputs must be numeric values.")

    print("Sum:", num1 + num2)

except TypeError as err:
    print("Error:", err)
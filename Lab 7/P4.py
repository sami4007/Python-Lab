try:
  
    file = open("student.txt", "w")
    file.write("Hello, this is my first file.\n")
    file.close()

    file = open("student.txt", "r")
    print(file.read())
    file.close()

    file = open("student.txt", "a")
    file.write("This is an appended line.\n")
    file.close()
    
    file = open("student.txt", "r")
    print(file.read())
    file.close()

except Exception as e:
    print("Error:", e)
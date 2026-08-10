#with is used to automatically closes the file
with open("students.txt", "r") as file:
    data = file.read()
    print(data)
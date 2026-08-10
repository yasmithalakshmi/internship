with open("students.txt", "r+") as file:
    print(file.read())
    file.write("\nNew content")

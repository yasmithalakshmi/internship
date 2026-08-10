with open("demo.txt", "a+") as file:
    file.write("\nDjango Framework")
    file.seek(0)
    print(file.read())

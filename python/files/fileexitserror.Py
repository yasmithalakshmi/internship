try:
   with open("students.txt", "x") as file:
       file.write("New student file")
except FileExistsError:
     print("The file already exists.")

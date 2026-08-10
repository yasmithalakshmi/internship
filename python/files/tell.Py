with open("students.txt", "r") as file:
   print(file.tell())
   file.read(5)
   print(file.tell())
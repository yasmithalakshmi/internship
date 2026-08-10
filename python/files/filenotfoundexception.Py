try:
   with open("newfile.txt", "r") as file:
       print(file.read())
except FileNotFoundError:
   print("The requested file was not found.")
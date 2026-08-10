#exception handling with file handling example
try:
   file = open("students.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
     print("The file does not exist.")
finally:
    try:
       file.close()
    except NameError:
         print("File was never opened.")
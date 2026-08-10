try:
  with open("students.txt", "r") as file:
    content = file.read()
except FileNotFoundError:
   print("Student file was not found.")
except permissionError:
   print("Permission denied.")  
else:
    print(content)
finally:
   print("File operation completed.")

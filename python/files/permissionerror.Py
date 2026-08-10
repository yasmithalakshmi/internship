try:
  with open("students.txt", "w") as file:
      file.write("New content")
except PermissionError:
    print("Permission denied.")
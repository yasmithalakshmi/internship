#write and read to a file
file = open("students.txt", "w+")
file.write("yasmitha")
file.seek(0)
data = file.read()
print(data)
file.close()
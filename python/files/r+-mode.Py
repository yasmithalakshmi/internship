#read and write to a file
file = open("students.txt", "r+")
data = file.read()
print(data)
file.write("hii yash!!! hello everyone")
file.close()

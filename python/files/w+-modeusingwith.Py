with open("students.txt", "w+") as f:
    f.write("Machine Learning\n")
    f.seek(0)
    data = f.read()
    print(data)
    f.close()
    
    
    
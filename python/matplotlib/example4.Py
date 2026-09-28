import matplotlib
import matplotlib.pyplot as plt
marks = [35, 40, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65, 70, 75, 80, 85, 90]
plt.hist(marks,bins=10)
plt.title("range of marks of the students")
plt.xlabel("marks")
plt.ylabel("number of students")
plt.show()
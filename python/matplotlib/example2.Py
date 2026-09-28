import matplotlib
import matplotlib.pyplot as plt
cources = ['python','java','c','javascript','c++']
students = [30,20,25,35,15]
plt.bar(cources,students)
plt.title("count of students of each course")
plt.xlabel("programming languages")
plt.ylabel("number of students")
plt.show()
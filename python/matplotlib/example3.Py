import matplotlib
import matplotlib.pyplot as plt
students = ['a','b','c','d','e','f']
study_hours = [1,2,3,4,5,6]
marks = [40,45,55,65,75,85]
plt.scatter(study_hours,marks)
plt.title('marks based on study hours')
plt.xlabel("number of study hours")
plt.ylabel("marks of the students")
plt.show()



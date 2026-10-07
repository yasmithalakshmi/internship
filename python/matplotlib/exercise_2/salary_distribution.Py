import matplotlib.pyplot as plt
salary = [    22000, 25000, 27000, 28000, 30000,    31000, 32000, 35000, 36000, 38000,    40000, 42000, 45000, 47000, 50000,    52000, 55000, 60000, 75000, 120000 ]
plt.hist(salary, bins=5, edgecolor='black')
plt.title('Histogram of Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid()
plt.show()
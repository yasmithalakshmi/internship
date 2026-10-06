import matplotlib.pyplot as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = [2, 3, 4, 3, 5]
plt.style.use("ggplot")
plt.plot(days,hours,marker='o')
plt.title("Weekly Study Tracking")
plt.xlabel("days")
plt.ylabel("study hours")
plt.grid()
plt.savefig("styled_graph.png")
plt.show()
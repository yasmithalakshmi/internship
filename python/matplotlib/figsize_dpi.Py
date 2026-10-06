import matplotlib.pyplot as plt
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
values = [20, 35, 30, 45, 50]
hours = [2, 3, 4, 3, 5]
plt.figure(figsize=(10,5),dpi=100)
plt.plot(days,values,marker='o')
plt.title("weekly tracking")
plt.xlabel("days")
plt.ylabel("values")
plt.grid()
plt.savefig("progress.png")
plt.show()

 
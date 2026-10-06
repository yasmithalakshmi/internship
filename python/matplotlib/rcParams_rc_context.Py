import matplotlib.pyplot as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = [2, 3, 4, 3, 5]
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["font.size"] = 12#changes the default for your figures.
with plt.rc_context({"font.size":14}):# temporarily changes a value after the block the value became to 12
    plt.plot(days,hours,marker='o')
    plt.title("Weekly Study Tracking")
    plt.xlabel("Days")
    plt.ylabel("Study Hours")
    plt.grid()
plt.show()
print(plt.rcParams["font.size"])
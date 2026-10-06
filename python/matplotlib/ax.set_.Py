import matplotlib.pyplot as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
study = [2, 3, 4, 3, 5]
exercise = [1, 2, 1, 2, 3]
fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle("weekly progress")
ax1.plot(days,study,marker='o')
ax1.set_title("Study tracking")
ax1.set_xlabel("Days")
ax1.set_ylabel("study")
ax1.grid()
ax2.plot(days,exercise,marker='s')
ax2.set_title("Exercise tracking")
ax2.set_xlabel("Days")
ax2.set_ylabel("Exercises")
ax2.grid()
plt.tight_layout()
plt.show()



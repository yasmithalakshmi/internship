import matplotlib.pyplot as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = [2, 3, 4, 3, 5]
fig, ax = plt.subplots()
ax.plot(days,hours,marker='o')
ax.set_title("Weekly Study Tracking")
ax.set_xlabel("Days")
ax.set_ylabel("Study Hours")
ax.axhline(y=3,color="green")#used to add the horizantal line at specified position
ax.axvline(x="wednesday",color="orange")#used to add the vertical line at the specified position
ax.tick_params(axis='x' , rotation=45)# oops approch of plt.xticks() and yticks
ax.tick_params(axis='both' , labelsize=12 )
ax.spines["top"].set_visible(False)#used to change the spines(top,bottom,right,left)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_linewidth(2)
ax.grid()
plt.show()
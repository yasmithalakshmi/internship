import matplotlib.pyplot as plt
days = ['monday','tuesday','wednesday','thursday','friday']
study_hours = [2, 3, 4, 3, 5]
#marks =[50,60,70,65,85]
hours = [1,2,2,3,2]
fig, (ax1, ax2) = plt.subplots(2, 1 )#sharey=True
fig.suptitle("weekly activity report")
ax1.plot(days,study_hours,marker='o',label='study')
ax1.set_title("study tracking")
ax1.set_xlabel("working days")
ax1.set_ylabel("working hours")
ax1.grid()
ax2.plot(days,hours,marker='s',label='exercise')
ax2.set_title("hours tracking")
ax2.set_xlabel("working days")
#ax2.set_ylabel("working hours")
ax2.grid()
fig.text(
    0.5, 0.02,
    "Weekly progress tracking",
    ha="center"
)
fig.legend()
#plt.tight_layout()
plt.subplots_adjust(hspace=0.6)
plt.show()
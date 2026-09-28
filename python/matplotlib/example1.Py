import matplotlib.pyplot as plt
days = ['monday','tuesday','wednesday','thursday','friday']
study_hours = [2, 3, 4, 3, 5]
exercise_hours = [1, 1, 2, 1, 2]
#hours = [3,2,3,2,3]
#plt.plot(days,hours,color='purple',marker='o',linestyle='--',linewidth=4,alpha=0.6)
#plt.figure(figsize=(8, 5))
#plt.subplot(1, 2, 1)
plt.title("study vs exercise tracking")
plt.plot(days,study_hours,label = 'study',marker='o')
plt.xlabel("study days")
plt.ylabel("no.of hours per day")
#plt.xticks(rotation=45)
#plt.yticks([0,2,4,6,8])
#plt.subplot(1,2,2)
plt.plot(days,exercise_hours,label = 'exercise',marker='s')
plt.xlabel("exercise days")
plt.ylabel("no.of hours per day")
plt.legend()
plt.grid()
#plt.tight_layout()
#plt.savefig("study_exercise.png")
#plt.ylim(0,8)
#plt.text(4,5,'highest')
#plt.annotate( 'highest study',
    #xy=(4,5),
   # xytext=(2.5,6),
   # arrowprops=dict(arrowstyle="->") )
plt.show()
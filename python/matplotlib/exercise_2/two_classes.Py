import matplotlib.pyplot as plt
class_a = [55, 60, 62, 65, 67, 70, 72, 75, 78]
class_b = [60, 65, 68, 70, 73, 76, 80, 82, 85]
plt.hist(class_a, bins=5, edgecolor='black', alpha=0.7, label='Class A')
plt.hist(class_b, bins=5, edgecolor='black', alpha=0.7, label='Class B')
plt.title('Comparison of Two Classes')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()
plt.grid()
plt.show()
import matplotlib.pyplot as plt
product = ["laptop","desktop","keyboards"]
sales = [120000,34000,56000]
plt.barh(product,sales)
plt.title("sales report")
plt.xlabel("product")
plt.ylabel("sales")
plt.show()

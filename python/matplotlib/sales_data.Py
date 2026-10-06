import matplotlib.pyplot as plt

#sales = [100, 500, 300, 300, 400]
#years = [2018, 2019, 2020, 2021, 2022]
months = ['jan','feb','march','april']
sales_2025 = [200,300,100,500]
sales_2026 =[100,300,400,200]
plt.plot(months,sales_2025, linestyle = "--", marker = 'D',label=2025)
plt.title("sales data 2025")
plt.xlabel("months")
plt.ylabel("sales")
plt.grid()
plt.plot(months,sales_2026,marker='o',label=2026)
plt.legend()
plt.show()
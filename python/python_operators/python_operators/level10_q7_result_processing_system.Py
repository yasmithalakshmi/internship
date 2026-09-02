# Level 10 - Question 7
# Result Processing System.

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = maths + science + english
average = total / 3
percentage = average
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Pass:", percentage >= 35)

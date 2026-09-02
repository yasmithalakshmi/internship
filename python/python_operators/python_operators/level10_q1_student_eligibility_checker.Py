# Level 10 - Question 1
# Student Eligibility Checker using arithmetic, comparison, and logical operators.

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
attendance = float(input("Enter attendance percentage: "))

average = (maths + science) / 2
print("Average:", average)
print(average >= 50 and attendance >= 75)

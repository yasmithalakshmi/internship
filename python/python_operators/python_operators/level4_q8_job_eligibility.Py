# Level 4 - Question 8
# Check whether a person is eligible for a job based on age and qualification.

age = int(input("Enter age: "))
qualified = input("Are you qualified? (yes/no): ")
print(age >= 18 and qualified.lower() == "yes")

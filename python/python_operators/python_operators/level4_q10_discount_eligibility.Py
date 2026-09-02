# Level 4 - Question 10
# Check whether a user is eligible for a discount based on age or membership status.

age = int(input("Enter age: "))
member = input("Are you a member? (yes/no): ")
print(age >= 60 or member.lower() == "yes")

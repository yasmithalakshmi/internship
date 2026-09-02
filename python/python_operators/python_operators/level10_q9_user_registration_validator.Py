# Level 10 - Question 9
# User Registration Validator using comparison, logical, and membership operators.

username = input("Enter username: ")
email = input("Enter email: ")
allowed_users = ["admin", "user1", "guest"]
print(username in allowed_users and "@" in email)

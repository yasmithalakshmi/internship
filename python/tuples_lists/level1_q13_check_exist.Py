# Level 1: Lists - Question 13
# Check if element exists in list using 'in' operator

numbers = [10, 20, 30, 40, 50]

print("Numbers list:", numbers)

search_value = 30

if search_value in numbers:
    print(search_value, "exists in list")
else:
    print(search_value, "does not exist in list")

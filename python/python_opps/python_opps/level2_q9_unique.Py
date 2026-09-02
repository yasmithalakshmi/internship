# Level 2: Lists with Loops - Question 9
# Remove duplicates and keep unique values

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

print("Original list with duplicates:", numbers)

unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Unique values:", unique_list)

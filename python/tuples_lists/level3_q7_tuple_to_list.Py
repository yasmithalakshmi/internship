# Level 3: Lists & Tuples - Question 7
# Create tuple of numbers, convert to list, add three new numbers

numbers_tuple = (10, 20, 30, 40, 50)

print("Original tuple:", numbers_tuple)
print("Type:", type(numbers_tuple))

numbers_list = list(numbers_tuple)
print("\nConverted to list:", numbers_list)
print("Type:", type(numbers_list))

print("\nAdding three new numbers:")
numbers_list.append(60)
numbers_list.append(70)
numbers_list.append(80)

print("List after adding:", numbers_list)

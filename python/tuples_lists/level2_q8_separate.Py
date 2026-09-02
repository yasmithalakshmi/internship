# Level 2: Lists with Loops - Question 8
# Separate even and odd numbers into two lists

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Original list:", numbers)

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

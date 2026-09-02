# Level 2: Lists with Loops - Question 6
# Calculate average of all numbers

numbers = [10, 20, 30, 40, 50]

print("Numbers list:", numbers)

total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)

print("Total:", total)
print("Average:", average)

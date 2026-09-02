# Level 2: Lists with Loops - Question 7
# Count numbers greater than 50

numbers = [30, 45, 60, 50, 75, 25, 80, 40]

print("Numbers list:", numbers)

count = 0
for num in numbers:
    if num > 50:
        count = count + 1

print("Count of numbers greater than 50:", count)

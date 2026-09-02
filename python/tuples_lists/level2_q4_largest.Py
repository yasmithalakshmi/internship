# Level 2: Lists with Loops - Question 4
# Find largest number in list using manual loop

numbers = [45, 23, 89, 12, 67, 34, 90, 56]

print("Numbers list:", numbers)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

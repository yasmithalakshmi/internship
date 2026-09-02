# Level 2: Lists with Loops - Question 5
# Find smallest number in list using manual loop

numbers = [45, 23, 89, 12, 67, 34, 90, 56]

print("Numbers list:", numbers)

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)

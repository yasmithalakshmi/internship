# Level 2: Lists with Loops - Question 1
# Filter and print even numbers from list

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Numbers list:", numbers)

print("\nEven numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

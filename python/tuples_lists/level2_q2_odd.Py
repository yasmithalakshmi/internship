# Level 2: Lists with Loops - Question 2
# Filter and print odd numbers from list

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Numbers list:", numbers)

print("\nOdd numbers:")
for num in numbers:
    if num % 2 != 0:
        print(num)

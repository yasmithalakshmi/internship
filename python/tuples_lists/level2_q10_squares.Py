# Level 2: Lists with Loops - Question 10
# Create new list with squares of each number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original numbers:", numbers)

squares = []
for num in numbers:
    square = num * num
    squares.append(square)

print("Squares:", squares)

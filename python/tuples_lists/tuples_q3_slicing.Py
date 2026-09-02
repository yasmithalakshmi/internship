# Tuples - Question 3
# Slice tuple to get different ranges

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("Original tuple:", numbers)

slice1 = numbers[0:3]
print("First 3 elements [0:3]:", slice1)

slice2 = numbers[-3:]
print("Last 3 elements [-3:]:", slice2)

slice3 = numbers[2:6]
print("Elements from index 2 to 6 [2:6]:", slice3)

# Level 3: Lists & Tuples - Question 5
# Create tuple containing lists, access and modify elements

data = ([10, 20, 30], [40, 50, 60], [70, 80, 90])

print("Tuple containing lists:", data)
print("First list:", data[0])
print("Second element of first list:", data[0][1])

print("\nModifying first list (adding 25):")
data[0].append(25)
print("First list after modification:", data[0])

print("\nTuple after modification:", data)

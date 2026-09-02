# Level 6 - Question 5
# Create two dictionary objects with the same data and check their identity.

d1 = {"name": "Alice"}
d2 = {"name": "Alice"}
print(d1 == d2)
print(d1 is d2)

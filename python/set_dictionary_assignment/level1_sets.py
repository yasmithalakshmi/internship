# Level 1: Sets
# Write Python code for all the questions below.

# 1. Create a set containing 5 fruits and print all elements.
# 2. Create a set of numbers and find its length.
# 3. Create a set and add a new element using add().
# 4. Create a set and add multiple elements using update().
# 5. Create a set and remove a specific element using remove().
# 6. Create a set and remove a specific element using discard().
# 7. Create a set and remove an element using pop().
# 8. Create a set of numbers and check whether a particular number exists.
# 9. Create two sets and find their union.
# 10. Create two sets and find their intersection.
# 11. Create two sets and find their difference.
# 12. Create two sets and find their symmetric difference.
# 13. Create two sets and check whether one set is a subset of another set.
# 14. Create two sets and check whether one set is a superset of another set.
# 15. Create a list containing duplicate values and convert it into a set to remove duplicates.

# Solutions
fruits = {"apple", "banana", "mango", "grape", "orange"}
print("1. Fruits set:", fruits)

numbers = {10, 20, 30, 40, 50}
print("2. Length of set:", len(numbers))

marks = {65, 70, 80}
marks.add(90)
print("3. After add():", marks)

set1 = {1, 2, 3}
set1.update([4, 5, 6])
print("4. After update():", set1)

colors = {"red", "blue", "green", "yellow"}
colors.remove("blue")
print("5. After remove():", colors)

colors2 = {"red", "blue", "green"}
colors2.discard("black")
print("6. After discard():", colors2)

nums = {11, 22, 33, 44}
removed = nums.pop()
print("7. pop() removed:", removed, "Remaining:", nums)

check_set = {10, 20, 30, 40}
print("8. Number exists?", 30 in check_set)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("9. Union:", set_a | set_b)
print("10. Intersection:", set_a & set_b)
print("11. Difference:", set_a - set_b)
print("12. Symmetric difference:", set_a ^ set_b)
print("13. subset:", {1, 2}.issubset(set_a))
print("14. superset:", set_a.issuperset({1, 2, 3}))

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = set(list_with_duplicates)
print("15. Duplicate list to set:", unique_list)

# Set & Dictionary Combined
# Write Python code for all the questions below.

# 1. Create two sets of student names and use a dictionary to store each student's course.
# 2. Create a list of student names with duplicates and create a dictionary containing each student's name and number of occurrences.
# 3. Create a dictionary of employees and their departments. Use sets to find all unique departments.
# 4. Create two dictionaries containing student marks for two subjects. Find students who appear in both dictionaries.
# 5. Create a dictionary of products and prices. Use a set to store all products whose price is above ₹5,000.

# Solutions
student_course = {
    "Asha": "Python",
    "Bharat": "Java",
    "Chitra": "Python",
    "David": "C++",
    "Esha": "Java"
}
student_names = {"Asha", "Bharat", "Chitra", "David"}
print("1. Student course dictionary:", student_course)

name_list = ["Asha", "Asha", "Bharat", "Chitra", "Asha", "David", "Bharat"]
name_occurrences = {}
for name in name_list:
    name_occurrences[name] = name_list.count(name)
print("2. Name occurrences:", name_occurrences)

employees = {"Alice": "HR", "Bob": "IT", "Charlie": "HR", "Dina": "Finance"}
unique_departments = set(employees.values())
print("3. Unique departments:", unique_departments)

math_marks = {"Asha": 90, "Bharat": 80, "Chitra": 85}
science_marks = {"Bharat": 88, "David": 75, "Asha": 92}
print("4. Students in both dictionaries:", set(math_marks) & set(science_marks))

product_prices = {"Laptop": 60000, "Phone": 20000, "Tablet": 35000, "Mouse": 700}
expensive_products = {name for name, price in product_prices.items() if price > 5000}
print("5. Products above ₹5,000:", expensive_products)

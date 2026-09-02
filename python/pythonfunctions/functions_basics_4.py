# 4. Function Arguments - Default, Keyword, Positional, *args, **kwargs

def total_price(price, tax_percent=10):
    tax = price * tax_percent / 100
    total = price + tax
    return total


def display_student_info(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


def area_of_rectangle(length, breadth):
    return length * breadth


def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total


def largest_number(*args):
    if not args:
        return None
    largest = args[0]
    for value in args[1:]:
        if value > largest:
            largest = value
    return largest


def display_employee_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def display_student_details(*args, **kwargs):
    print("Student details:")
    for value in args:
        print(value)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def average_values(*args):
    if not args:
        return 0
    total = 0
    for value in args:
        total += value
    return total / len(args)


print("Total price:", total_price(500))
print("Total price with tax:", total_price(500, 12))
display_student_info(name="Asha", age=20, course="BCA")
print("Area:", area_of_rectangle(10, 5))
print("Sum:", sum_values(1, 2, 3, 4, 5))
print("Largest:", largest_number(8, 12, 3, 20, 5))
display_employee_info(name="Ravi", department="IT", salary=45000)
display_student_details("Riya", "BCA", marks=90, age=21)
print("Average:", average_values(10, 20, 30, 40))

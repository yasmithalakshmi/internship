# Function practice group 4

def total_price(price, tax_percent=10):
    tax = price * tax_percent / 100
    return price + tax


def display_student_info(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


def area_of_rectangle(length, breadth):
    return length * breadth


def sum_any(*args):
    total = 0
    for value in args:
        total += value
    return total


def largest_any(*args):
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
    print("Values:", args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def average_any(*args):
    if not args:
        return 0
    total = 0
    for value in args:
        total += value
    return total / len(args)


print("Total price:", total_price(500))
print("Total price with custom tax:", total_price(500, 12))
display_student_info(name="Asha", age=20, course="BCA")
print("Area:", area_of_rectangle(12, 8))
print("Sum:", sum_any(2, 4, 6, 8))
print("Largest:", largest_any(3, 9, 1, 15, 4))
display_employee_info(name="Ravi", department="IT", salary=45000)
display_student_details("Riya", 20, marks=90, course="MCA")
print("Average:", average_any(10, 20, 30, 40))

from pathlib import Path

base = Path(r"c:\Users\yasmitha\OneDrive\internship\python\classes&objects")
base.mkdir(parents=True, exist_ok=True)

items = [
    ("set1_01_student_class.Py", """class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Alice", 18, "BCA")
s2 = Student("Bob", 20, "BSc")
s3 = Student("Charlie", 19, "MBA")

print("Student 1:", s1.name, s1.age, s1.course)
print("Student 2:", s2.name, s2.age, s2.course)
print("Student 3:", s3.name, s3.age, s3.course)
"""),
    ("set1_02_car_class.Py", """class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

car1 = Car("Toyota", "Corolla", 2020, 1800000)
car2 = Car("Honda", "Civic", 2022, 2200000)
car3 = Car("Maruti", "Swift", 2021, 900000)

print("Car 1:", car1.brand, car1.model, car1.year, car1.price)
print("Car 2:", car2.brand, car2.model, car2.year, car2.price)
print("Car 3:", car3.brand, car3.model, car3.year, car3.price)
"""),
    ("set1_03_employee_class.Py", """class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

emp = Employee("Rahul", "IT", 45000)
print("Employee Name:", emp.name)
print("Department:", emp.department)
print("Salary:", emp.salary)
"""),
    ("set1_04_mobile_class.Py", """class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

m = Mobile("Samsung", "Galaxy M32", 18000)
print("Brand:", m.brand)
print("Model:", m.model)
print("Price:", m.price)
"""),
    ("set1_05_book_class.Py", """class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Basics", "John", 350)
book2 = Book("Data Structures", "Alice", 500)

print("Book 1:", book1.title, book1.author, book1.price)
print("Book 2:", book2.title, book2.author, book2.price)
"""),
    ("set1_06_laptop_class.Py", """class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

laptop = Laptop("Dell", "16GB", "Intel i5", 55000)
print("Brand:", laptop.brand)
print("RAM:", laptop.ram)
print("Processor:", laptop.processor)
print("Price:", laptop.price)
"""),
    ("set1_07_college_class.Py", """class College:
    def __init__(self, college_name, location, course):
        self.college_name = college_name
        self.location = location
        self.course = course

c1 = College("ABC College", "Hyderabad", "B.Tech")
c2 = College("XYZ College", "Chennai", "BCA")
c3 = College("PQR College", "Bangalore", "MBA")

print("College 1:", c1.college_name, c1.location, c1.course)
print("College 2:", c2.college_name, c2.location, c2.course)
print("College 3:", c3.college_name, c3.location, c3.course)
"""),
    ("set1_08_product_class.Py", """class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

p = Product("Laptop", 50000, 2)
print("Product Name:", p.product_name)
print("Price:", p.price)
print("Quantity:", p.quantity)
"""),
    ("set1_09_bankaccount_class.Py", """class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

acc = BankAccount("Ravi", 1234567890)
print("Account Holder:", acc.account_holder)
print("Account Number:", acc.account_number)
"""),
    ("set1_10_movie_class.Py", """class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

m1 = Movie("Bahubali", "Prabhas", "Anushka", 9.0)
m2 = Movie("KGF", "Yash", "Srinidhi", 8.8)

print("Movie 1:", m1.movie_name, m1.hero, m1.heroine, m1.rating)
print("Movie 2:", m2.movie_name, m2.hero, m2.heroine, m2.rating)
"""),
    ("set2_01_student_class.Py", """class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

students = [
    Student("Asha", 18, "BCA"),
    Student("Kiran", 20, "BSc"),
    Student("Meena", 19, "MBA")
]

for student in students:
    print(student.name, student.age, student.course)
"""),
    ("set2_02_employee_class.Py", """class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employees = [
    Employee("Naveen", "HR", 30000),
    Employee("Priya", "IT", 45000),
    Employee("Suresh", "Sales", 35000),
    Employee("Anu", "Finance", 50000),
    Employee("Raju", "Support", 28000)
]

for emp in employees:
    print(emp.name, emp.department, emp.salary)
"""),
    ("set2_03_product_class.Py", """class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

p1 = Product("Pen", 20, 5)
p2 = Product("Book", 150, 3)

print("Total price of Pen:", p1.total_price())
print("Total price of Book:", p2.total_price())
"""),
    ("set2_04_car_class.Py", """class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

cars = [
    Car("Tesla", "Model 3", 2023, 4500000),
    Car("BMW", "X5", 2022, 7000000),
    Car("Audi", "A4", 2021, 5000000)
]

for car in cars:
    print(car.brand, car.model, car.year, car.price)
"""),
    ("set2_05_person_class.Py", """class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

p1 = Person("Anil", 25, "Pune")
p2 = Person("Sita", 30, "Delhi")

print("Person 1:", p1.name, p1.age, p1.city)
print("Person 2:", p2.name, p2.age, p2.city)
"""),
    ("set2_06_book_class.Py", """class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

books = [
    Book("C Programming", "Dennis", 250, 300),
    Book("Java", "James", 400, 500),
    Book("Python", "Guido", 350, 430)
]

for book in books:
    print(book.title, book.author, book.price, book.pages)
"""),
    ("set2_07_laptop_class.Py", """class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptops = [
    Laptop("HP", "8GB", "512GB", 42000),
    Laptop("Lenovo", "16GB", "1TB", 65000),
    Laptop("Asus", "32GB", "1TB", 85000)
]

for laptop in laptops:
    print(laptop.brand, laptop.ram, laptop.storage, laptop.price)
"""),
    ("set2_08_bankaccount_class.Py", """class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

acc1 = BankAccount("Kavya", 101, 5000)
acc2 = BankAccount("Vikram", 102, 7000)

print("Account 1:", acc1.account_holder, acc1.account_number, acc1.balance)
print("Account 2:", acc2.account_holder, acc2.account_number, acc2.balance)
"""),
    ("set2_09_teacher_class.Py", """class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

teachers = [
    Teacher("Mrs. Rao", "Math", 12),
    Teacher("Mr. Kumar", "Physics", 8),
    Teacher("Mrs. Devi", "English", 10)
]

for teacher in teachers:
    print(teacher.name, teacher.subject, teacher.experience)
"""),
    ("set2_10_hospital_class.Py", """class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

p1 = Hospital("Arun", 28, "Fever", "Dr. Ghosh")
p2 = Hospital("Neha", 35, "Cold", "Dr. Singh")
p3 = Hospital("Ritu", 42, "Migraine", "Dr. Kapoor")

for patient in [p1, p2, p3]:
    print(patient.patient_name, patient.age, patient.disease, patient.doctor_name)
"""),
    ("set3_01_student_classvariable.Py", """class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Sneha")
s3 = Student("Deepak")

print(s1.name, Student.college_name)
print(s2.name, Student.college_name)
print(s3.name, Student.college_name)
"""),
    ("set3_02_employee_classvariable.Py", """class Employee:
    company_name = "TechWorld"

    def __init__(self, name):
        self.name = name

emp1 = Employee("Amit")
emp2 = Employee("Neha")

print(emp1.name, Employee.company_name)
print(emp2.name, Employee.company_name)
"""),
    ("set3_03_car_classvariable.Py", """class Car:
    number_of_wheels = 4

    def __init__(self, brand):
        self.brand = brand

c1 = Car("Audi")
c2 = Car("BMW")

print(c1.brand, c1.number_of_wheels)
print(c2.brand, Car.number_of_wheels)
"""),
    ("set3_04_bankaccount_classvariable.Py", """class BankAccount:
    bank_name = "SBI"

    def __init__(self, account_holder):
        self.account_holder = account_holder

acc1 = BankAccount("Asha")
acc2 = BankAccount("Vikram")

print(acc1.account_holder, BankAccount.bank_name)
print(acc2.account_holder, BankAccount.bank_name)
"""),
    ("set3_05_product_classvariable.Py", """class Product:
    category = "Electronics"

    def __init__(self, name):
        self.name = name

p1 = Product("Mobile")
p2 = Product("Laptop")

print(p1.name, Product.category)
print(p2.name, Product.category)
"""),
    ("set3_06_object_counter.Py", """class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")

print("Total students:", Student.count)
"""),
    ("set3_07_student_class_and_instance.Py", """class Student:
    college_name = "Global College"

    def __init__(self, name):
        self.name = name

s1 = Student("Riya")
s2 = Student("Rohit")

print(s1.name, Student.college_name)
print(s2.name, Student.college_name)
"""),
    ("set3_08_employee_classvariables.Py", """class Employee:
    company_name = "Infosys"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

emp1 = Employee("Sunita")
emp2 = Employee("Ramesh")

print(Employee.company_name)
print(Employee.employee_count)
"""),
    ("set3_09_car_classvariables.Py", """class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

c1 = Car("Corolla", 1800000)
c2 = Car("Innova", 2200000)

print(c1.model, c1.price, Car.company, Car.number_of_wheels)
print(c2.model, c2.price, Car.company, Car.number_of_wheels)
"""),
    ("set3_10_course_classvariable.Py", """class Course:
    institute_name = "SkillHub"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

c1 = Course("Python", "3 months")
c2 = Course("Java", "4 months")

print(c1.course_name, c1.duration, Course.institute_name)
print(c2.course_name, c2.duration, Course.institute_name)
"""),
    ("set4_01_student_display_method.Py", """class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

s = Student("Amit", 20, "BCA")
s.display()
"""),
    ("set4_02_employee_display_salary.Py", """class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(self.name, "salary is", self.salary)

emp = Employee("Rohit", 50000)
emp.display_salary()
"""),
    ("set4_03_calculator_methods.Py", """class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

c = Calculator()
print("Addition:", c.add(10, 5))
print("Subtraction:", c.subtract(10, 5))
print("Multiplication:", c.multiply(10, 5))
print("Division:", c.divide(10, 5))
"""),
    ("set4_04_rectangle_methods.Py", """class Rectangle:
    def area(self, length, width):
        return length * width

    def perimeter(self, length, width):
        return 2 * (length + width)

r = Rectangle()
print("Area:", r.area(5, 4))
print("Perimeter:", r.perimeter(5, 4))
"""),
    ("set4_05_circle_methods.Py", """class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius * radius

    def circumference(self, radius):
        return 2 * self.pi * radius

c = Circle()
print("Area:", c.area(7))
print("Circumference:", c.circumference(7))
"""),
    ("set4_06_bankaccount_methods.Py", """class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Remaining balance:", acc.balance)
"""),
    ("set4_07_car_methods.Py", """class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "started")

    def stop(self):
        print(self.brand, self.model, "stopped")

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car = Car("Honda", "City")
car.start()
car.display_details()
car.stop()
"""),
    ("set4_08_student_marks_methods.Py", """class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total_marks(self):
        return self.marks1 + self.marks2 + self.marks3

    def average_marks(self):
        return self.total_marks() / 3

s = Student(80, 90, 85)
print("Total marks:", s.total_marks())
print("Average marks:", s.average_marks())
"""),
    ("set4_09_employee_annual_salary.Py", """class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp = Employee(45000)
print("Annual salary:", emp.annual_salary())
"""),
    ("set4_10_product_total_cost.Py", """class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

p = Product(200, 5)
print("Total cost:", p.total_cost())
"""),
    ("set5_01_student_init.Py", """class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

s = Student("Riya", 19, "BCA", 88)
print("Name:", s.name)
print("Age:", s.age)
print("Course:", s.course)
print("Marks:", s.marks)
"""),
    ("set5_02_employee_init.Py", """class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

emp = Employee(101, "Nisha", "HR", 42000)
print("Employee ID:", emp.emp_id)
print("Name:", emp.name)
print("Department:", emp.department)
print("Salary:", emp.salary)
"""),
    ("set5_03_book_init_display.Py", """class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book = Book("Python", "Guido", 450)
book.display()
"""),
    ("set5_04_car_init_methods.Py", """class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "started")

    def stop(self):
        print(self.brand, self.model, "stopped")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car = Car("Ford", "EcoSport")
car.start()
car.display()
car.stop()
"""),
    ("set5_05_bankaccount_init.Py", """class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

acc = BankAccount("Rina", 987654321, 2500)
print("Account Holder:", acc.account_holder)
print("Account Number:", acc.account_number)
print("Balance:", acc.balance)
"""),
    ("set5_06_product_init_totalprice.Py", """class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

p = Product("Mouse", 500, 3)
print("Total price:", p.total_price())
"""),
    ("set5_07_student_grade.Py", """class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

s = Student("Anita", 82)
print(s.name, "got grade", s.calculate_grade())
"""),
    ("set5_08_movie_init_display.Py", """class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

    def display(self):
        print("Movie:", self.movie_name)
        print("Hero:", self.hero)
        print("Heroine:", self.heroine)
        print("Rating:", self.rating)

m = Movie("3 Idiots", "Aamir Khan", "Kareena", 8.9)
m.display()
"""),
    ("set5_09_laptop_init_display.Py", """class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)

laptop = Laptop("HP", "16GB", "512GB", 60000)
laptop.display()
"""),
    ("set5_10_hospitalpatient_init.Py", """class HospitalPatient:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

    def display(self):
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor:", self.doctor_name)

p = HospitalPatient("Harish", 32, "Asthma", "Dr. Pawan")
p.display()
"""),
    ("set6_01_calculator_parameter_methods.Py", """class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

c = Calculator()
print(c.add(7, 3))
print(c.subtract(7, 3))
print(c.multiply(7, 3))
print(c.divide(7, 3))
"""),
    ("set6_02_student_grade_method.Py", """class Student:
    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "D"

s = Student()
print(s.grade(80))
"""),
    ("set6_03_rectangle_area_method.Py", """class Rectangle:
    def area(self, length, width):
        return length * width

r = Rectangle()
print(r.area(10, 5))
"""),
    ("set6_04_bankaccount_deposit_method.Py", """class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        return self.balance

acc = BankAccount()
print(acc.deposit(500))
"""),
    ("set6_05_product_total_price_method.Py", """class Product:
    def total_price(self, price, quantity):
        return price * quantity

p = Product()
print(p.total_price(200, 4))
"""),
    ("set6_06_employee_salary_method.Py", """class Employee:
    def salary(self, working_days):
        return working_days * 500

emp = Employee()
print(emp.salary(22))
"""),
    ("set6_07_number_methods.Py", """class Number:
    def is_even(self, n):
        return n % 2 == 0

    def is_odd(self, n):
        return n % 2 != 0

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_palindrome(self, n):
        original = n
        reverse = 0
        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10
        return reverse == original

num = Number()
print(num.is_even(8))
print(num.is_odd(7))
print(num.is_prime(11))
print(num.is_palindrome(121))
"""),
    ("set6_08_string_operations.Py", """class StringOperations:
    def reverse(self, text):
        return text[::-1]

    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for ch in text:
            if ch in vowels:
                count += 1
        return count

    def is_palindrome(self, text):
        return text == text[::-1]

s = StringOperations()
print(s.reverse("python"))
print(s.count_vowels("hello"))
print(s.is_palindrome("madam"))
"""),
    ("set6_09_shopping_cart.Py", """class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def total(self):
        return sum(self.items)

cart = ShoppingCart()
cart.add_product(100)
cart.add_product(200)
print(cart.total())
cart.remove_product(100)
print(cart.total())
"""),
    ("set6_10_temperature.Py", """class Temperature:
    def c_to_f(self, c):
        return (c * 9 / 5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5 / 9

obj = Temperature()
print(obj.c_to_f(30))
print(obj.f_to_c(86))
"""),
    ("set7_01_class_and_instance_variables.Py", """class Example:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

obj1 = Example("Sam")
obj2 = Example("John")

print(obj1.name)
print(obj1.college_name)
print(obj2.name)
print(Example.college_name)
"""),
    ("set7_02_multiple_instance_methods.Py", """class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

    def show(self):
        self.greet()

s = Student("Asha")
s.show()
"""),
    ("set7_03_method_returns_object_info.Py", """class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def info(self):
        return self.name + " studies " + self.course

class School:
    def __init__(self, student):
        self.student = student

    def display_student(self):
        print(self.student.info())

s = Student("Divya", "BCA")
school = School(s)
school.display_student()
"""),
    ("set7_04_student_object_counter.Py", """class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")
print("Total students created:", Student.count)
"""),
    ("set7_05_employee_annual_salary.Py", """class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp = Employee(60000)
print(emp.annual_salary())
"""),
    ("set7_06_bankaccount_insufficient_balance.Py", """class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

acc = BankAccount(500)
acc.withdraw(700)
"""),
    ("set7_07_librarybook_issue_return.Py", """class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued")
        else:
            print(self.title, "already issued")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned")
        else:
            print(self.title, "not issued")

book = LibraryBook("Python Basics")
book.issue()
book.return_book()
"""),
    ("set7_08_shoppingcart_multiple_products.Py", """class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_bill(self):
        total = 0
        for item in self.products:
            total += item
        return total

cart = ShoppingCart()
cart.add_product(200)
cart.add_product(150)
cart.add_product(100)
print("Total bill:", cart.total_bill())
"""),
    ("set7_09_course_enrolled_students.Py", """class Course:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def display_students(self):
        for name in self.students:
            print(name)

course = Course()
course.add_student("Asha")
course.add_student("Ravi")
course.add_student("Neha")
course.display_students()
"""),
    ("set7_10_company_employees.Py", """class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print(name, "removed")
        else:
            print(name, "not found")

    def search_employee(self, name):
        if name in self.employees:
            print(name, "found")
        else:
            print(name, "not found")

    def display_employees(self):
        for name in self.employees:
            print(name)

company = Company()
company.add_employee("Anu")
company.add_employee("Bhavya")
company.display_employees()
company.search_employee("Anu")
company.remove_employee("Bhavya")
""")
]

for filename, content in items:
    path = base / filename
    path.write_text(content, encoding="utf-8")

print(f"Created {len(items)} files in {base}")

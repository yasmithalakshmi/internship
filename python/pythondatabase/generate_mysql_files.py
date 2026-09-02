from pathlib import Path

base = Path(r"c:\Users\yasmitha\OneDrive\internship\python\pythondatabase")
base.mkdir(parents=True, exist_ok=True)

files = [
    {
        "filename": "mysql_create_college_db.Py",
        "question": "1. Create a MySQL database named college_db using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\"\n)\n\ncursor = mydb.cursor()\ncursor.execute(\"CREATE DATABASE IF NOT EXISTS college_db\")\nprint(\"Database college_db created successfully.\")\n"
    },
    {
        "filename": "mysql_create_students_table.Py",
        "question": "2. Create a table named students with columns id, name, age, course, and marks.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nquery = '''\nCREATE TABLE IF NOT EXISTS students (\n    id INT AUTO_INCREMENT PRIMARY KEY,\n    name VARCHAR(100),\n    age INT,\n    course VARCHAR(100),\n    marks INT\n)\n'''\n\ncursor.execute(query)\nprint(\"Table students created successfully.\")\n"
    },
    {
        "filename": "mysql_connect_success_message.Py",
        "question": "3. Connect Python to a MySQL database and display a successful connection message.",
        "code": "import mysql.connector\n\ntry:\n    mydb = mysql.connector.connect(\n        host=\"localhost\",\n        user=\"root\",\n        password=\"your_password\",\n        database=\"college_db\"\n    )\n    print(\"Connected to MySQL database successfully!\")\nexcept mysql.connector.Error as e:\n    print(\"Connection failed:\", e)\n"
    },
    {
        "filename": "mysql_insert_one_student.Py",
        "question": "4. Insert one student record into the students table using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nsql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\nvalues = (\"Alice\", 20, \"BCA\", 88)\n\ncursor.execute(sql, values)\nmydb.commit()\nprint(\"1 student record inserted successfully.\")\n"
    },
    {
        "filename": "mysql_insert_five_students.Py",
        "question": "5. Insert five student records into the students table using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nrecords = [\n    (\"Asha\", 18, \"BCA\", 82),\n    (\"Ravi\", 19, \"BCA\", 90),\n    (\"Meena\", 20, \"BSc\", 74),\n    (\"Kiran\", 21, \"MBA\", 85),\n    (\"Anu\", 22, \"MCA\", 92)\n]\n\nsql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\ncursor.executemany(sql, records)\nmydb.commit()\nprint(\"5 student records inserted successfully.\")\n"
    },
    {
        "filename": "mysql_display_all_students.Py",
        "question": "6. Retrieve and display all student records using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\ncursor.execute(\"SELECT * FROM students\")\nrows = cursor.fetchall()\n\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_display_student_names.Py",
        "question": "7. Retrieve and display only student names from the database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\ncursor.execute(\"SELECT name FROM students\")\nrows = cursor.fetchall()\n\nfor name in rows:\n    print(name[0])\n"
    },
    {
        "filename": "mysql_students_marks_gt_75.Py",
        "question": "8. Retrieve students whose marks are greater than 75.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nquery = \"SELECT * FROM students WHERE marks > 75\"\ncursor.execute(query)\nrows = cursor.fetchall()\n\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_students_specific_course.Py",
        "question": "9. Retrieve students belonging to a particular course.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\ncourse_name = \"BCA\"\nquery = \"SELECT * FROM students WHERE course = %s\"\ncursor.execute(query, (course_name,))\nrows = cursor.fetchall()\n\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_total_students_count.Py",
        "question": "10. Display the total number of students stored in the database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\ncursor.execute(\"SELECT COUNT(*) FROM students\")\ncount = cursor.fetchone()[0]\nprint(\"Total students:\", count)\n"
    },
    {
        "filename": "mysql_insert_new_student.Py",
        "question": "1. Write a Python program to insert a new student into the database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nname = \"Sonia\"\nage = 23\ncourse = \"MCA\"\nmarks = 91\n\nsql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\nvalues = (name, age, course, marks)\ncursor.execute(sql, values)\nmydb.commit()\nprint(\"Student inserted successfully.\")\n"
    },
    {
        "filename": "mysql_update_student_name.Py",
        "question": "2. Write a Python program to update a student's name.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nstudent_id = 1\nnew_name = \"Priya\"\nquery = \"UPDATE students SET name = %s WHERE id = %s\"\ncursor.execute(query, (new_name, student_id))\nmydb.commit()\nprint(\"Student name updated successfully.\")\n"
    },
    {
        "filename": "mysql_update_student_marks.Py",
        "question": "3. Write a Python program to update a student's marks.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nstudent_id = 2\nnew_marks = 95\nquery = \"UPDATE students SET marks = %s WHERE id = %s\"\ncursor.execute(query, (new_marks, student_id))\nmydb.commit()\nprint(\"Marks updated successfully.\")\n"
    },
    {
        "filename": "mysql_update_student_course.Py",
        "question": "4. Write a Python program to update a student's course.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nstudent_id = 3\nnew_course = \"BSc\"\nquery = \"UPDATE students SET course = %s WHERE id = %s\"\ncursor.execute(query, (new_course, student_id))\nmydb.commit()\nprint(\"Course updated successfully.\")\n"
    },
    {
        "filename": "mysql_delete_student_by_id.Py",
        "question": "5. Write a Python program to delete a student using their ID.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nstudent_id = 4\nquery = \"DELETE FROM students WHERE id = %s\"\ncursor.execute(query, (student_id,))\nmydb.commit()\nprint(\"Student deleted successfully.\")\n"
    },
    {
        "filename": "mysql_search_student_by_id.Py",
        "question": "6. Write a Python program to search for a student using their ID.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nstudent_id = 1\nquery = \"SELECT * FROM students WHERE id = %s\"\ncursor.execute(query, (student_id,))\nrow = cursor.fetchone()\nprint(row)\n"
    },
    {
        "filename": "mysql_search_students_by_name.Py",
        "question": "7. Write a Python program to search for students using their name.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nname = \"Asha\"\nquery = \"SELECT * FROM students WHERE name = %s\"\ncursor.execute(query, (name,))\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_students_marks_between_50_80.Py",
        "question": "8. Write a Python program to display students whose marks are between 50 and 80.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM students WHERE marks BETWEEN 50 AND 80\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_students_desc_order_marks.Py",
        "question": "9. Write a Python program to display students in descending order of marks.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM students ORDER BY marks DESC\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_top_5_students_by_marks.Py",
        "question": "10. Write a Python program to display the top 5 students based on marks.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM students ORDER BY marks DESC LIMIT 5\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_insert_student_from_user.Py",
        "question": "1. Accept student details from the user and insert them into the database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nname = input(\"Enter student name: \")\nage = int(input(\"Enter age: \") )\ncourse = input(\"Enter course: \")\nmarks = int(input(\"Enter marks: \") )\n\nsql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\nvalues = (name, age, course, marks)\ncursor.execute(sql, values)\nmydb.commit()\nprint(\"Student inserted successfully.\")\n"
    },
    {
        "filename": "mysql_display_student_by_id_input.Py",
        "question": "2. Accept a student ID from the user and display that student's details.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nstudent_id = int(input(\"Enter student ID: \") )\nquery = \"SELECT * FROM students WHERE id = %s\"\ncursor.execute(query, (student_id,))\nrow = cursor.fetchone()\nprint(row)\n"
    },
    {
        "filename": "mysql_update_marks_by_id_input.Py",
        "question": "3. Accept a student ID and new marks from the user and update the database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nstudent_id = int(input(\"Enter student ID: \") )\nnew_marks = int(input(\"Enter new marks: \") )\nquery = \"UPDATE students SET marks = %s WHERE id = %s\"\ncursor.execute(query, (new_marks, student_id))\nmydb.commit()\nprint(\"Marks updated successfully.\")\n"
    },
    {
        "filename": "mysql_delete_student_by_id_input.Py",
        "question": "4. Accept a student ID from the user and delete the student record.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nstudent_id = int(input(\"Enter student ID to delete: \") )\nquery = \"DELETE FROM students WHERE id = %s\"\ncursor.execute(query, (student_id,))\nmydb.commit()\nprint(\"Student deleted successfully.\")\n"
    },
    {
        "filename": "mysql_display_students_by_course_input.Py",
        "question": "5. Accept a course name from the user and display all students in that course.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\ncourse_name = input(\"Enter course name: \")\nquery = \"SELECT * FROM students WHERE course = %s\"\ncursor.execute(query, (course_name,))\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_display_students_by_mark_range_input.Py",
        "question": "6. Accept minimum and maximum marks from the user and display matching students.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nmin_marks = int(input(\"Enter minimum marks: \") )\nmax_marks = int(input(\"Enter maximum marks: \") )\nquery = \"SELECT * FROM students WHERE marks BETWEEN %s AND %s\"\ncursor.execute(query, (min_marks, max_marks))\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_search_student_by_name_input.Py",
        "question": "7. Accept a student name from the user and search for the student.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nname = input(\"Enter student name: \")\nquery = \"SELECT * FROM students WHERE name = %s\"\ncursor.execute(query, (name,))\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_insert_employee_from_user.Py",
        "question": "8. Accept employee details from the user and insert them into an employees table.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nname = input(\"Enter employee name: \")\ndepartment = input(\"Enter department: \")\nsalary = float(input(\"Enter salary: \") )\njoining_date = input(\"Enter joining date (YYYY-MM-DD): \")\n\nquery = \"INSERT INTO employees (name, department, salary, joining_date) VALUES (%s, %s, %s, %s)\"\nvalues = (name, department, salary, joining_date)\ncursor.execute(query, values)\nmydb.commit()\nprint(\"Employee inserted successfully.\")\n"
    },
    {
        "filename": "mysql_display_product_by_id_input.Py",
        "question": "9. Accept a product ID from the user and display product information.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nproduct_id = int(input(\"Enter product ID: \") )\nquery = \"SELECT * FROM products WHERE id = %s\"\ncursor.execute(query, (product_id,))\nrow = cursor.fetchone()\nprint(row)\n"
    },
    {
        "filename": "mysql_menu_driven_crud.Py",
        "question": "10. Create a menu-driven program that allows users to perform database CRUD operations.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nwhile True:\n    print(\"\\n1. Insert Student\")\n    print(\"2. View Students\")\n    print(\"3. Update Student\")\n    print(\"4. Delete Student\")\n    print(\"5. Exit\")\n    choice = input(\"Enter your choice: \")\n\n    if choice == '1':\n        name = input(\"Enter name: \")\n        age = int(input(\"Enter age: \"))\n        course = input(\"Enter course: \")\n        marks = int(input(\"Enter marks: \"))\n        sql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\n        cursor.execute(sql, (name, age, course, marks))\n        mydb.commit()\n        print(\"Student added.\")\n    elif choice == '2':\n        cursor.execute(\"SELECT * FROM students\")\n        for row in cursor.fetchall():\n            print(row)\n    elif choice == '3':\n        print(\"Update operation selected.\")\n    elif choice == '4':\n        print(\"Delete operation selected.\")\n    elif choice == '5':\n        break\n    else:\n        print(\"Invalid option\")\n"
    },
    {
        "filename": "mysql_create_employees_table.Py",
        "question": "1. Create a table employees with employee ID, name, department, salary, and joining date.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nquery = '''\nCREATE TABLE IF NOT EXISTS employees (\n    employee_id INT AUTO_INCREMENT PRIMARY KEY,\n    name VARCHAR(100),\n    department VARCHAR(100),\n    salary DECIMAL(10,2),\n    joining_date DATE\n)\n'''\n\ncursor.execute(query)\nprint(\"Table employees created successfully.\")\n"
    },
    {
        "filename": "mysql_insert_10_employees.Py",
        "question": "2. Insert 10 employee records into the employees table using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nrecords = [\n    (\"Rahul\", \"IT\", 52000, \"2021-01-10\"),\n    (\"Priya\", \"HR\", 48000, \"2020-05-15\"),\n    (\"Karan\", \"IT\", 61000, \"2022-07-11\"),\n    (\"Sunita\", \"Finance\", 55000, \"2021-09-20\"),\n    (\"Javed\", \"Sales\", 43000, \"2023-02-15\"),\n    (\"Aditi\", \"IT\", 67000, \"2021-11-13\"),\n    (\"Ramesh\", \"Support\", 50000, \"2019-04-21\"),\n    (\"Neha\", \"Marketing\", 39000, \"2022-08-22\"),\n    (\"Vikram\", \"IT\", 71000, \"2020-12-09\"),\n    (\"Maya\", \"HR\", 47000, \"2021-06-18\")\n]\n\nquery = \"INSERT INTO employees (name, department, salary, joining_date) VALUES (%s, %s, %s, %s)\"\ncursor.executemany(query, records)\nmydb.commit()\nprint(\"10 employee records inserted successfully.\")\n"
    },
    {
        "filename": "mysql_employees_salary_gt_50000.Py",
        "question": "3. Display employees whose salary is greater than ₹50,000.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM employees WHERE salary > 50000\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_employees_it_department.Py",
        "question": "4. Display employees belonging to the IT department.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM employees WHERE department = 'IT'\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_employees_sorted_by_salary_asc.Py",
        "question": "5. Display employees sorted by salary in ascending order.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM employees ORDER BY salary ASC\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_employees_sorted_by_salary_desc.Py",
        "question": "6. Display employees sorted by salary in descending order.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT * FROM employees ORDER BY salary DESC\"\ncursor.execute(query)\nrows = cursor.fetchall()\nfor row in rows:\n    print(row)\n"
    },
    {
        "filename": "mysql_highest_employee_salary.Py",
        "question": "7. Find the highest employee salary.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT MAX(salary) FROM employees\"\ncursor.execute(query)\nprint(cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_lowest_employee_salary.Py",
        "question": "8. Find the lowest employee salary.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT MIN(salary) FROM employees\"\ncursor.execute(query)\nprint(cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_average_employee_salary.Py",
        "question": "9. Calculate the average employee salary.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT AVG(salary) FROM employees\"\ncursor.execute(query)\nprint(cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_total_company_salary.Py",
        "question": "10. Calculate the total salary paid by the company.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT SUM(salary) FROM employees\"\ncursor.execute(query)\nprint(cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_students_courses_relationship.Py",
        "question": "1. Create students and courses tables and establish a relationship between them.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\ncreate_courses = '''\nCREATE TABLE IF NOT EXISTS courses (\n    course_id INT AUTO_INCREMENT PRIMARY KEY,\n    course_name VARCHAR(100)\n)\n'''\ncreate_students = '''\nCREATE TABLE IF NOT EXISTS students (\n    id INT AUTO_INCREMENT PRIMARY KEY,\n    name VARCHAR(100),\n    course_id INT,\n    FOREIGN KEY (course_id) REFERENCES courses(course_id)\n)\n'''\n\ncursor.execute(create_courses)\ncursor.execute(create_students)\nprint(\"Students and courses tables created with relationship.\")\n"
    },
    {
        "filename": "mysql_customers_orders_relationship.Py",
        "question": "2. Create customers and orders tables and establish a relationship using foreign keys.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nquery1 = '''CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))'''\nquery2 = '''CREATE TABLE IF NOT EXISTS orders (order_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, amount DECIMAL(10,2), FOREIGN KEY (customer_id) REFERENCES customers(id))'''\n\ncursor.execute(query1)\ncursor.execute(query2)\nprint(\"Customer-order relationship created.\")\n"
    },
    {
        "filename": "mysql_employee_department_join.Py",
        "question": "3. Create employees and departments tables and retrieve employee department names using JOIN.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = '''\nSELECT e.name, d.department_name\nFROM employees e\nJOIN departments d ON e.department_id = d.department_id\n'''\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_college_management_relations.Py",
        "question": "4. Create students, courses, and enrollments tables for a college management system.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nqueries = [\n    \"CREATE TABLE IF NOT EXISTS courses (course_id INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(100))\",\n    \"CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), course_id INT)\",\n    \"CREATE TABLE IF NOT EXISTS enrollments (enrollment_id INT AUTO_INCREMENT PRIMARY KEY, student_id INT, course_id INT)\"\n]\nfor query in queries:\n    cursor.execute(query)\nprint(\"College management tables created.\")\n"
    },
    {
        "filename": "mysql_join_students_course_names.Py",
        "question": "5. Retrieve students along with their course names using JOIN.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = '''\nSELECT s.name, c.course_name\nFROM students s\nJOIN courses c ON s.course_id = c.course_id\n'''\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_join_customers_orders.Py",
        "question": "6. Retrieve customers along with their orders using JOIN.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = '''\nSELECT c.name, o.order_id, o.amount\nFROM customers c\nJOIN orders o ON c.id = o.customer_id\n'''\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_join_employees_departments.Py",
        "question": "7. Display employees along with their department names.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = '''\nSELECT e.name, d.department_name\nFROM employees e\nJOIN departments d ON e.department_id = d.department_id\n'''\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_departments_without_employees.Py",
        "question": "8. Find departments that have no employees.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = '''\nSELECT d.department_name\nFROM departments d\nLEFT JOIN employees e ON d.department_id = e.department_id\nWHERE e.employee_id IS NULL\n'''\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_total_records_in_table.Py",
        "question": "1. Write a Python program to calculate the total number of records in a table.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT COUNT(*) FROM students\"\ncursor.execute(query)\nprint(\"Total records:\", cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_average_marks_students.Py",
        "question": "2. Write a Python program to calculate the average marks of students.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT AVG(marks) FROM students\"\ncursor.execute(query)\nprint(\"Average marks:\", cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_highest_marks_student.Py",
        "question": "3. Write a Python program to find the highest marks.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT MAX(marks) FROM students\"\ncursor.execute(query)\nprint(\"Highest marks:\", cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_lowest_marks_student.Py",
        "question": "4. Write a Python program to find the lowest marks.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT MIN(marks) FROM students\"\ncursor.execute(query)\nprint(\"Lowest marks:\", cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_total_sales_orders.Py",
        "question": "5. Write a Python program to calculate the total sales from an orders table.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT SUM(amount) FROM orders\"\ncursor.execute(query)\nprint(\"Total sales:\", cursor.fetchone()[0])\n"
    },
    {
        "filename": "mysql_total_sales_each_customer.Py",
        "question": "6. Write a Python program to calculate total sales for each customer.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id\"\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_average_salary_each_department.Py",
        "question": "7. Write a Python program to calculate average salary for each department.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT department, AVG(salary) FROM employees GROUP BY department\"\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_count_students_each_course.Py",
        "question": "8. Write a Python program to count students in each course.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"SELECT course, COUNT(*) FROM students GROUP BY course\"\ncursor.execute(query)\nfor row in cursor.fetchall():\n    print(row)\n"
    },
    {
        "filename": "mysql_bank_account_deposit_withdraw.Py",
        "question": "1. Create a bank account table and perform deposit and withdrawal operations using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\n\nquery = '''\nCREATE TABLE IF NOT EXISTS bank_accounts (\n    account_id INT AUTO_INCREMENT PRIMARY KEY,\n    account_holder VARCHAR(100),\n    balance DECIMAL(10,2)\n)\n'''\ncursor.execute(query)\nprint(\"Bank account table ready.\")\n"
    },
    {
        "filename": "mysql_bank_account_transfer_transaction.Py",
        "question": "2. Implement a money transfer between two bank accounts using a database transaction.",
        "code": "import mysql.connector\nfrom mysql.connector import Error\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ntry:\n    cursor = mydb.cursor()\n    mydb.start_transaction()\n    cursor.execute(\"UPDATE bank_accounts SET balance = balance - 500 WHERE account_id = 1\")\n    cursor.execute(\"UPDATE bank_accounts SET balance = balance + 500 WHERE account_id = 2\")\n    mydb.commit()\n    print(\"Transaction successful.\")\nexcept Error as e:\n    mydb.rollback()\n    print(\"Transaction failed:\", e)\n"
    },
    {
        "filename": "mysql_commit_rollback_demo.Py",
        "question": "3. Demonstrate commit() and rollback() using a Python database program.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\ntry:\n    cursor.execute(\"INSERT INTO students (name, age, course, marks) VALUES ('Test', 20, 'BCA', 70)\")\n    mydb.commit()\n    print(\"Commit successful.\")\nexcept Exception as e:\n    mydb.rollback()\n    print(\"Rollback done:\", e)\n"
    },
    {
        "filename": "mysql_order_transaction_stock_update.Py",
        "question": "4. Create an order system and use transactions while creating an order and updating product stock.",
        "code": "import mysql.connector\nfrom mysql.connector import Error\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ntry:\n    cursor = mydb.cursor()\n    mydb.start_transaction()\n    cursor.execute(\"INSERT INTO orders (customer_id, total_amount) VALUES (1, 2500)\")\n    cursor.execute(\"UPDATE products SET quantity = quantity - 1 WHERE id = 10\")\n    mydb.commit()\n    print(\"Order placed and stock updated.\")\nexcept Error as e:\n    mydb.rollback()\n    print(\"Transaction failed:\", e)\n"
    },
    {
        "filename": "mysql_transaction_rollback_on_error.Py",
        "question": "5. Write a program that rolls back a transaction when an error occurs.",
        "code": "import mysql.connector\nfrom mysql.connector import Error\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ntry:\n    cursor = mydb.cursor()\n    mydb.start_transaction()\n    cursor.execute(\"INSERT INTO students (name, age, course, marks) VALUES ('Bad', 20, 'BCA', 100)\")\n    raise ValueError(\"Sample error\")\nexcept Exception as e:\n    mydb.rollback()\n    print(\"Rollback because of error:\", e)\n"
    },
    {
        "filename": "mysql_create_backup_table.Py",
        "question": "6. Create a database backup table using Python.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"CREATE TABLE IF NOT EXISTS students_backup LIKE students\"\ncursor.execute(query)\nprint(\"Backup table created.\")\n"
    },
    {
        "filename": "mysql_copy_records_between_tables.Py",
        "question": "7. Write a program to copy records from one table to another.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"INSERT INTO students_backup SELECT * FROM students\"\ncursor.execute(query)\nmydb.commit()\nprint(\"Records copied successfully.\")\n"
    },
    {
        "filename": "mysql_delete_multiple_records.Py",
        "question": "8. Write a program to delete multiple records based on a condition.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nquery = \"DELETE FROM students WHERE marks < 40\"\ncursor.execute(query)\nmydb.commit()\nprint(\"Records deleted successfully.\")\n"
    },
    {
        "filename": "mysql_function_add_student.Py",
        "question": "1. Create a function add_student() to insert a student into the database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef add_student(name, age, course, marks):\n    cursor = mydb.cursor()\n    sql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\n    cursor.execute(sql, (name, age, course, marks))\n    mydb.commit()\n    print(\"Student added.\")\n\nadd_student(\"Pooja\", 22, \"BCA\", 87)\n"
    },
    {
        "filename": "mysql_function_get_students.Py",
        "question": "2. Create a function get_students() to retrieve all students.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef get_students():\n    cursor = mydb.cursor()\n    cursor.execute(\"SELECT * FROM students\")\n    return cursor.fetchall()\n\nfor student in get_students():\n    print(student)\n"
    },
    {
        "filename": "mysql_function_search_student.Py",
        "question": "3. Create a function search_student() to search students by ID or name.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef search_student(value):\n    cursor = mydb.cursor()\n    query = \"SELECT * FROM students WHERE id = %s OR name = %s\"\n    cursor.execute(query, (value, value))\n    return cursor.fetchall()\n\nprint(search_student(1))\n"
    },
    {
        "filename": "mysql_function_update_student.Py",
        "question": "4. Create a function update_student() to update student details.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef update_student(student_id, new_name, new_course):\n    cursor = mydb.cursor()\n    query = \"UPDATE students SET name = %s, course = %s WHERE id = %s\"\n    cursor.execute(query, (new_name, new_course, student_id))\n    mydb.commit()\n    print(\"Student updated.\")\n\nupdate_student(1, \"Rita\", \"MCA\")\n"
    },
    {
        "filename": "mysql_function_delete_student.Py",
        "question": "5. Create a function delete_student() to delete a student.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef delete_student(student_id):\n    cursor = mydb.cursor()\n    query = \"DELETE FROM students WHERE id = %s\"\n    cursor.execute(query, (student_id,))\n    mydb.commit()\n    print(\"Student deleted.\")\n\ndelete_student(5)\n"
    },
    {
        "filename": "mysql_employee_crud_functions.Py",
        "question": "6. Create an employee management program using separate functions for all CRUD operations.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef add_employee(name, department, salary):\n    cursor = mydb.cursor()\n    cursor.execute(\"INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)\", (name, department, salary))\n    mydb.commit()\n\ndef get_employees():\n    cursor = mydb.cursor()\n    cursor.execute(\"SELECT * FROM employees\")\n    return cursor.fetchall()\n\nadd_employee(\"Nisha\", \"HR\", 45000)\nfor emp in get_employees():\n    print(emp)\n"
    },
    {
        "filename": "mysql_product_management_functions.Py",
        "question": "7. Create a product management program using functions and a database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef add_product(name, price, quantity):\n    cursor = mydb.cursor()\n    cursor.execute(\"INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)\", (name, price, quantity))\n    mydb.commit()\n\nadd_product(\"Laptop\", 45000, 4)\nprint(\"Product added.\")\n"
    },
    {
        "filename": "mysql_customer_management_functions.Py",
        "question": "8. Create a customer management program using functions and a database.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ndef add_customer(name, email):\n    cursor = mydb.cursor()\n    cursor.execute(\"INSERT INTO customers (name, email) VALUES (%s, %s)\", (name, email))\n    mydb.commit()\n\nadd_customer(\"Riya\", \"riya@gmail.com\")\nprint(\"Customer added.\")\n"
    },
    {
        "filename": "mysql_student_class_crud.Py",
        "question": "1. Create a Student class with methods to insert, update, delete, and retrieve student records.",
        "code": "import mysql.connector\n\nclass Student:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def insert_student(self, name, age, course, marks):\n        sql = \"INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)\"\n        self.cursor.execute(sql, (name, age, course, marks))\n        self.mydb.commit()\n        print(\"Student inserted.\")\n\n    def get_students(self):\n        self.cursor.execute(\"SELECT * FROM students\")\n        return self.cursor.fetchall()\n\nstudent = Student()\nstudent.insert_student(\"Tina\", 24, \"BCA\", 81)\nprint(student.get_students())\n"
    },
    {
        "filename": "mysql_employee_class_crud.Py",
        "question": "2. Create an Employee class that performs CRUD operations using a database.",
        "code": "import mysql.connector\n\nclass Employee:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def add_employee(self, name, department, salary):\n        sql = \"INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)\"\n        self.cursor.execute(sql, (name, department, salary))\n        self.mydb.commit()\n        print(\"Employee added.\")\n\nemp = Employee()\nemp.add_employee(\"Naveen\", \"IT\", 56000)\n"
    },
    {
        "filename": "mysql_product_class_crud.Py",
        "question": "3. Create a Product class with methods for adding, updating, deleting, and searching products.",
        "code": "import mysql.connector\n\nclass Product:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def add_product(self, name, price, quantity):\n        sql = \"INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)\"\n        self.cursor.execute(sql, (name, price, quantity))\n        self.mydb.commit()\n\nproduct = Product()\nproduct.add_product(\"Mouse\", 700, 10)\nprint(\"Product added.\")\n"
    },
    {
        "filename": "mysql_customer_class_crud.Py",
        "question": "4. Create a Customer class with database operations.",
        "code": "import mysql.connector\n\nclass Customer:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def add_customer(self, name, email):\n        sql = \"INSERT INTO customers (name, email) VALUES (%s, %s)\"\n        self.cursor.execute(sql, (name, email))\n        self.mydb.commit()\n\ncustomer = Customer()\ncustomer.add_customer(\"Aman\", \"aman@gmail.com\")\nprint(\"Customer added.\")\n"
    },
    {
        "filename": "mysql_order_class_crud.Py",
        "question": "5. Create an Order class that stores and retrieves order information.",
        "code": "import mysql.connector\n\nclass Order:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def add_order(self, customer_id, total_amount):\n        sql = \"INSERT INTO orders (customer_id, total_amount) VALUES (%s, %s)\"\n        self.cursor.execute(sql, (customer_id, total_amount))\n        self.mydb.commit()\n\norder = Order()\norder.add_order(1, 2500)\nprint(\"Order added.\")\n"
    },
    {
        "filename": "mysql_bankaccount_class_db.Py",
        "question": "6. Create a BankAccount class connected to a database for storing account details and transactions.",
        "code": "import mysql.connector\n\nclass BankAccount:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def add_account(self, holder_name, balance):\n        sql = \"INSERT INTO bank_accounts (account_holder, balance) VALUES (%s, %s)\"\n        self.cursor.execute(sql, (holder_name, balance))\n        self.mydb.commit()\n\naccount = BankAccount()\naccount.add_account(\"Rahul\", 2500)\nprint(\"Account created.\")\n"
    },
    {
        "filename": "mysql_librarybook_class_db.Py",
        "question": "7. Create a LibraryBook class that stores book information in a database.",
        "code": "import mysql.connector\n\nclass LibraryBook:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def add_book(self, title, author):\n        sql = \"INSERT INTO books (title, author) VALUES (%s, %s)\"\n        self.cursor.execute(sql, (title, author))\n        self.mydb.commit()\n\nbook = LibraryBook()\nbook.add_book(\"Python Basics\", \"John\")\nprint(\"Book added.\")\n"
    },
    {
        "filename": "mysql_library_class_db.Py",
        "question": "8. Create a Library class with methods to issue and return books using database records.",
        "code": "import mysql.connector\n\nclass Library:\n    def __init__(self):\n        self.mydb = mysql.connector.connect(\n            host=\"localhost\",\n            user=\"root\",\n            password=\"your_password\",\n            database=\"college_db\"\n        )\n        self.cursor = self.mydb.cursor()\n\n    def issue_book(self, book_id, student_name):\n        print(\"Book issued to\", student_name)\n\n    def return_book(self, book_id):\n        print(\"Book returned.\")\n\nlib = Library()\nlib.issue_book(1, \"Asha\")\n"
    },
    {
        "filename": "mysql_student_management_database.Py",
        "question": "1. Create a Student Management Database with students, courses, and enrollments tables.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nqueries = [\n    \"CREATE TABLE IF NOT EXISTS courses (course_id INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(100))\",\n    \"CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), course_id INT)\",\n    \"CREATE TABLE IF NOT EXISTS enrollments (enrollment_id INT AUTO_INCREMENT PRIMARY KEY, student_id INT, course_id INT)\"\n]\nfor query in queries:\n    cursor.execute(query)\nprint(\"Student management database ready.\")\n"
    },
    {
        "filename": "mysql_employee_management_database.Py",
        "question": "2. Create an Employee Management Database with employees, departments, and salaries tables.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nqueries = [\n    \"CREATE TABLE IF NOT EXISTS departments (department_id INT AUTO_INCREMENT PRIMARY KEY, department_name VARCHAR(100))\",\n    \"CREATE TABLE IF NOT EXISTS employees (employee_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), department_id INT, salary DECIMAL(10,2))\",\n    \"CREATE TABLE IF NOT EXISTS salaries (salary_id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, amount DECIMAL(10,2))\"\n]\nfor query in queries:\n    cursor.execute(query)\nprint(\"Employee management database ready.\")\n"
    },
    {
        "filename": "mysql_ecommerce_database.Py",
        "question": "3. Create an E-Commerce Database with customers, products, orders, and order items tables.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nqueries = [\n    \"CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))\",\n    \"CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2), quantity INT)\",\n    \"CREATE TABLE IF NOT EXISTS orders (order_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, total_amount DECIMAL(10,2))\",\n    \"CREATE TABLE IF NOT EXISTS order_items (item_id INT AUTO_INCREMENT PRIMARY KEY, order_id INT, product_id INT, quantity INT)\"\n]\nfor query in queries:\n    cursor.execute(query)\nprint(\"E-commerce database ready.\")\n"
    },
    {
        "filename": "mysql_banking_database.Py",
        "question": "4. Create a Banking Database with customers, accounts, transactions, and branches tables.",
        "code": "import mysql.connector\n\nmydb = mysql.connector.connect(\n    host=\"localhost\",\n    user=\"root\",\n    password=\"your_password\",\n    database=\"college_db\"\n)\n\ncursor = mydb.cursor()\nqueries = [\n    \"CREATE TABLE IF NOT EXISTS customers (customer_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))\",\n    \"CREATE TABLE IF NOT EXISTS accounts (account_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, balance DECIMAL(10,2))\",\n    \"CREATE TABLE IF NOT EXISTS transactions (transaction_id INT AUTO_INCREMENT PRIMARY KEY, account_id INT, amount DECIMAL(10,2), type VARCHAR(20))\",\n    \"CREATE TABLE IF NOT EXISTS branches (branch_id INT AUTO_INCREMENT PRIMARY KEY, branch_name VARCHAR(100))\"\n]\nfor query in queries:\n    cursor.execute(query)\nprint(\"Banking database ready.\")\n"
    }
]

for item in files:
    path = base / item["filename"]
    content = f"# {item['question']}\n\n{item['code']}\n"
    path.write_text(content, encoding='utf-8')

print(f"Created {len(files)} files in {base}")

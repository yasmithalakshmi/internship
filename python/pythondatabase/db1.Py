import sqlite3

# Connect to the database
conn = sqlite3.connect("emp.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp2 (
        emp_id INTEGER,
        emp_name TEXT,
        emp_phn_no INTEGER,
        dept TEXT,
        salary INTEGER
    )
""")

# Insert sample data
employee_data = [
    (101, 'yashu', 1234567890, 'IT', 50000),
    (102, 'anu', 6677889900, 'HR', 45000),
    (103, 'teju', 1122334455, 'IT', 60000),
    (104, 'manu', 9988776655, 'Sales', 55000),
    (105, 'roo', 8877665544, 'HR', 47000),
    (106, 'abhi', 7766554433, 'IT', 65000)
]

# Insert into the same table used above
cursor.executemany(
    """INSERT INTO emp2 (emp_id, emp_name, emp_phn_no, dept, salary)
    VALUES (?, ?, ?, ?, ?)""",
    employee_data
)

conn.commit()

print("1. WHERE CLAUSE")
cursor.execute("SELECT * FROM emp2 WHERE dept = 'IT'")
for row in cursor.fetchall():
    print(row)

print("\n2. ORDER BY CLAUSE")
cursor.execute("SELECT * FROM emp2 ORDER BY salary DESC")
for row in cursor.fetchall():
    print(row)

print("\n3. GROUP BY CLAUSE")
cursor.execute("SELECT dept, COUNT(*) AS total_employees FROM emp2 GROUP BY dept")
for row in cursor.fetchall():
    print(row)

print("\n4. AGGREGATIONS")
cursor.execute("SELECT COUNT(*) AS total_emp, SUM(salary) AS total_salary, AVG(salary) AS avg_salary, MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM emp2")
for row in cursor.fetchall():
    print(row)

print("\n5. WHERE + ORDER BY")
cursor.execute("SELECT * FROM emp2 WHERE salary > 50000 ORDER BY salary")
for row in cursor.fetchall():
    print(row)

conn.close()
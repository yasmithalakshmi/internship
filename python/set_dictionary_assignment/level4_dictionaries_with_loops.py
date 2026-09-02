# Level 4: Dictionaries with Loops
# Write Python code for all the questions below.

# 1. Create a dictionary of student marks and print students who scored above 75.
# 2. Create a dictionary of numbers and count how many values are even and odd.
# 3. Create a dictionary containing employee names and salaries. Display employees earning more than ₹50,000.
# 4. Create a dictionary containing product names and quantities. Display products with quantity less than 10.
# 5. Create a dictionary and calculate the total of all numeric values without using sum().
# 6. Create a dictionary of words and their meanings. Ask the user for a word and display its meaning.
# 7. Create a dictionary containing 5 students and their marks. Display the topper and lowest scorer.
# 8. Create a dictionary and count the frequency of each character in a given string.
# 9. Create a dictionary and count the frequency of each word in a sentence.
# 10. Create a dictionary from two lists: one containing keys and another containing values.

# Solutions
marks = {"Asha": 80, "Bharat": 70, "Chitra": 95, "David": 60, "Esha": 82}
above_75 = {name: mark for name, mark in marks.items() if mark > 75}
print("1. Students above 75:", above_75)

number_values = {"a": 2, "b": 7, "c": 8, "d": 13, "e": 4}
count_even = 0
count_odd = 0
for value in number_values.values():
    if value % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("2. Even values:", count_even, "Odd values:", count_odd)

employees = {"Alice": 55000, "Bob": 47000, "Charlie": 62000, "Dina": 36000}
high_salary = {name: salary for name, salary in employees.items() if salary > 50000}
print("3. Employees earning more than 50,000:", high_salary)

products_qty = {"Pen": 8, "Notebook": 15, "A4 Paper": 6, "Marker": 20}
low_stock = {product: qty for product, qty in products_qty.items() if qty < 10}
print("4. Products with quantity less than 10:", low_stock)

dict_total = {"a": 10, "b": 20, "c": 30, "d": 40}
total = 0
for value in dict_total.values():
    total += value
print("5. Total of values:", total)

words = {"apple": "A fruit", "python": "A programming language", "chair": "A seat"}
search_word = "python"
print("6. Meaning of python:", words.get(search_word, "Word not found"))

student_marks_2 = {"Asha": 88, "Bharat": 72, "Chitra": 94, "David": 68, "Esha": 80}
topper_name = ""
topper_mark = -1
low_name = ""
low_mark = 101
for name, mark in student_marks_2.items():
    if mark > topper_mark:
        topper_mark = mark
        topper_name = name
    if mark < low_mark:
        low_mark = mark
        low_name = name
print("7. Topper:", topper_name, topper_mark)
print("7. Lowest scorer:", low_name, low_mark)

char_string = "programming"
char_freq = {}
for ch in char_string:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print("8. Character frequency:", char_freq)

sentence = "python is easy and python is fun"
words_list = sentence.split()
word_freq = {}
for w in words_list:
    word_freq[w] = word_freq.get(w, 0) + 1
print("9. Word frequency:", word_freq)

keys = ["name", "age", "course"]
values = ["Aditi", 21, "Java"]
merged_dict = dict(zip(keys, values))
print("10. Dictionary from two lists:", merged_dict)

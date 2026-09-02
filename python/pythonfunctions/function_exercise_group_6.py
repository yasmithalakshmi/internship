# Function practice group 6

def min_max_list(numbers):
    return min(numbers), max(numbers)


def sum_tuple(values):
    total = 0
    for value in values:
        total += value
    return total


def unique_count(my_set):
    return len(my_set)


def topper_name(student_marks):
    top_student = ""
    top_mark = -1
    for student, marks in student_marks.items():
        if marks > top_mark:
            top_student = student
            top_mark = marks
    return top_student


def keys_value_greater_50(data):
    result = []
    for key, value in data.items():
        if value > 50:
            result.append(key)
    return result


def sorted_names(names):
    return sorted(names)


def count_even_odd(numbers):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return {"even": even, "odd": odd}


def char_frequency(text):
    frequency = {}
    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency


def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def square_dictionary(numbers):
    result = {}
    for num in numbers:
        result[num] = num * num
    return result


print("Min and max:", min_max_list([10, 25, 6, 18]))
print("Tuple sum:", sum_tuple((2, 4, 6, 8)))
print("Unique count:", unique_count({1, 2, 2, 3, 4}))
print("Topper:", topper_name({"Asha": 88, "Ravi": 92, "Meena": 80}))
print("Above 50:", keys_value_greater_50({"Math": 78, "Science": 60, "English": 45}))
print("Sorted names:", sorted_names(["Riya", "Asha", "Kiran", "Meena"]))
print("Even and odd:", count_even_odd([1, 2, 3, 4, 5, 6]))
print("Character count:", char_frequency("hello"))
print("Word count:", word_frequency("hello world hello"))
print("Square dict:", square_dictionary([1, 2, 3, 4]))

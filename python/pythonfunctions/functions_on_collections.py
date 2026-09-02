# 6. Functions on Lists, Tuples, Sets, and Dictionaries

# 1. Minimum and maximum in a list

def min_max_list(numbers):
    return min(numbers), max(numbers)


# 2. Sum of tuple

def sum_tuple(values):
    total = 0
    for value in values:
        total += value
    return total


# 3. Number of unique elements in a set

def unique_count(my_set):
    return len(my_set)


# 4. Topper from dictionary

def topper_name(student_marks):
    top_student = ""
    top_mark = -1
    for name, marks in student_marks.items():
        if marks > top_mark:
            top_student = name
            top_mark = marks
    return top_student


# 5. Keys with values greater than 50

def keys_greater_than_50(data):
    result = []
    for key, value in data.items():
        if value > 50:
            result.append(key)
    return result


# 6. Sort names alphabetically

def sort_names(names):
    return sorted(names)


# 7. Count even and odd numbers

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {"even": even_count, "odd": odd_count}


# 8. Character frequency in a string

def char_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


# 9. Word frequency in a sentence

def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# 10. Number and square dictionary

def number_square_dict(numbers):
    result = {}
    for num in numbers:
        result[num] = num * num
    return result


print(min_max_list([12, 5, 9, 18, 3]))
print(sum_tuple((2, 4, 6, 8)))
print(unique_count({1, 2, 2, 3, 4}))
print(topper_name({"Asha": 88, "Ravi": 92, "Meena": 80}))
print(keys_greater_than_50({"Math": 70, "Science": 60, "English": 40}))
print(sort_names(["Riya", "Asha", "Kiran", "Neha"]))
print(count_even_odd([1, 2, 3, 4, 5, 6, 7, 8]))
print(char_frequency("python"))
print(word_frequency("hello world hello"))
print(number_square_dict([1, 2, 3, 4]))

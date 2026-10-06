#1. Install NumPy and import it using the alias np.
import numpy as np
#2. Create a NumPy array from the list [10, 20, 30, 40, 50].
arr1 = np.array([10,20,30,40,50])
#3. Print the type of a NumPy array.
print(type(arr1))
#4. Print the data type (dtype) of an array.
print(arr1.dtype)
#5. Find the number of dimensions of an array using ndim.
print(arr1.ndim)
#6. Find the shape of a 1D array.
print(arr1.shape)
#7. Find the total number of elements using size.
print(arr1.size)
#8. Create an array containing numbers from 1 to 10.
arr2 = np.arange(1, 11)
print(arr2)
#9. Create an array of ten zeros.
arr3 = np.zeros(10)
print(arr3)
#10. Create an array of ten ones.
arr4 = np.ones(10)
print(arr4)
#11. Create an array containing five 7s.
arr5 = np.full(5, 7)
print(arr5)
#12. Create an array containing numbers from 0 to 20 using arange().
arr6 = np.arange(21)
print(arr6)
#13. Create an array of even numbers from 2 to 20.
arr7 = np.arange(2, 21, 2)
print(arr7)
#14. Create an array of odd numbers from 1 to 19.
arr8 = np.arange(1, 20, 2)
print(arr8)
#15. Create five equally spaced numbers between 0 and 1 using linspace().
arr9 = np.linspace(0, 1, 5)
print(arr9)
#16. Create a 3×3 matrix containing zeros.
arr10 = np.zeros((3, 3))
print(arr10)
#17. Create a 3×3 matrix containing ones.
arr11 = np.ones((3, 3))
print(arr11)
#18. Create a 4×4 identity matrix.
arr12 = np.eye(4)
print(arr12)
#19. Create a 2D array from a nested Python list.
arr13 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr13)
#20. Access the first element of a NumPy array.
print(arr13[0, 0])
#21. Access the last element using negative indexing.
print(arr13[-1, -1])
#22. Access the second row of a 2D array.
print(arr13[1, :])
#23. Access the third column of a 2D array.
print(arr13[:, 2])
#24. Use slicing to extract the first three elements.
print(arr6[0:3])
#25. Reverse a NumPy array using slicing.
print(arr6[::-1])
#26. Add two NumPy arrays element by element.
arr14 =np.array([1, 2, 3])
arr15 = np.array([4, 5, 6])
arr16 = arr14 + arr15
print(arr16)
#27. Subtract two NumPy arrays element by element.
arr17 = arr15 - arr14
print(arr17)
#28. Multiply two NumPy arrays element by element.
arr18 = arr14 * arr15
print(arr18)
#29. Divide two NumPy arrays element by element.
arr19 = arr15 / arr14
print(arr19)
#30. Calculate the square of every array element.
arr20 = arr14 ** 2
print(arr20)
#31. Calculate the cube of every array element.
arr21 = arr14 ** 3
print(arr21)
#32. Find the sum of all elements.
print(np.sum(arr14))
#33. Find the mean of an array.
print(np.mean(arr14))
#34. Find the median of an array.
print(np.median(arr14))
#35. Find the minimum value.
print(np.min(arr14))
#36. Find the maximum value.
print(np.max(arr14))
#37. Find the standard deviation.
print(np.std(arr14))
#38. Find the variance.
print(np.var(arr14))
#39. Find the cumulative sum.
print(np.cumsum(arr14))
#40. Find the cumulative product.
print(np.cumprod(arr14))
#41. Calculate the absolute value of negative numbers.
arr22 = np.array([-1, -2, -3])
print(np.abs(arr22))
#42. Round floating-point values to two decimal places.
arr23 = np.array([1.12345, 2.6789, 3.14159])
print(np.round(arr23, 2))
#43. Find the index of the maximum value using argmax().
print(np.argmax(arr14))
#44. Find the index of the minimum value using argmin().
print(np.argmin(arr14))
#45. Count values greater than 50.
arr24 = np.array([55, 60, 45, 70, 80])
print(np.count_nonzero(arr24 > 50))
#46. Count even numbers in an array.
print(np.count_nonzero(arr2 % 2 == 0))
#47. Find all numbers divisible by 5.
print(arr24[arr24 % 5 == 0])
#48. Replace all negative values with 0.
arr25 = np.array([-1, 2, -3, 4, -5])
arr25[arr25 < 0] = 0
print(arr25)
#49. Replace all values greater than 100 with 100.
arr26 = np.array([50, 150, 200, 75])
arr26[arr26 > 100] = 100
print(arr26)
#50. Calculate the percentage contribution of each value to the total.
total = np.sum(arr24)
percentage_contribution = (arr24 / total) * 100
print(percentage_contribution)


#LEVEL 3


#51. Reshape an array of 12 elements into a 3×4 matrix.
arr27 = np.arange(12)
reshaped_arr = arr27.reshape(3, 4)
print(reshaped_arr)
#52. Reshape an array of 16 elements into a 4×4 matrix.
arr28 = np.arange(16)
reshaped_arr2 = arr28.reshape(4, 4)
print(reshaped_arr2)
#53. Convert a 2D array into a 1D array using flatten().
flatten_arr = arr28.flatten()
print(flatten_arr)
#54. Convert a 2D array into a 1D array using ravel().
ravel_arr = arr28.ravel()
print(ravel_arr)
#55. Transpose a 2D matrix.
transposed_arr = arr28.reshape(4, 4).T
print(transposed_arr)
#56. Swap the first and last rows of a matrix.
swapped_arr = arr28.reshape(4, 4)
print("Before swapping:\n", swapped_arr)
swapped_arr[[0, -1]] = swapped_arr[[-1, 0]]
print("After swapping:\n", swapped_arr)
#57. Swap the first and last columns of a matrix.
swapped_arr2 = arr28.reshape(4, 4)
print("Before swapping:\n", swapped_arr2)
swapped_arr2[:, [0, -1]] = swapped_arr2[:, [-1, 0]]
print("After swapping:\n", swapped_arr2)
#58. Extract a 2×2 sub-matrix from a 4×4 matrix.
sub_matrix = arr28.reshape(4, 4)[1:3, 1:3]
print(sub_matrix)
#59. Extract all elements from the second row onward.
second_row_onward = arr28.reshape(4, 4)[1:4, :]
print(second_row_onward)
#60. Extract all elements from the third column onward.
third_column_onward = arr28.reshape(4, 4)[:, 2:4]
print(third_column_onward)
#61. Use boolean indexing to find values greater than 50.
greater_than_50 = arr24[arr24 > 50]
print(greater_than_50)
#62. Use boolean indexing to find values between 20 and 80.
between_20_and_80 = arr24[(arr24 > 20) & (arr24 < 80)]
print(between_20_and_80)
#63. Find all even values using boolean indexing.
even_values = arr24[arr24 % 2 == 0]
print(even_values)
#64. Find all odd values using boolean indexing.
odd_values = arr24[arr24 % 2 != 0]
print(odd_values)
#65. Replace even values with 0 using boolean indexing.
arr_replace_even = arr24.copy()
arr_replace_even[arr_replace_even % 2 == 0] = 0
print(arr_replace_even)
#66. Replace values below the mean with the mean.
arr_mean = np.array([5, 1, 8, 3, 9])
arr_mean[arr_mean < np.mean(arr_mean)] = np.mean(arr_mean)
print(arr_mean)
#67. Sort a NumPy array.
sorted_array = np.sort(arr24)
print(sorted_array)
#68. Sort each row of a 2D array.
arr_2d = np.array([[5, 2, 9], [1, 7, 3]])
sorted_rows = np.sort(arr_2d, axis=1)
print(sorted_rows)
#69. Sort each column of a 2D array.
sorted_columns = np.sort(arr_2d, axis=0)
print(sorted_columns)
#70. Find unique values in an array.
unique_values = np.unique(arr24)
print(unique_values)
#71. Concatenate two NumPy arrays using concatenate().
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
concatenated_array = np.concatenate((arr_a, arr_b))
print(concatenated_array)
#72. Stack two arrays vertically using vstack().
arr_c = np.array([1, 2, 3])
arr_d = np.array([4, 5, 6])
vertical_stack = np.vstack((arr_c, arr_d))
print(vertical_stack)
#73. Stack two arrays horizontally using hstack().
horizontal_stack = np.hstack((arr_c, arr_d))
print(horizontal_stack)
#74. Split an array into three equal parts.
arr_split = np.array([1, 2, 3, 4, 5, 6])
part1, part2, part3 = np.split(arr_split, 3)
print(part1, part2, part3)
#75. Split a 2D matrix into two vertical sections.
mat_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
left, right = np.hsplit(mat_2d, 2)
print(left)
print(right)
#76. Split a 2D matrix into two horizontal sections.
upper, lower = np.vsplit(mat_2d, 2)
print(upper)
print(lower)
#77. Perform matrix addition on two 3×3 matrices.
mat_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix_sum = mat_a + mat_b
print(matrix_sum)
#78. Perform matrix multiplication on two matrices.
matrix_product = np.dot(mat_a, mat_b)
print(matrix_product)
#79. Calculate the transpose of a matrix and verify its shape.
transposed_matrix = mat_a.T
print(transposed_matrix)
print(transposed_matrix.shape)
#80. Calculate the determinant of a 2×2 matrix using np.linalg.det().
mat_det = np.array([[4, 3], [2, 1]])
determinant = np.linalg.det(mat_det)
print(determinant)
#81. Calculate the inverse of a matrix using np.linalg.inv().
mat_inv = np.array([[2, 1], [1, 3]])
inverse_matrix = np.linalg.inv(mat_inv)
print(inverse_matrix)
#82. Solve a system of linear equations using np.linalg.solve().
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
solution = np.linalg.solve(A, b)
print(solution)
#83. Calculate dot product of two vectors.
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
dot_product = np.dot(vec1, vec2)
print(dot_product)
#84. Calculate the Euclidean norm of a vector.
vector = np.array([3, 4])
vector_norm = np.linalg.norm(vector)
print(vector_norm)
#85. Normalize an array so its values range from 0 to 1.
arr_norm = np.array([10, 20, 30, 40, 50])
arr_norm_normalized = (arr_norm - arr_norm.min()) / (arr_norm.max() - arr_norm.min())
print(arr_norm_normalized)
#86. Find the second-largest unique value in a NumPy array.
arr_second = np.array([5, 7, 3, 9, 7, 2, 9])
unique_second = np.unique(arr_second)
second_largest_unique = unique_second[-2]
print(second_largest_unique)
#87. Find the third-largest value without sorting the entire array.
arr_third = np.array([12, 5, 9, 17, 3, 15])
third_largest = np.partition(arr_third, -3)[-3]
print(third_largest)
#88. Find duplicate values in a NumPy array.
arr_dup = np.array([1, 2, 2, 3, 4, 4, 5])
unique_dup, counts_dup = np.unique(arr_dup, return_counts=True)
duplicate_values = unique_dup[counts_dup > 1]
print(duplicate_values)
#89. Find values that occur exactly once.
unique_once, counts_once = np.unique(arr_dup, return_counts=True)
values_once = unique_once[counts_once == 1]
print(values_once)
#90. Find the frequency of every unique value.
unique_freq, freq_counts = np.unique(arr_dup, return_counts=True)
print(unique_freq)
print(freq_counts)
#91. Find the row with the highest sum in a 2D array.
matrix_rows = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_sums = matrix_rows.sum(axis=1)
row_with_highest_sum = np.argmax(row_sums)
print(row_with_highest_sum)
#92. Find the column with the lowest average in a 2D array.
col_averages = matrix_rows.mean(axis=0)
col_with_lowest_avg = np.argmin(col_averages)
print(col_with_lowest_avg)
#93. Find the top 3 values and their indexes.
arr_top3 = np.array([8, 2, 9, 4, 7, 1])
top3_indexes = np.argsort(arr_top3)[::-1][:3]
print(top3_indexes)
print(arr_top3[top3_indexes])
#94. Find all values that are above the array's mean.
arr_above_mean = np.array([3, 5, 8, 2, 7, 1])
above_mean_values = arr_above_mean[arr_above_mean > np.mean(arr_above_mean)]
print(above_mean_values)
#95. Find the percentage of missing values represented by NaN.
arr_nan = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
missing_percentage = np.mean(np.isnan(arr_nan)) * 100
print(missing_percentage)
#96. Replace NaN values with the mean of the array.
arr_nan_fill = arr_nan.copy()
arr_nan_fill[np.isnan(arr_nan_fill)] = np.nanmean(arr_nan_fill)
print(arr_nan_fill)
#97. Remove rows containing NaN values from a 2D array.
arr_2d_nan = np.array([[1.0, 2.0], [np.nan, 4.0], [5.0, 6.0], [7.0, np.nan]])
clean_matrix = arr_2d_nan[~np.isnan(arr_2d_nan).any(axis=1)]
print(clean_matrix)
#98. Calculate row-wise and column-wise mean for a matrix.
matrix_mean = np.array([[1, 2, 3], [4, 5, 6]])
row_means = matrix_mean.mean(axis=1)
col_means = matrix_mean.mean(axis=0)
print(row_means)
print(col_means)
#99. Create a 10×10 random matrix and find its minimum, maximum, mean, and standard deviation.
random_matrix = np.random.rand(10, 10)
print(random_matrix.min())
print(random_matrix.max())
print(random_matrix.mean())
print(random_matrix.std())
#100. Final Challenge: Build a NumPy Student Marks Analyzer. Given a 2D array of student marks, calculate total marks, average marks, highest and lowest scorer, subject-wise average, pass/fail count, grades, rank, and students above the class average.
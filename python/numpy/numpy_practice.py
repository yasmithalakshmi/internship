import numpy as np
#1. Create a NumPy array containing numbers from 1 to 10.
arr = np.arange(1,11)
#2. Create a 1D array containing:
arr1 = np.array([10,20,30,40,50])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
#3. Create a 2D array with 3 rows and 3 columns.
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.size)
#4. Create a 3D NumPy array and check its shape and dimensions.
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(arr3)
print(arr3.ndim)
print(arr3.shape)
#5. Create an array of 10 zeros.
arr_zero = np.zeros(10)
print(arr_zero)
## Create a 3 × 4 array filled with ones.
arr_ones = np.ones((3,4))
print(arr_ones)
#7. Create a 4 × 4 identity matrix.
arr_identity = np.eye((4))
print(arr_identity)
#8. Create numbers from 0 to 20 using arange().
arr_range = np.arange(21)
print(arr_range)
#9. Create even numbers from 0 to 20.
arr_even = np.arange(0,21,2)
print(arr_even)
#10. Create odd numbers from 0 to 20.
arr_odd = np.arange(1,21,2)
print(arr_odd)

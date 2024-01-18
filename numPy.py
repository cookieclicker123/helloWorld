import numpy as np

# Create a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

# Create a 2D NumPy array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array (Matrix):\n", matrix)

# Basic array operations
print("Array addition:", arr + 2)
print("Array multiplication:", arr * 2)

# Array slicing
print("Sliced array:", arr[1:4])

# Reshape a 1D array to a 2D array
reshaped = arr.reshape((1, 5))
print("Reshaped to 2D array:\n", reshaped)

# Linear algebra - Dot product of two arrays
dot_product = np.dot(arr, arr)
print("Dot product:", dot_product)

dotProduct2 = np.dot(matrix, matrix)
print("Dot product:", dotProduct2)

# Generate random data
random_data = np.random.random((3, 3))
print("Random 3x3 matrix:\n", random_data)
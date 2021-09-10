# numpy used to create arrays, arrays are more performant than lists
# Basic Array commands/navigation
import numpy as np
# 1D array
a = np.array([1, 2, 3])
print(a)
print("=======")

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print("=======")

# Get Dimension
print(a.ndim)

# Get Shape
print(b.shape)

# Get a specific element [r, c] (index starts at 0)
print(b[1, 2])  # prints 6
print(b[0, 1])  # prints 2
print(b[1, 0])  # prints 4

# Get a specific row
print("=======")
print(b[0, :])
print("=======")
print(b[1, :])
print("=======")

# Get a specific column
print("=======")
print(b[:, 0])
print("=======")
print(b[:, 1])
print("=======")
print(b[:, 2])
print("=======")

# make array of size specified fill with number value
print("=======")
print(np.full((4, 4), 0))
print("=======")
# math with array elements
print("=======")
print(a)
print(a + 5)
print(a * 2)
print(np.sin(a))
print(np.cos(a))
print("=======")

# Statistics
print("=======")
print(np.min(b))
print(np.min(b, axis=0))  # smallest value found in respective columns
print(np.min(b, axis=1))  # smallest value found in respective rows
print(np.min(b))          # smallest value

print(np.max(b, axis=0))  # largest value found in respective columns
print(np.max(b, axis=1))  # largest value found in respective rows
print(np.max(b))          # smallest value

print(np.sum(b, axis=0))  # sum of rows
print(np.sum(b, axis=1))  # sum of columns
print(np.sum(b))          # sum of values
print("=======")

# Also has math functions that are used in advanced calculus
# https://numpy.org/doc/stable/numpy-ref.pdf

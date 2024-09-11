import numpy as np

# Define matrix 'a' and vector 'b'
a = np.array([[52, 30, 18],
              [20,  50, 30],
              [25,  20,  55]])

b = np.array([4800, 5810, 5690])

# Calculate the inverse of matrix 'a'
a_inv = np.linalg.inv(a)

# Solve for 'x' using the inverse of 'a' and vector 'b'
x = np.dot(a_inv, b)

# Output the results
print("Matrix a inverse:\n", a_inv)
print("\nSolution x:\n", x)

# This code takes user input as the number of rows and columns of a matrix,
# and then takes the matrix elements as input.
# It then converts the matrix into a numpy array and performs transpose and flatten operations.
# Finally, it prints the transpose and flattened array.

# Import the numpy library
import numpy as np

# Take user input as the number of rows and columns of a matrix
n , m = list(map(int , input().strip().split()))

# Initialize an empty list to store the matrix elements
l = []

# Loop through the rows of the matrix and take the input for each row
for i in range(n):
    l.append(list(map(int , input().strip().split())))

# Convert the list of lists to a numpy array
l = np.array(l)

# Transpose the numpy array and print it
print(l.T)

# Flatten the numpy array and print it
print(l.flatten())

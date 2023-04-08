# This code takes user input as space-separated integers, 
# converts them into a list of integers, 
# and then converts the list into a 3x3 numpy array using the reshape() method. 
# Finally, it prints the numpy array.

# Import the numpy library
import numpy as np

# Take user input as space-separated integers, convert them to a list of integers
my_list = list(map(int,input().strip().split()))

# Convert the list of integers to a numpy array
my_array = np.array(my_list)

# Reshape the 1D numpy array into a 3x3 matrix
my_array = np.reshape(my_array,(3,3))

# Print the 3x3 numpy array
print(my_array)

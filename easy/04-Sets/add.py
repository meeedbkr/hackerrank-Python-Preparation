# Prompt user for input
n = int(input())  # number of strings to read

# Create an empty set to store the strings
set_ = set()

# Loop over the input and add each string to the set
for i in range(n):
    set_.add(input())

# Print the size of the set
print(len(set_))

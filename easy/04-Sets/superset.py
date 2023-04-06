# Enter your code here. Read input from STDIN. Print output to STDOUT
# This line reads input from user, split it by spaces, 
# converts each element to integer and creates a set of integers.
a = set(map(int, input().split()))

# This line reads a single integer as input from the user and assigns it to the variable "n".
n = int(input())

# Initializes the counter variable "nn" to zero.
nn = 0

# Loop through the range n.
for _ in range(n):
    # This line reads input from user, split it by spaces, 
    # converts each element to integer and creates a set of integers.
    m = set(map(int, input().split()))

    # This line checks if set "a" is a superset of set "m".
    # If so, increment the counter variable "nn".
    if a.issuperset(m):
        nn += 1

# This line checks if the total number of sets processed equals the number of sets that are subsets of set "a".
# If so, it prints "True". Otherwise, it prints "False".
print(n == nn)


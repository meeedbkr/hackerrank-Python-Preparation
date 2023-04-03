# Prompt user for input
M = int(input())  # size of first set
a = set(map(int, input().split()))  # elements of first set
N = int(input())  # size of second set
b = set(map(int, input().split()))  # elements of second set

# Calculate symmetric difference of the two sets
diff = a.symmetric_difference(b)

# Convert the result to a sorted list
diff = list(diff)
diff.sort()

# Print the elements of the symmetric difference in sorted order
for i in diff:
    print(i)

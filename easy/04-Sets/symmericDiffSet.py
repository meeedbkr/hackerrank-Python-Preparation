# Enter your code here. Read input from STDIN. Print output to STDOUT
# This line reads a single integer as input from the user and assigns it to the variable "n".
n = int(input())

# This line reads input from the user, splits it by spaces, 
# converts each element to integer and creates a set of integers "s1".
s1 = set(map(int, input().split()))

# This line reads a single integer as input from the user and assigns it to the variable "n2".
n2 = int(input())

# This line reads input from the user, splits it by spaces, 
# converts each element to integer and creates a set of integers "s2".
s2 = set(map(int, input().split()))

# This line finds the symmetric difference of the two sets "s1" and "s2",
# which is the set of elements that are in either "s1" or "s2" but not in both.
# It then prints the length of the symmetric difference set.
print(len(s1.symmetric_difference(s2)))



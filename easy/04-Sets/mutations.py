# Enter your code here. Read input from STDIN. Print output to STDOUT
# This line reads a single integer as input from the user and assigns it to the variable "ns".
ns = int(input())

# This line reads input from the user, splits it by spaces, 
# converts each element to integer and creates a set of integers "s".
s = set(map(int, input().split()))

# This line reads a single integer as input from the user and assigns it to the variable "n".
n = int(input())

# This loop runs "n" times and performs different set operations on the set "s" based on the input commands.
for _ in range(n):

    # This line reads a command as input from the user, splits it by spaces, and assigns the parts to variables "op" and "ns".
    op = input().strip().split()
    ns = int(op[1])

    # If the command is "intersection_update", the code finds the intersection of set "s" with a new set,
    # which is created from the input values after the command, and updates the original set "s" with the intersection.
    elif op[0] == 'intersection_update':
        s.intersection_update(set(map(int, input().split())))

    # If the command is "update", the code updates the set "s" with the input values after the command.
    elif op[0] == 'update':
        s.update(set(map(int, input().split())))

    # If the command is "symmetric_difference_update", the code finds the symmetric difference of set "s" with a new set,
    # which is created from the input values after the command, and updates the original set "s" with the symmetric difference.
    elif op[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(set(map(int, input().split())))

    # If the command is "difference_update", the code finds the difference of set "s" with a new set,
    # which is created from the input values after the command, and updates the original set "s" with the difference.
    elif op[0] == 'difference_update':
        s.difference_update(set(map(int, input().split())))

# This line prints the sum of all the elements in the updated set "s".
print(sum(s))



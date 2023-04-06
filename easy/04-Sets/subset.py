# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of test cases
n = int(input())

# Loop over each test case
for _ in range(n):
    # Read the number of elements in the first set
    n1 = int(input())

    # Read the elements of the first set
    s1 = set(map(int, input().split()))

    # Read the number of elements in the second set
    n2 = int(input())

    # Read the elements of the second set
    s2 = set(map(int, input().split()))

    # Check if s1 is a subset of s2
    print(s1.issubset(s2))


    

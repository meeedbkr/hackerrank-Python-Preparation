'''
Given an integer,n , and n space-separated integers as input, create a tuple, t , of those n integers. Then compute and print the result of  hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
'''


# Check if this module is being run as the main program
if __name__ == '__main__':
    # Read the input integer n
    n = int(input())
    # Read a space-separated list of integers and store it as a list of integers
    integer_list = list(map(int, input().split()))
    # Convert the list of integers to a tuple, sorted in ascending order
    integer_tuple = tuple(sorted(integer_list))
    # Print the hash value of the integer tuple
    print(hash(integer_tuple))

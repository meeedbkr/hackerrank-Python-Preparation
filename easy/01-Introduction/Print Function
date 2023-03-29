'''
The included code stub will read an integer, n , from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.
'''
# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Prompt the user to enter an integer value and convert it to an integer.
    n = int(input())
    
    # Concatenate the range of numbers into a single string and print it.
    numbers = ''.join(str(i) for i in range(1, n+1))
    print(numbers)

'''
In general, numbers = ''.join(str(i) for i in range(1, n+1)) is likely to be faster than for i in range(1, n+1): print(i, end='') for larger values of n.

The reason for this is that the join() method is implemented in C, which makes it very fast for concatenating strings. In contrast, using a loop to print each number individually can be slower, especially for larger values of n.
'''
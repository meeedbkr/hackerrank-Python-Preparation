'''
Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Prompt the user to enter two integer values and convert them to integers.
    a = int(input())
    b = int(input())
    
    # Perform addition, subtraction, and multiplication operations on a and b and print the results.
    print(a+b)
    print(a-b)
    print(a*b)

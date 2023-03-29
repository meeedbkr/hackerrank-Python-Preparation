'''
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a//b . The second line should contain the result of float division, a/b .

No rounding or formatting is necessary.
'''

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Prompt the user to enter two integer values and convert them to integers.
    a = int(input())
    b = int(input())
    
    # Perform integer division on a and b and print the result.
    print(a//b)
    
    # Perform floating-point division on a and b and print the result.
    print(a/b)

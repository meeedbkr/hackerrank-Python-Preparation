'''
The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<n print i**2 .
'''

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Prompt the user to enter an integer value and convert it to an integer.
    n = int(input())
    
    # Iterate through a range of n and print the square of each number.
    for i in range(n):
        print(i**2)

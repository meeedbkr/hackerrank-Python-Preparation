'''
Given an integer, n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20 , print Weird
If n is even and greater than 20 , print Not Weird
'''

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Prompt the user to enter an integer value and convert it to an integer.
    n = int(input().strip())
    
    # Check if n is odd or between 6 and 20 (inclusive) and print "Weird" if true.
    if n%2==1 or ( n%2==0 and n<=20 and n>=6  ):
        print('Weird')
        
    # Check if n is even and between 2 and 5 (inclusive) or greater than 20, and print "Not Weird" if true.
    elif n%2==0 and n<=5 and n>=2 or ( n%2==0 and n>=20  ) :
        print('Not Weird')

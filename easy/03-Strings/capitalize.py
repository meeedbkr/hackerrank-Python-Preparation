# The code imports necessary modules for running the program
import math
import os
import random
import re
import sys

# The solve function takes a string s as input and returns a modified string
# where the first character of each word is capitalized
def solve(s):
    # Initialize an empty string called out
    out = ""
    # Loop through each character in the input string s and its index using enumerate
    for i, chr in enumerate(s):
        # Check if the current character is the first character in the string or if the previous
        # character is a space. If either of these conditions is true, capitalize the current character
        if(i == 0 or s[i - 1] == " "):
            out = out + chr.upper()
        else:
            out = out + chr
    # Return the modified string out
    return out
        
# This if statement checks if the code is being run as the main program
# and creates a file object to write the output of the solve function to a file
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Prompt the user to input a string and assign it to the variable s
    s = input()

    # Call the solve function on the input string and store the output in the variable result
    result = solve(s)

    # Write the modified string to a file and close the file
    fptr.write(result + '\n')
    fptr.close()

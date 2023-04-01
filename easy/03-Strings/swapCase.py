#In Python, a string can be split on a delimiter.

# This function takes a string and returns the string with cases swapped.
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    # Take user input as string.
    s = input()

    # Call the swap_case function and assign the returned value to a variable.
    result = swap_case(s)

    # Print the result.
    print(result)
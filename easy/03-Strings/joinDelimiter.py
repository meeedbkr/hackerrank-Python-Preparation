#In Python, a string can be split on a delimiter.



def split_and_join(line):
    # Split the input string into a list of strings using the `split` method.
    # Join the list of strings using the `join` method, and separate each element with a hyphen ('-').
    # Return the resulting string.
    return '-'.join(line.split()) 

if __name__ == '__main__':
    # Take user input as a string.
    line = input()

    # Call the `split_and_join` function and assign the returned value to a variable called `result`.
    result = split_and_join(line)

    # Print the resulting string to the console using the `print` function.
    print(result)

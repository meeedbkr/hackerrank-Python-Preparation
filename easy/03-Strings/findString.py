# Define a function called count_substring that takes two parameters: a string and a sub_string.
def count_substring(string, sub_string):
    # Initialize a variable called count to 0.
    count = 0
    # Loop through the string using a range from 0 to the length of the string minus 1.
    for i in range(len(string)-1):
        # If the substring is found at the current position in the string,
        if string[i:].startswith(sub_string):
            # increment the count.
            count += 1
    # Return the final count.
    return count

# The code below is executed only if the script is run directly and not imported as a module.
if __name__ == '__main__':
    # Take two inputs from the user: a string and a sub_string.
    string = input()
    sub_string = input()

    # Call the count_substring function with the user's inputs and print the result.
    result = count_substring(string, sub_string)
    print(result)

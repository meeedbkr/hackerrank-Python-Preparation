# Define a function called 'mutate_string' that takes in three parameters, 'string', 'position', and 'character'.
# The function returns a string that is identical to 'string', except that the character at the given 'position' is replaced with the given 'character'.
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    # Take user input as a string called 's', and two separate inputs 'i' and 'c' as an integer and a character, respectively.
    s = input()
    i, c = input().split()

    # Call the 'mutate_string' function with 's', 'int(i)', and 'c' as arguments and assign the resulting string to a variable called 's_new'.
    s_new = mutate_string(s, int(i), c)

    # Print the resulting string 's_new' to the console using the 'print' function.
    print(s_new)

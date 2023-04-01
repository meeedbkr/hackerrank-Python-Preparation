#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# Define the function 'print_full_name', which takes in two parameters, 'first' and 'last'
def print_full_name(first, last):
    # Concatenate the strings 'Hello', 'first', 'last', and '! You just delved into python.' using string interpolation
    # and print the resulting string to the console.
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    # Take user input as 'first_name' and 'last_name'
    first_name = input()
    last_name = input()

    # Call the 'print_full_name' function with 'first_name' and 'last_name' as arguments and print the result to the console.
    print_full_name(first_name, last_name)

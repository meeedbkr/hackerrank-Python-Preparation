# Define a function to print formatted output
def print_formatted(number):
    # Loop through the range of numbers from 1 to number + 1
    for i in range(1, number + 1):
        # Determine the length of the binary representation of the number
        x = len(bin(n)[2:])
        # Print the number in decimal, octal, hexadecimal, and binary formats with appropriate padding
        print(f'{str(i).rjust(x)} {oct(i)[2:].rjust(x)} {hex(i)[2:].rjust(x).upper()} {bin(i)[2:].rjust(x)}')

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Read input from the user and call the print_formatted function
    n = int(input())
    print_formatted(n)

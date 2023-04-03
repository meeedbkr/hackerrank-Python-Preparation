import string

def print_rangoli(size):
    # Get all lowercase letters
    alpha = string.ascii_lowercase

    # Calculate the maximum length of the row
    max_r = size * 2 - 1

    # Calculate the total number of characters in the row
    chars = 2 * max_r - 1

    # Print the top half of the pattern
    for i in range(size):
        # Calculate the characters to include in the row
        row_chars = alpha[size - 1:size - i - 1:-1] + alpha[size - i - 1:size]

        # Join the characters with '-' and center the row
        row = '-'.join(row_chars).center(chars, '-')

        # Print the row
        print(row)

    # Print the bottom half of the pattern
    for i in range(size - 2, -1, -1):
        # Calculate the characters to include in the row
        row_chars = alpha[size - 1:size - i - 1:-1] + alpha[size - i - 1:size]

        # Join the characters with '-' and center the row
        row = '-'.join(row_chars).center(chars, '-')

        # Print the row
        print(row)

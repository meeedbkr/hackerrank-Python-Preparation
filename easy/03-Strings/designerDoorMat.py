# Take two integers as input from user separated by space
n, m = map(int, input().split())

# Calculate half the number of rows
n2 = n // 2

# Loop through the first half of the rows and print them
for i in range(n2):
    # Print the left side of the row
    print('-' * ((n2 - i) * 3), end='')

    # Print the center part of the row
    print('.|.' * (1 + 2 * i), end='')

    # Print the right side of the row
    print('-' * ((n2 - i) * 3))

# Print the middle row
print('WELCOME'.center(m, '-'))

# Loop through the second half of the rows and print them
for i in range(n2 - 1, -1, -1):
    # Print the left side of the row
    print('-' * ((n2 - i) * 3), end='')

    # Print the center part of the row
    print('.|.' * (1 + 2 * i), end='')

    # Print the right side of the row
    print('-' * ((n2 - i) * 3))

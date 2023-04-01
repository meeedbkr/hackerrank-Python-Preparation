if __name__ == '__main__':
    # Take user input as a string called 's'.
    s = input()

    # Convert the string 's' to a list of characters and assign it back to the variable 's'.
    s = list(s)

    # Check whether any of the characters in the list 's' is alphanumeric using a list comprehension, and print the result.
    print(any([el.isalnum() for el in s]))

    # Check whether any of the characters in the list 's' is alphabetic using a list comprehension, and print the result.
    print(any([el.isalpha() for el in s]))

    # Check whether any of the characters in the list 's' is a digit using a list comprehension, and print the result.
    print(any([el.isdigit() for el in s]))

    # Check whether any of the characters in the list 's' is lowercase using a list comprehension, and print the result.
    print(any([el.islower() for el in s]))

    # Check whether any of the characters in the list 's' is uppercase using a list comprehension, and print the result.
    print(any([el.isupper() for el in s]))
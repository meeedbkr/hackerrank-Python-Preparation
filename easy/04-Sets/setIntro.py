def average(array):
    # Convert the input list to a set to remove duplicates
    a_set = set(array)

    # Calculate the average of the set
    average = sum(a_set) / len(a_set)

    # Return the average
    return average

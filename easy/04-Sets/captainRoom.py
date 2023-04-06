# This line reads an integer from the user and assigns it to the variable "k".
k = int(input())

# This line reads input from the user, splits it by spaces, 
# converts each element to integer and creates a list of integers "list1".
list1 = list(map(int, input().split()))

# This creates an empty dictionary "a" to store the frequency count of integers in "list1".
a = {}

# This loop iterates over the elements in "list1" and counts the frequency of each integer using dictionary "a".
# If the integer already exists in the dictionary, its frequency is incremented by 1. Otherwise, it is added
# to the dictionary with a frequency count of 1.
for i in range(len(list1)):
    if list1[i] in a.keys():
        a[list1[i]] += 1
    else:
        a[list1[i]] = 1

# This loop iterates over the key-value pairs in dictionary "a" and prints the key (integer) for those
# with a frequency count less than 5.
for k, v in a.items():
    if v < 5:
        print(k)


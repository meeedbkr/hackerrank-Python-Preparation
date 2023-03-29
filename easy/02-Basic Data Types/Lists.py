'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e .
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__ == '__main__':
    N = int(input())
    # Initializing an empty list arr
    arr = []

    # Loop through N number of times and perform the command based on the input
    while N>0:
        # Take input of the command in form of a list called line
        line = input().split()

        # Perform the insert command on the list arr
        if line[0]=='insert':
            index = int(line[1])
            el = int(line[2])
            arr.insert(index,el)

        # Print the list arr
        if line[0]=='print':
            print(arr)

        # Remove an element from the list arr
        if line[0]=='remove':
            el = int(line[1])
            arr.remove(el)

        # Append an element to the list arr
        if line[0]=='append':
            el = int(line[1])
            arr.append(el)

        # Sort the list arr
        if line[0]=='sort':
            arr.sort()

        # Remove and return the last element from the list arr
        if line[0]=='pop':
            arr.pop()

        # Reverse the order of the list arr
        if line[0]=='reverse':
            arr.reverse()

        # Decrement the value of N
        N-=1

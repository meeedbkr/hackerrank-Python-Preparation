# read in the number of elements in the set
n = int(input())

# read in the elements of the set and create a set object
s = set(map(int, input().split()))

# read in the number of commands to execute
no_commands = int(input())

# iterate over each command
for i in range(no_commands):
    
    # read in the command as a list of strings
    commands = input().strip().split()
    
    # execute the command
    if commands[0] == 'pop':
        # remove and return an arbitrary element from the set
        s.pop()
    if commands[0] == 'remove':
        # remove the element with the given value from the set
        if commands[1] not in s:
            # if the element is not in the set, discard it
            s.discard(int(commands[1]))
        else:
            # if the element is in the set, remove it
            s.remove(int(commands[1]))    
    if commands[0] == 'discard':
        # remove the element with the given value from the set (if it exists)
        s.discard(int(commands[1]))    
    
# print the sum of the remaining elements in the set
print(sum(s))
 


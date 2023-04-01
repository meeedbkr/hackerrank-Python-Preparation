# Prompt the user to enter an integer value for the variable 'thickness'.
thickness = int(input()) # This must be an odd number

# Set the variable 'c' to the string 'H'.
c = 'H'

# Top Cone: Loop through a range from 0 to 'thickness'-1.
for i in range(thickness):
    # Print a string of 'i' characters of 'c', right-justified within a space of 'thickness-1' characters,
    # followed by a single 'c', followed by a string of 'i' characters of 'c', left-justified within a space of 'thickness-1' characters.
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars: Loop through a range from 0 to 'thickness'.
for i in range(thickness+1):
    # Print two strings of 'thickness' characters of 'c', centered within a space of 'thickness*2' characters, 
    # followed by two more strings of 'thickness' characters of 'c', centered within a space of 'thickness*6' characters.
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt: Loop through a range from 0 to '(thickness+1)//2'.
for i in range((thickness+1)//2):
    # Print a string of 'thickness*5' characters of 'c', centered within a space of 'thickness*6' characters.
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars: Loop through a range from 0 to 'thickness'.
for i in range(thickness+1):
    # Print two strings of 'thickness' characters of 'c', centered within a space of 'thickness*2' characters, 
    # followed by two more strings of 'thickness' characters of 'c', centered within a space of 'thickness*6' characters.
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# Bottom Cone: Loop through a range from 0 to 'thickness'-1.
for i in range(thickness):
    # Print a string of 'thickness-i-1' characters of 'c', right-justified within a space of 'thickness' characters,
    # followed by a single 'c', followed by a string of 'thickness-i-1' characters of 'c', left-justified within a space of 'thickness' characters,
    # followed by that entire string right-justified within a space of 'thickness*6' characters.
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

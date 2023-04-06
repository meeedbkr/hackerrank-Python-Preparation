# Enter your code here. Read input from STDIN. Print output to STDOUT
# Importing the cmath library
import cmath

# Getting user input for a complex number as a string, and converting it to a complex number object
c = complex(input().strip())

# Calculating the magnitude (modulus) of the complex number
r = cmath.sqrt(c.real**2 + c.imag**2)

# Calculating the phase (angle) of the complex number
phi = cmath.phase(c)

# Printing the magnitude of the complex number, ignoring any imaginary component
print(r.real)

# Printing the phase of the complex number in radians
print(phi)



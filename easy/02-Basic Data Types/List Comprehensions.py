'''Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (x,y,z) on a 3D grid where the sum of i+j+k is not equal to n . Here, 0<=i<=x; 0<=j<=y;0<=k<=z . Please use list comprehensions rather than multiple loops, as a learning exercise.'''

if __name__ == '__main__':    # check if the script is being run as the main program
    x = int(input())         # prompt the user to input an integer value for x
    y = int(input())         # prompt the user to input an integer value for y
    z = int(input())         # prompt the user to input an integer value for z
    n = int(input())         # prompt the user to input an integer value for n

    # create a list l of all possible combinations of three integers i, j, and k, where each integer is in the range of 0 to x, y, and z respectively, but exclude any combination where i+j+k equals n
    l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!= n]

    print(l)                 # output the resulting list l

'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.'''


if __name__ == '__main__':   # check if the script is being run as the main program
    n = int(input())         # prompt the user to input an integer value n
    arr = list(map(int, input().split()))   # prompt the user to input n space-separated integers, then create a list of integers called 'arr'
    arr.sort(reverse=True)   # sort the list 'arr' in descending order
    for i in arr:            # iterate through the elements in the list 'arr'
        if i != arr[0]:      # check if the current element is not equal to the first element in the sorted 'arr'
            print(i)         # if true, print the current element and break out of the loop
            break

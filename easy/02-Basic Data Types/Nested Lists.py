'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
'''

if __name__ == '__main__':
    # Initializing empty lists for student names and scores
    stds = []
    scores = []
    # Loop through input of number of students
    for _ in range(int(input())):
        # Take input of student name and score and store it in respective lists
        name = input()
        score = float(input())
        scores.append(score)
        stds.append([score,name])
        
    # Sort the student list based on the score in descending order and also sort the scores in descending order
    stds.sort(key=lambda a:a[0],reverse=True)
    scores.sort(reverse=True)

    # Find the second lowest score
    x = scores.count(scores[-1])

    # Make a list of names of students who have the second lowest score
    names = [ i[1] for i in stds if i[0]==stds[-(x+1)][0]]
    names.sort()

    # Print the names of the students who have the second lowest score
    for name in names:
        print(name)

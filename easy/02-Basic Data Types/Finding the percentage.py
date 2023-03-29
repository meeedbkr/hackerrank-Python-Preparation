'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

if __name__ == '__main__':
	n = int(input()) # prompt the user to input the number of students
	student_marks = {} # initialize an empty dictionary to store students' marks
	# loop through the range of the number of students and take input of their names and scores, store them in the dictionary
	for _ in range(n):
	    name, *line = input().split()
	    scores = list(map(float, line))
	    student_marks[name] = scores

	query_name = input()  # take input of the query name
	notes = student_marks[query_name]  # get the grades of the query name
	subjects = len(notes)  # calculate the number of subjects
	percentage = sum(notes)/subjects  # calculate the average score of the query name's grades

	print(f'{percentage:.2f}')  # output the average score with two decimal places

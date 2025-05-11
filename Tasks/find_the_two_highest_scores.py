import math

largest_name = ""
largest_name_2 = ""

largest_score = -math.inf
largest_score_2 = -math.inf
number_of_students = int(input("Enter the number of students: "))
print()
for index in range(1, number_of_students + 1):
	student_name = str(input(f"Enter student {index}'s name: "))
	student_score = int(input(f"Enter student {index}'s score: "))
	print()
	if student_score > 100 or student_score < 0:
		print("Invalid score...") 
		break
	elif student_score > largest_score:
		largest_score_2 = largest_score
		largest_score = student_score
		
		largest_name_2 = largest_name
		largest_name = student_name
		
	elif student_score > largest_score_2:
		largest_name_2 = student_name
		largest_score_2 = student_score

		
if student_score < 100 and student_score > 0:
	print(f"HIGHEST SCORE 1:\nName: {largest_name}\nScore: {largest_score}\n")
	print(f"HIGHEST SCORE 2:\nName: {largest_name_2}\nScore: {largest_score_2}")
		

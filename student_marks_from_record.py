# program to display student's marks from record
student_name ="Arun"

marks = {"Arun":50,"Binu":70,"Kiran":80}

for student in marks:
	if student == student_name:
		print(marks[student])
		break
else:
	print("no entry with that name")

student = {"appu":23,"jomon":22,"jis":24}

def my_fun(student1):
	student2 = {"bibin":20,"norman":20}
	student1.update(student2)
	return student1


result = my_fun(student)

print("inside function ", result)

print("outside function ", student)


"""
inside function  {'appu': 23, 'jomon': 22, 'jis': 24, 'bibin': 20, 'norman': 20}
outside function  {'appu': 23, 'jomon': 22, 'jis': 24, 'bibin': 20, 'norman': 20}

"""
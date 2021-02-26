#Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {"name":"Daby","age":28}

child2 = {"name":"Jims","age":25}

child3 = {"name":"Robin","age":23}


myfamily = {
	"child1":child1,
	"child2" :child2,
	"child3" : child3
}


print(myfamily)

"""
{'child1': {'name': 'Daby', 'age': 28}, 'child2': {'name': 'Jims', 'age': 25}, 'child3': {'name': 'Robin', 'age': 23}}
"""
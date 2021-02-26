
#Accept a list of strings from user input
members = input("enter family members seperated by comma: ")
print(members)
#split into a list of strings by comma or default is space - split(" ") or split()
members_split = members.split(",")
print(members_split)

for x in members_split:
	print(x)

"""
enter family members seperated by comma appa,amma,bro
appa,amma,bro
['appa', 'amma', 'bro']

appa
amma
bro

"""






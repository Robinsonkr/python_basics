customers= [

{
	'name':'John',
	'country': 'USA'
},
{
	'name':'Mohan',
	'country': 'India'
},
{
	'name':'Nancy',
	'country' : 'USA'
},

{
	'name':'abdul',
	'country':'India'
}


]

unique_countries = set() #use set
for customer in customers:
	unique_countries.append(customer['country'])


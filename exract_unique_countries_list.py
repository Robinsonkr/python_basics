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

countries = [] #use set
for customer in customers:
	countries.append(customer['country'])

print(countries)
unique_countries = remove_duplicates(countries)
print(unique_countries)


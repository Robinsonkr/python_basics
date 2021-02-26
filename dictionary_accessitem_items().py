#items() method will return each item in a dictionary, as tuples in a list
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.items())

for x,y in thisdict.items():
    print(x,y)

"""
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

brand Ford
model Mustang
year 1964

"""
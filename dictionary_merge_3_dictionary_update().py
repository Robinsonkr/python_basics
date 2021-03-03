def merge_2_dictionary(dict1,dict2,dict3):
	final_cars = {}

	for i in (dict1,dict2,dict3):
		final_cars.update(i)

	return final_cars

cars1 = {"audi":20000,"bmw":50000}

cars2 = {"benz": 30000,"toyota":10000}

cars3 = {"maruti":25000,"nano":8000}

result = merge_2_dictionary(cars1,cars2,cars3)

print(result)

"""

{'audi': 20000, 'bmw': 50000, 'benz': 30000, 'toyota': 10000, 'maruti': 25000, 'nano': 8000}

"""





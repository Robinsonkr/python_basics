 # Area of circle = π r² 
from builtin_function import pi

def area_circle(r):
	if type(r) not in [int, float]:
		raise TypeError("the radius must be a non negetive real numbers")
		
	if r < 0:
		raise TypeError("the radius cannot be negetiveee")

	return pi * (r**2)

print(area_circle(5))
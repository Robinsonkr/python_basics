# Find the number of occurrence of each values in an iterable
from collections import Counter
my_list= ["apple","apple",5,22,22,22]

result = Counter(my_list)

print(result)

"""

Counter({22: 3, 'apple': 2, 5: 1})


"""
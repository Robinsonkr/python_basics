#get only even numbers from list using lambda
numbers = [1,2,3,4,5,6,7,8,9,10]

even_nums =filter(lambda x : x% 2 == 0,numbers)

print(list(even_nums))

"""
[2, 4, 6, 8, 10]

"""
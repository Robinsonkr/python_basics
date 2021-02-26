## filter() with lambda()
mylist= [1,2,3,4,5,6,7,8,9,10]

even_list= list(filter(lambda x:(x%2 ==0),mylist))

print(even_list)

"""
[2, 4, 6, 8, 10]

"""
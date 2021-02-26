#get only even numbers from list
list1 = [1,2,3,4,5,6,7,8,9,10]

def even(x):
    if x % 2 == 0:
        return x

f = filter(even, list1)
print(list(f))
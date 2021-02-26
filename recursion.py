#sum of that number from(5 = 1+2+3+4+5)
def recursion(n):
    if n <= 1:
        return n
    else:
        return n + recursion(n-1)

summ = recursion(5)
print(summ)



"""
15
"""
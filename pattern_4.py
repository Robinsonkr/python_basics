num = int(input("Enter no of rows "))
for i in range(num):
    for j in range(i+1):  #i+1 is columns, and num is rows
        print(j+1, end=" ")
    print() #goto nextline


"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

"""
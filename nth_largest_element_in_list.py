# Python program to find N largest 
# element from given list of integers 
  
# Function returns N largest elements 
def Nmaxelements(list1, N): 
    final_list = [] 
    for i in range(0, N):  #0 1
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1:
                max1 = list1[j];
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    print(final_list) 
  
# Driver code 
list1 = [30,10,20,40,50] 
N = 2
  
# Calling the function 
Nmaxelements(list1, N)

"""

[85, 10]

"""
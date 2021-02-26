#kth largest element in unorderedlist
#[6 9 2 5]
#9 first largest element
#6 second largest element
#5 third largest element
#2 4th largest element

list1 = [6,9,2,5]

k = int(input("enter k: "))

#descending order
list1.sort(reverse=True)

print(list1) #[9, 6, 5, 2]

print(list1[k-1])


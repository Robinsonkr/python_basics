my_list = [1, 3, 5, 6, 3, 5, 6, 1]

unique_list = []

[unique_list.append(x) for x in my_list if x not in unique_list]

print(unique_list)

"""
[1, 3, 5, 6]

"""
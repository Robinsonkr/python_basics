def Convert_list_to_dict(a):
    initt = iter(a)
    res_dct = dict(zip(initt, initt))
    return res_dct


# Driver code
list1 = ['arun', 10, 'jose', 20, 'hari', 30]
print(Convert_list_to_dict(list1))
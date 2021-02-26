# add items from another set(ANY ITERABLE) into the current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}


thisset.update(tropical)


print(thisset)


"""

{'banana', 'papaya', 'pineapple', 'cherry', 'mango', 'apple'}

"""
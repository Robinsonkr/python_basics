
# Count vowels in a different way 
# Using dictionary 
def Check_Vow(string, vowels): 
      
    # casefold has been used to ignore cases 
    stringg = string.casefold()
    print(stringg)
      
    # Forms a dictionary with key as a vowel 
    # and the value as 0 
    count = {}.fromkeys(vowels, 0) 
    # To count the vowels 
    for character in stringg:
        if character in count: 
            count[character] += 1    
    return count 
      
# Driver Code 
vowels = 'aeiou'
string = str(input("Enter string: "))

print (Check_Vow(string, vowels))


"""
{'a': 0, 'e': 4, 'i': 0, 'o': 1, 'u': 0}

"""
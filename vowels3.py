def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
    print(final) 
      
# Driver Code 
string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels); 


# def vowel(text):
#     vowels = "aeiuoAEIOU"
#     print(len([letter for letter in text if letter in vowels]))
#     print([letter for letter in text if letter in vowels])
# vowel('w3resource');
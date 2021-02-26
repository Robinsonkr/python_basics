a_string = input("enter string: ")
lowercase = a_string.lower()

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count


print(vowel_counts)
# counts = vowel_counts.values() #Number of each vowel

# total_vowels = sum(counts)
# print(total_vowels)

"""
enter string: hello world

{'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}

"""
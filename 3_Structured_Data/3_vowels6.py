vowels = set('aeiou')
word = input("Type me: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)

#1. Write a function called count_vowels(input) that takes a 
#string
#and returns the number of vowels (a, e, i, o, u) in it.


def count_vowels(input):
    count = 0
    vowels = "a,e,i,o,u"
    for letter in input:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("apple"))
print(count_vowels("easter"))
print(count_vowels("abracadabra"))

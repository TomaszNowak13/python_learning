"""Disemvoweling means removing the vowels from text.
(For this challenge, the letters a, e, i, o, and u are considered
vowels, and the letter y is not.) The idea is to make text
difficult but not impossible to read, for when somebody posts
something so idiotic you want people who are reading it to
get extra frustrated. We also want to keep the vowels we removed
around (in their original order)."""

def disemvoweler():
    x = input("Enter a word: ")
    word = x.lower()
    vowels = ("a", "e", "i", "o", "u")
    new_word = ""
    removed_vowels = ""
    for letter in word:
        if letter not in vowels:
            new_word += letter
        else:
            removed_vowels += letter
    new_word = new_word.replace(" ", "")
    removed_vowels = removed_vowels.replace(" ","")
    print ("New word: ", new_word)
    print ("Removed vowels: ", removed_vowels)
    
disemvoweler()

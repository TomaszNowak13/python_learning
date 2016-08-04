"""Atbash is a simple substitution cipher originally
for the Hebrew alphabet, but possible with any known
alphabet. It emerged around 500-600 BCE. It works by
substituting the first letter of an alphabet for the
last letter, the second letter for the second to last
and so on, effectively reversing the alphabet. Implement
the Atbash cipher and encode (or decode) some English
language words. If the character is NOT part of the
English alphabet (a-z), you can keep the symbol intact."""

def atbash_cipher():
    word = input("Write a word: ").lower()
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    encoded_word = ""
    change_letter = ""
    
    for letter in word:
        if letter in plain:
            encoded_word += cipher[plain.index(letter)]
        else:
            encoded_word += letter

    print ("Encoded/decoded word: ",encoded_word)
    
atbash_cipher()

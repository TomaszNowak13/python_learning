"""Rövarspråket is super-secret language in Sweden.
Here's the rules: you take an ordinary word and replace the consonants with
the consonant doubled and with an "o" in between. So the consonant "b" is
replaced by "bob", "r" is replaced with "ror", "s" is replaced with "sos",
and so on. Vowels are left intact. It's made for Swedish, but it works
just as well in English. Your task today is to write a program that
can encode a string of text into Rövarspråket."""

def rovarspraket():
    vowels = ("A", "E", "I", "O", "U", "Y", "Å", "Ä", "Ö")
    punctuation_marks = (".", ",", "!", "?", ":", ";", "'")
    choice = None
    
    while choice != "0":
        print("1 - Encode sentence \n"
           "2 - Decode sentence \n"
          "0 - Exit")
        choice = input("What do you want to do? ")
        if choice == "0":
            print ("Goodbye")
        elif choice == "1":
            word = input("Please enter a word: ")
            encoded_word = ""
            for letter in word:
                if letter.lower() and letter.upper() not in vowels and letter.lower() and letter.upper() not in punctuation_marks:
                    encoded_word = encoded_word + letter + "o" + letter.lower()
                else:
                    encoded_word = encoded_word + letter
            print ("Encoded word: ", encoded_word)
        elif choice == "2":
            x = input("Please enter a word: ")
            word = x.split()
            decoded_word = ""
            i = 0
            while i < len(word):
                decoded_word += word[i]
                if word[i].lower() and word[i].upper() in vowels and word[i].lower() and word[i].upper() in punctuation_marks:
                    i += 1
                else:
                    i += 3
            print ("Decoded word: ", decoded_word)
        else:
            print ("There's no option")

    input("Press Enter to exit")


rovarspraket()
            

"""Enter a string and the program will reverse it and print it out."""

def reverse_string():
    word = input("Enter your word: ")
    back_word = ""
    for letter in word:
        back_word = letter + back_word
    print ("Your word in reverse: ",back_word)

reverse_string()

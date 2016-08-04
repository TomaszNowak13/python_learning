"""A handful of words have their letters in alphabetical order, that is nowhere in the word do you change direction in the word if you were to scan along the English alphabet. An example is the word "almost", which has its letters in alphabetical order.
Your challenge today is to write a program that can determine if the letters in a word are in alphabetical order.
As a bonus, see if you can find words spelled in reverse alphebatical order."""

def alphabetical_order():
    x = None
    while x != 0:
        word = input("Write yout word: ")
        alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
        word_order = []
        for letter in word.upper():
            word_order.append(alphabet.index(letter))
        
        order = sorted(word_order)
        reverse_order = sorted(word_order, reverse=True)

        if word_order == order:
            print (word, "IN ORDER")
        elif word_order == reverse_order:
            print (word, "REVERSE ORDER")
        else:
            print (word, "NOT IN ORDER")
        
alphabetical_order()

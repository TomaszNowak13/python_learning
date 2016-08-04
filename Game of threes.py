"""Game of Threes. Here's how you play it:
First, you mash in a random large number to start with.
Then, repeatedly do the following:
If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3),
then divide it by 3.
The game stops when you reach "1"."""

def game_of_threes():
    x = int(input("Write a number: "))
    while x != 1:
        if x % 3 == 0:
            x = x / 3
            print (x)
        elif x % 3 == 1:
            x = x - 1
            x = x / 3
            print (x)
        else:
            x = x + 1
            x = x / 3
            print (x)
    print ("1")
    

game_of_threes()
            
        
         

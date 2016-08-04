""" Start with a number n > 1. Find the number of steps it
takes to reach one using the following process: If n is even,
divide it by 2. If n is odd, multiply it by 3 and add 1."""

def collatz_conjecture():
    step = int(input("Write number > 1: "))
    while step != 1:
        if step % 2 == 0:
            step = step/2
            print (step)
        else:
            step = step * 3 + 1
            print (step)
    print("End")

collatz_conjecture()

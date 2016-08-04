"""Enter a number and have the program generate
the Fibonacci sequence which has the length of the number given."""

def fibonacci():
    num = int(input("How long Fibonnacci sequence should be? "))
    sequence = [0, 1]
    for i in range(0,num-2):
        new_item = sequence[len(sequence)-2] + sequence[len(sequence)-1]
        sequence.append(new_item)

    for i in sequence:
        print (i)

fibonacci()

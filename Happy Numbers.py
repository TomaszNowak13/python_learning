"""A happy number is defined by the following process.
Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers
for which this process ends in 1 are happy numbers, while those
that do not end in 1 are unhappy numbers. Check if the number given
is happy or unhappy."""

def happy_numbers():
    num = str(input("Enter a number: "))
    numbers = [num]
    count = 0
    while True:
        if "1" in numbers:
            print("\nYour number is happy :)")
            break
        elif numbers.count(numbers[len(numbers)-1]) > 1:
            print("\nYour number is unhappy :(")
            break
        else:
            temp = 0
            for i in numbers[count]:
                temp += int(i)**2    
            numbers.append(str(temp))
            count += 1
            print(temp)
    print("\nGoodbye")

happy_numbers()

            
    

"""Binary to Decimal and Back Converter -
Develop a converter to convert a decimal number to binary
or a binary number to its decimal equivalent."""

def binary_to_decimal(num):
    num = "0b" + num
    print ("Your binary number in decimal notation: ", int(num, 2))

def decimal_to_binary(num):
    binary = ""
    while num != 0:
        binary = binary + str(num % 2)
        num = num // 2
    print ("Your decimal number in binary notation: ", binary[::-1])

def main():
    choice = None
    while choice != "0":
        print("\n 1 - Convert binary to decimal\n"
          " 2 - Convert decimal to binary\n"
          " 0 - Exit")
        choice = input("Choose convert option: ")
        if choice == "0":
            print ("Goodbye")
        elif choice == "1":
            num = input("Enter your binary number: ")
            binary_to_decimal(num)
        elif choice == "2":
            num = int(input("Enter your decimal number: "))
            decimal_to_binary(num)
        else:
            print("There's no option like this")
    input("Press Enter to exit")

main()

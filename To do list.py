"""Create a "To do list" program. It should havethe following basic functionality:
- Add an item to the to-do list
- Delete a selected item from the to-do list
- And obviously, print out the list so I can see what to do!"""


def to_do_list():
    list = {}
    choice = None
    while choice != "0":
        print("""
            1 - Add item
            2 - Delete item
            0 - Exit
                 """)
        choice = input("\nWhat do you want to do? ")
        if choice == "1":
            word = input("Write a new item to the list: ")
            print(word, "has been added to your list.")
            list[len(list)+1] = word
        elif choice == "2":
            num = int(input("Select a number of deleted item: "))
            print(list[num], "has been deleted.")
            del list[num]
            i = 1
            for key in list.keys():
                list[i] = list.pop(key)
                i += 1
                
        print("\nYour list: ")
        for key, value in list.items():
            print (str(key) + ". ", value)
        
    print ("Goodbye")

to_do_list()

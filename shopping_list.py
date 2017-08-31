shopping_list = []


def help():
    print("""
        +===================================================================+
        | Simply type the item you would like to add to the list.           |
        | Typing "RM" will take you to the remove item program.             |
        | Typing "DONE" will exit the program and print your final list:    |
        +===================================================================+
        """)


def add_item(command):
    """function to add and and remove items in list"""
    if command != 'RM':
        # adds item to list
        shopping_list.append(command)
        return shopping_list
    else:
        # function to remove item
        remove_it()


def remove_it():
    """item removal loop"""
    while True:
        for number, item in enumerate(shopping_list):
            print(number + 1, item)
        n = int(
            input("Type the number of the item you would like to remove \
(0 to exit the removal program): "))
        if n == 0:
            break
        else:
            del shopping_list[n - 1]


def main():
    help()
    while True:
        command = input("'?' for help > ")
        if command == "DONE":
            print("Here's the shit you need to get:")
            for item in sorted(shopping_list):
                print(item)
            break
        elif command == '?':
            help()
        else:
            add_item(command)
            print("{}.".format(shopping_list))

if __name__ == '__main__':
    main()

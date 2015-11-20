

def add_item(action):
    to_do.append(action)

def remove_item(action):
    to_do.remove(action)

def view_list():
    print("".join(to_do))

def number(s):
    global is_number
    try:
        int(s)
        is_number = True
    except ValueError:
        is_number = False

to_do = []

while True:
    option = input("Would you like to: "
                   "\n1) Add an item to your to-do list?"
                   "\n2) Remove an item from your to-do list?"
                   "\n3) View your to-do list?"
                   "\n4) End the program?"
                   "\nAnswer: ")

    number(option)
    if option == "1":
        activity = input("\nWhat would you like to add?: ")
        add_item(activity)
        print("")
    elif option == "2":
        activity = input("\nWhat would you like to remove?: ")
        remove_item(activity)
        print("")
    elif option == "3":
        print("")
        view_list()
        print("")
    elif option == "4":
        break
    else:
        print("That is not a valid input.")
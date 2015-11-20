def palindrome():
    string = input("Please input a string: ")
    result = ""

    for i in reversed(string):
        result += i

    if string.lower() == result.lower():
        print("That word is a palindrome.")
        again()

    else:
        print("That word is not a palindrome.")
        again()

def again():
    restart = input("\nWould you like to restart? ")
    restart.lower()
    if restart == "yes" or restart == "y":
        print("")
        palindrome()

    elif restart == "no" or restart == "n":
        print("Thank you for playing.")

palindrome()



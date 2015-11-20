from random import randint

def randNum():
    
    number = randint(1, 100)
    global number
    numGuess()

def numGuess():

    guess = int(input("Guess my number: ") )

    if guess > number:
        print("Too high.\n")
        numGuess()

    elif guess < number:
        print("Too low.\n")
        numGuess()

    elif guess == number:
        print("Correct!")
        again()

def again():
    restart = input("\nWould you like to restart? ")
    restart.lower()
    if restart == "yes" or restart == "y":
        print("")
        palindrome()

    elif restart == "no" or restart == "n":
        print("Thank you for playing.")

randNum()

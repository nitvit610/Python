import random

computerScore = 0
playerScore = 0

types = ["rock", "r", "paper", "p", "scissors", "s"]

rpsDict = {1: "Rock", 2: "Paper", 3: "Scissors"}

def rps():
    
    choice = input("Rock, paper or scissors? ")
    choiceLower = choice.lower()
    
    if choiceLower in types:
        choiceLow = choiceLower[:1]
        compNum = random.randint(1, 3)
        global compNum

        if choiceLow == "r":
            choiceNum = 1
            game(choiceNum)

        elif choiceLow == "p":
            choiceNum = 2
            game(choiceNum)

        elif choiceLow == "s":
            choiceNum = 3
            game(choiceNum)

    else:
        print("That is not a valid input.\n")
        rps()

def game(x):
    mod = ((x - compNum) % 3)

    if mod == 1:
        print("You win.", rpsDict[x], "beats", rpsDict[compNum] + ".")
        playerScore += 1
        again()

    elif mod == 0:
        print("You draw.", rpsDict[x], "draws with", rpsDict[compNum] + ".")
        again()

    elif mod == 2:
        print("You lose.", rpsDict[compNum], "beats", rpsDict[x] + ".")
        computerScore += 1
        again()

def again():
    restart = input("\nWould you like to restart? ")
    restart.lower()
    
    if restart == "yes" or restart == "y":
        print("")
        rps()

    elif restart == "no" or restart == "n":
        print("Thank you for playing.")

    else:
        print("That was not a valid input.")
        again()

rps()

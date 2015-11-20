import random

computerScore = 0
playerScore = 0

types = ["rock", "r", "paper", "p", "scissors", "s"]

rockDict = {1: "Draw", 2: "Lose", 3: "Win"}
paperDict = {1: "Win", 2: "Draw", 3: "Lose"}
scissorsDict = {1: "Lose", 2: "Win", 3: "Draw"}

rpsDict = {"r": rockDict, "p": paperDict, "s": scissorsDict}

def rps():
    
    choice = input("Rock, paper or scissors? ")
    choiceLower = choice.lower()
    if choiceLower in types:
        choiceLow = choiceLower[:1]
        randomNum = random.randint(1, 3)

        if choiceLow == "r":
            print("You", rpsDict[choiceLow][randomNum])
    
            if rpsDict[choiceLow][randomNum] == "Win":
                score(1)

            elif rpsDict[choiceLow][randomNum] == "Draw":
                score(2)

            elif rpsDict[choiceLow][randomNum] == "Lose":
                score(3)

        elif choiceLow == "p":
            print("You", rpsDict[choiceLow][randomNum])
    
            if rpsDict[choiceLow][randomNum] == "Win":
                score(1)

            elif rpsDict[choiceLow][randomNum] == "Draw":
                score(2)

            elif rpsDict[choiceLow][randomNum] == "Lose":
                score(3)

        elif choiceLow == "s":
            print("You", rpsDict[choiceLow][randomNum])
    
            if rpsDict[choiceLow][randomNum] == "Win":
                score(1)

            elif rpsDict[choiceLow][randomNum] == "Draw":
                score(2)

            elif rpsDict[choiceLow][randomNum] == "Lose":
                score(3)

        else:
            print("That is not a valid input.\n")
            rps()

    else:
        print("That is not a valid input.\n")
        rps()

def score(y):
    global computerScore
    global playerScore

    if y == 1:
        playerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    if y == 2:
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    if y == 3:
        computerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
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

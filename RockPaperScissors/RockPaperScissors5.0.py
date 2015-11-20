import random

computerScore = 0
playerScore = 0

types = ["rock", "r", "paper", "p", "scissors", "s"]
rpsDict = {1: "Rock", 2: "Paper", 3: "Scissors"}

def rps():

    global computerScore
    global playerScore
    
    choice = input("Rock, paper or scissors? ")
    choiceLower = choice.lower()
    
    if choiceLower in types:
        choiceLow = choiceLower[:1]
        compNum = random.randint(1, 3)

        if choiceLow == "r":
            choiceNum = 1

        elif choiceLow == "p":
            choiceNum = 2

        elif choiceLow == "s":
            choiceNum = 3

    else:
        print("That is not a valid input.\n")
        rps()

    mod = ((choiceNum - compNum) % 3)

    if mod == 1:
        playerScore += 1
        print("You win.", rpsDict[choiceNum], "beats", rpsDict[compNum] + ".\nPlayer:", playerScore, "/ Computer:", computerScore)
        again()

    elif mod == 0:
        print("You draw.", rpsDict[choiceNum], "draws with", rpsDict[compNum] + ".\nPlayer:", playerScore, "/ Computer:", computerScore)
        again()

    elif mod == 2:
        computerScore += 1
        print("You lose.", rpsDict[compNum], "beats", rpsDict[choiceNum] + ".\nPlayer:", playerScore, "/ Computer:", computerScore)
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

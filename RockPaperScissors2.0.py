"""
You must make a rock paper scissors game
Goal
Ask the player if they pick rock paper or scissors
Have the computer chose its move
Compare the choices and decide who wins
Print the results
Subgoals
Let the player play again
Keep a record of the score e.g. (Player: 3 / Computer: 6)

rock = 1
paper = 2
scissors = 3

rock beats scissors
paper beats rock
scissors beat paper

1 beats 3
2 beats 1
3 beats 2
"""

import random

computerScore = 0
playerScore = 0

rockDict = {1: "Draw", 2: "Lose", 3: "Win"}
paperDict = {1: "Win", 2: "Draw", 3: "Lose"}
scissorsDict = {1: "Lose", 2: "Win", 3: "Draw"}

rpsDict = {1: rockDict, 2: paperDict, 3: scissorsDict}

def rps():
    
    choice = input("Rock, paper or scissors? ")
    choiceLower = choice.lower()

    randomNum = random.randint(1, 3)
    global randomNum

    if choiceLower == "rock" or choiceLower == "r":
        choiceNum = 1
        global choiceNum
        choiceFunc(choiceNum)

    elif choiceLower == "paper" or choiceLower == "p":
        choiceNum = 2
        global choiceNum
        choiceFunc(choiceNum)

    elif choiceLower == "scissors" or choiceLower == "s":
        choiceNum = 3
        global choiceNum
        choiceFunc(choiceNum)

    else:
        print("That is not a valid input.")
        rps()

def choiceFunc(x):
    if x == 1:
        rock()            

    elif x == 2:
        paper()

    elif x == 3:
        scissors()

def rock():
    global computerScore
    global playerScore
    
    print("You", rpsDict[choiceNum][randomNum])
    if rpsDict[choiceNum][randomNum] == "Win":
        playerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    elif rpsDict[choiceNum][randomNum] == "Draw":
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    elif rpsDict[choiceNum][randomNum] == "Lose":
        computerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

def paper():
    global computerScore
    global playerScore
    
    print("You", rpsDict[choiceNum][randomNum])
    if rpsDict[choiceNum][randomNum] == "Win":
        playerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    elif rpsDict[choiceNum][randomNum] == "Draw":
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    elif rpsDict[choiceNum][randomNum] == "Lose":
        computerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

def scissors():
    global computerScore
    global playerScore
    
    print("You", rpsDict[choiceNum][randomNum])
    if rpsDict[choiceNum][randomNum] == "Win":
        playerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    elif rpsDict[choiceNum][randomNum] == "Draw":
        print("Computer:", computerScore, "/ Player:", playerScore)
        again()

    elif rpsDict[choiceNum][randomNum] == "Lose":
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

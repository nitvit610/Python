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

def rps():
    
    global computerScore
    global playerScore
    
    choice = input("Rock, paper or scissors? ")
    choiceLower = choice.lower()

    randomNum = random.randint(1, 3)

    if choiceLower == "rock" or choiceLower == "r":
        choiceNum = 1

        if choiceNum == randomNum:
            print("That was a draw.")
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

        elif randomNum == 3:
            print("Rock beats scissors.")
            playerScore += 1
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

        elif randomNum == 2:
            print("Paper beats rock.")
            computerScore += 1
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

    elif choiceLower == "paper" or choiceLower == "p":
        choiceNum = 2

        if choiceNum == randomNum:
            print("That was a draw.")
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

        elif randomNum == 1:
            print("Paper beats rock.")
            playerScore += 1
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

        elif randomNum == 3:
            print("Scissors beat paper.")
            computerScore += 1
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

    elif choiceLower == "scissors" or choiceLower == "s":
        choiceNum = 3

        if choiceNum == randomNum:
            print("That was a draw.")
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

        elif randomNum == 2:
            print("Scissors beat paper.")
            playerScore += 1
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

        elif randomNum == 1:
            print("Rock beats scissors.")
            computerScore += 1
            print("Computer:", computerScore, "/ Player:", playerScore)
            again()

    else:
        print("That is not a valid option.")
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

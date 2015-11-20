

print("(1 - 1) % 3 =", (1 - 1) % 3)
print("(1 - 2) % 3 =", (1 - 2) % 3)
print("(1 - 3) % 3 =", (1 - 3) % 3)
print("(2 - 1) % 3 =", (2 - 1) % 3)
print("(2 - 2) % 3 =", (2 - 2) % 3)
print("(2 - 3) % 3 =", (2 - 3) % 3)
print("(3 - 1) % 3 =", (3 - 1) % 3)
print("(3 - 2) % 3 =", (3 - 2) % 3)
print("(3 - 3) % 3 =", (3 - 3) % 3)




"""

computerScore = 0
playerScore = 0

functions = [win, draw, lose]

winDict = {}
drawDict = {}
loseDict = {}

rockDict = {1: drawDict, 2: loseDict, 3: winDict}
paperDict = {1: winDict, 2: drawDict, 3: loseDict}
scissorsDict = {1: loseDict, 2: winDict, 3: drawDict}

rpsDict = {1: rockDict, 2: paperDict, 3: scissorsDict}

choiceNum = 1
randomNum = 2


rockPaperScissors = {1: {1: "Draw"}, {2: "Lose"}, {3: "Win"},
                     2: {1: "Win"}, {2: "Draw"}, {3: "Lose"},
                     3: {1: "Lose"}, {2: "Win"}, {3: "Draw"}}

if randomNum == rps[choiceNum][choiceNum][randomNum]:
    print(rps[choiceNum][randomNum]["Draw"])



rock = {1: "Draw", 2: "Lose", 3: "Win"}
paper = {1: "Win", 2: "Draw", 3: "Lose"}
scissors = {1: "Lose", 2: "Win", 3: "Draw"}

rps = {1: rock, 2: paper, 3: scissors}



if choiceNum == 1:
    print("You", rps[choiceNum][randomNum])


randomNum = random.randint(1, 3)

def choiceOut(x):
    if x == 1:
        choiceRock()

def choiceRock():

    global computerScore
    global playerScore
    
    print("You", rpsDict[choiceNum][randomNum])
    if rpsDict[choiceNum][randomNum][1] == "Win":
        playerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)

    elif rpsDict[choiceNum][randomNum] == "Draw":
        print("Computer:", computerScore, "/ Player:", playerScore)

    elif rpsDict[choiceNum][randomNum] == "Lose":
        computerScore += 1
        print("Computer:", computerScore, "/ Player:", playerScore)

choiceOut(choiceNum)
"""

def next_stage(stage):
    if stage == 0:
        print("")

    if stage == 1:
        print("___")

    if stage == 2:
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 3:
        print(" _____")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 4:
        print(" _____")
        print(" |   |")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 5:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 6:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |   |")
        print(" | ")
        print("_|_")

    if stage == 7:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|")
        print(" | ")
        print("_|_")

    if stage == 8:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" | ")
        print("_|_")

    if stage == 9:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  /")
        print("_|_")

    if stage == 10:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  / \\")
        print("_|_")
        print("You lose! The word was:", fullWord)

fullWord = "banana"
guessed = []
tries = 0
location = []

while True:
    user = input("Guess a letter: ")
    if len(user) != 1:
        print("That is not a single letter.")
    else:
        userInput = user.lower()
        if userInput not in guessed:
            if userInput in fullWord:
                print("That letter is in the word.")
                location.append(fullWord.index(userInput))
                guessed.append(userInput)
                for i in range(1, len(fullWord)):
                    if i in location:
                        print(location[i])
                    else:
                        print("_")
                next_stage(tries)

            elif userInput not in fullWord:
                print("That letter is not in the word.")
                tries += 1
                next_stage(tries)

        else:
            print("You've already guessed that letter.")

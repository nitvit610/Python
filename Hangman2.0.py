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
fullWordArray = []
array = []
guessed = []
tries = 0

for i in fullWord:
    fullWordArray.append(i)

for i in range(len(fullWord)):
    array.append("_")

while True:
    user = input("Guess a letter: ")
    if len(user) != 1:
        print("That is not a single letter.")
    else:
        userInput = user.lower()
        if userInput not in guessed:
            if userInput in fullWord:
                print("That letter is in the word.")

                guessed.append(userInput)
                for i in array:
                    location = fullWordArray.index(userInput)
                    array[location] = "*"

                array = [w.replace("*", userInput) for w in array]
                print(array)

                next_stage(tries)

            elif userInput not in fullWord:
                print("That letter is not in the word.")
                tries += 1
                next_stage(tries)

        else:
            print("You've already guessed that letter.")

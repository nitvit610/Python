def hang(word, guess, tries):
    for i in fullWord:
        if i == userInput:
            print("That letter is in the word.")
            guessed.append(i)
            next_stage(tries)
            break

        elif i in fullWord:
            print("That letter is not in the word.")
            guessed.append("_")
            tries += 1

            next_stage(tries)
            break


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
guesses = 0

while True:
    user = input("Guess a letter: ")
    if len(user) != 1:
        print("That is not a single letter.")
    else:
        userInput = user.lower()
        hang(userInput, guessed, guesses)





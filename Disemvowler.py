while True:
    string = input("Please input a string: ")

    noSpace = string.replace(" ", "")

    vowels = "aeiou"

    vowelCount = []

    for i in noSpace:
        if i in vowels:
            vowelCount.append(i)
            noSpace = noSpace.replace(i, "")

    print("\n" + noSpace)
    print("".join(vowelCount), "\n")

    again = input("Would you like to try again? ")
    againLow = again.lower()

    if againLow == "no" or againLow == "n":
        print("Thank you for playing.")
        break

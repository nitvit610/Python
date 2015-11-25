import random

while True:
    num = random.randint(1, 6)

    if num == 1:
        print("+--------+\n"
              "|        |\n"
              "|   O    |\n"
              "|        |\n"
              "+--------+\n")

    if num == 2:
        print("+--------+\n"
              "|     O  |\n"
              "|        |\n"
              "|  O     |\n"
              "+--------+\n")

    if num == 3:
        print("+--------+\n"
              "| O      |\n"
              "|   O    |\n"
              "|     O  |\n"
              "+--------+\n")

    if num == 4:
        print("+--------+\n"
              "| O    O |\n"
              "|        |\n"
              "| O    O |\n"
              "+--------+\n")

    if num == 5:
        print("+--------+\n"
              "| O    O |\n"
              "|   O    |\n"
              "| O    O |\n"
              "+--------+\n")

    if num == 6:
        print("+--------+\n"
              "| O    O |\n"
              "| O    O |\n"
              "| O    O |\n"
              "+--------+\n")

    againTrue = True
    while againTrue == True:
        again = input("Would you like to go again?: ")
        againLow = again.lower()

        if againLow == "yes" or "y":
            print("")

        elif againLow == "no" or againLow == "n":
            print("Thanks for playing.")
            againTrue = False

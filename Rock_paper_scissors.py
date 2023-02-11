import random


def rock_paper_scissors():
    player = input("Rock, paper or scissors: ")  # ask player for an input
    # somehow codify player's input (R = 1, P = 2, C = 3)
    computer = random.randint(1, 3)  # generate randomly integer 1, 2 or 3 (r, p, c)
    #  print(computer)
    while player == "Rock":
            if computer == 1:
                return print("You played Rock, the computer played Rock. It's a draw!")
            elif computer == 2:
                return print("You played Rock, the computer played Paper. You lose!")
            else:
                return print("You played Rock, the computer played Scissors. You win!")
    while player == "Paper":
            if computer == 1:
                return print("You played Paper, the computer played Rock. You win!")
            elif computer == 2:
                return print("You played Paper, the computer played Paper. It's a draw!")
            else:
                return print("You played Paper, the computer played Scissors. You lose!")
    while player == "Scissors":
            if computer == 1:
                return print("You played Scissors, the computer played Rock. You lose!")
            elif computer == 2:
                return print("You played Scissors, the computer played Paper. You win!")
            else:
                return print("You played Scissors, the computer played Scissors. It's a draw!")
    while player != "Rock" or "Paper" or "Scissors":
        return print("Not a correct input!")

rock_paper_scissors()
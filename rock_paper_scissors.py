import random
from colorama import Fore

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_score = 0
computer_score = 0
choose = input("Type [yes] to Play or [no] to quit: ")

while choose == 'yes':
    player_choose = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_choose == 'r':
        player_choose = rock
    elif player_choose == 'p':
        player_choose = paper
    elif player_choose == 's':
        player_choose = scissors
    else:
        raise SystemExit('Invalid Input. Try again...')

    computer_random_number = random.randint(1, 3)
    computer_choose = ''

    if computer_random_number == 1:
        computer_choose = rock
    elif computer_random_number == 2:
        computer_choose = paper
    else:
        computer_choose = scissors

    print(f"The computer choose {Fore.RED + computer_choose}.")

    if (player_choose == rock and computer_choose == scissors) or (player_choose == paper and computer_choose == rock) \
            or (player_choose == scissors and computer_choose == paper):
        print(Fore.GREEN + "You win!")
        player_score += 1
    elif player_choose == computer_choose:
        print(Fore.YELLOW + "Draw!")
    else:
        print(Fore.RED + "You lose!")
        computer_score += 1

    print(f"{Fore.WHITE + 'Score:'} {Fore.BLUE + str(player_score)} - {Fore.RED + str(computer_score)}")

    choose = input("Type [yes] to Play or [no] to quit: ")

if choose == "no":
    print("Thank you for playing!")



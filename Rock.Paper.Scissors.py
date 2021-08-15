import getpass
import random
from os import system

# ASCII Art
rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Define the possible moves that a person or the computer can take
possible_actions = ["r", "p", "s"]

# Print the banner
system('cls')
print("*******************************************")
print("WELCOME TO ABBIE'S ROCK PAPER SCISSORS GAME")
print("*******************************************")
print("")

# Single player or multiplayer mode
print("Option 1: Play against the computer")
print("Option 2: Two people play against each other")
option = input("Which Option do you pick? 1 or 2? ")
print("")

# Ask the user how many rounds to play
first_to = int(input("First to ___ wins. Enter a number: "))
print("")

# Ask for names
player1_name = input("Who is Player 1? ")
if option == "2":
    player2_name = input("Who is Player 2? ")
else:
    player2_name = "Computer"
system('cls')

# Scores start at zero
player1_score = 0
player2_score = 0

# Number of rounds starts at zero
round_count = 0

# Play until there is a winner
while player1_score < first_to and player2_score < first_to:
    # Increment the round counter
    round_count += 1

    # Display the current score
    print("")
    print("*****************************")
    print(f"{player1_name}'s Score: {player1_score}")
    print(f"{player2_name}'s Score: {player2_score}")
    print("*****************************")
    print("")

    # Display round count
    print(f"Round #{round_count}")

    # Ask the player(s) for their selection
    print("r = Rock")
    print("p = Paper")
    print("s = Scissors")
    player1_action = ""
    while player1_action != "r" and player1_action != "p" and player1_action != "s":
        if player1_action != "":
            print("Invalid option.  Try again")
        player1_action = getpass.getpass(prompt=f"{player1_name}: Enter a choice (r, p, s): ")
        player1_action = player1_action.lower()

    player2_action = ""
    if option == "2":
        while player2_action != "r" and player2_action != "p" and player2_action != "s":
            if player2_action != "":
                print("Invalid option.  Try again")
            player2_action = getpass.getpass(prompt=f"{player2_name}: Enter a choice (r, p, s): ")
            player2_action = player2_action.lower()
        system('cls')
    else:
        player2_action = random.choice(possible_actions)
        system('cls')

    # Tie
    if player1_action == player2_action:
        if player1_action == "r":
            print(f"{player1_name} plays rock!")
            print(rock_art)
            print(f"{player2_name} plays rock!")
            print(rock_art)
            print("Both players selected rock. It's a tie!")
        elif player1_action == "p":
            print(f"{player1_name} plays paper!")
            print(paper_art)
            print(f"{player2_name} plays paper!")
            print(paper_art)
            print("Both players selected paper. It's a tie!")
        else:
            print(f"{player1_name} plays scissors!")
            print(scissors_art)
            print(f"{player2_name} plays scissors!")
            print(scissors_art)
            print("Both players selected scissors. It's a tie!")

    # Player 1 picks rock
    elif player1_action == "r":
        if player2_action == "s":
            print(f"{player1_name} plays rock!")
            print(rock_art)
            print(f"{player2_name} plays scissors!")
            print(scissors_art)
            print(f"Rock smashes scissors! {player1_name} wins!")
            player1_score += 1
        else:
            print(f"{player1_name} plays rock!")
            print(rock_art)
            print(f"{player2_name} plays paper!")
            print(paper_art)
            print(f"Paper covers rock! {player2_name} wins!")
            player2_score += 1

    # Player 1 picks paper
    elif player1_action == "p":
        if player2_action == "r":
            print(f"{player1_name} plays paper!")
            print(paper_art)
            print(f"{player2_name} plays rock!")
            print(rock_art)
            print(f"Paper covers rock! {player1_name} win!")
            player1_score += 1
        else:
            print(f"{player1_name} plays paper!")
            print(paper_art)
            print(f"{player2_name} plays scissors!")
            print(scissors_art)
            print(f"Scissors cuts paper! {player2_name} wins!")
            player2_score += 1

    # Player 1 picks scissors
    elif player1_action == "s":
        if player2_action == "p":
            print(f"{player1_name} plays scissors!")
            print(scissors_art)
            print(f"{player2_name} plays paper!")
            print(paper_art)
            print(f"Scissors cuts paper! {player1_name} wins!")
            player1_score += 1
        else:
            print(f"{player1_name} plays scissors!")
            print(scissors_art)
            print(f"{player2_name} plays rock!")
            print(rock_art)
            print(f"Rock smashes scissors! {player2_name} wins!")
            player2_score += 1

print("")
print("*********************")
print("FINAL SCORE")
print(f"{player1_name}'s Score: {player1_score}")
print(f"{player2_name}'s Score: {player2_score}")
print("*********************")
input()

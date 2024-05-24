from random import choice

# create a list of play options
plays = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def get_verb(winner, loser):
    verbs = {
        "Rock": {"Scissors": "crushes", "Lizard": "crushes"},
        "Paper": {"Rock": "covers", "Spock": "disproves"},
        "Scissors": {"Paper": "cuts", "Lizard": "decapitates"},
        "Lizard": {"Spock": "poisons", "Paper": "eats"},
        "Spock": {"Rock": "vaporizes", "Scissors": "smashes"}
    }
    return verbs[winner][loser]

while True:
    computer = choice(plays) # assign a random play to the computer

    player = input("Rock, Paper, Scissors, Lizard, or Spock? (Type 'exit' to quit) ").capitalize()  # get player's choice
    if player.lower() == 'exit':  # check if the player wants to exit
        print("Thanks for playing!")
        break

    if player not in plays:  # check if the input is valid
        print("That's not a valid play. Please choose Rock, Paper, Scissors, Lizard, or Spock.")
        continue

    if player == computer:
        print("Tie!")
    elif (player == "Rock" and (computer == "Scissors" or computer == "Lizard")) \
        or (player == "Paper" and (computer == "Rock" or computer == "Spock")) \
        or (player == "Scissors" and (computer == "Paper" or computer == "Lizard")) \
        or (player == "Lizard" and (computer == "Spock" or computer == "Paper")) \
        or (player == "Spock" and (computer == "Rock" or computer == "Scissors")):
        print(f"You win! {player} {get_verb(player, computer)} {computer}.")
    else:
        print(f"You lose! {computer} {get_verb(computer, player)} {player}.") 
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break


def get_verb(winner, loser):
    verbs = {
        "Rock": {"Scissors": "crushes", "Lizard": "crushes"},
        "Paper": {"Rock": "covers", "Spock": "disproves"},
        "Scissors": {"Paper": "cuts", "Lizard": "decapitates"},
        "Lizard": {"Spock": "poisons", "Paper": "eats"},
        "Spock": {"Rock": "vaporizes", "Scissors": "smashes"}
    }
    return verbs[winner][loser]

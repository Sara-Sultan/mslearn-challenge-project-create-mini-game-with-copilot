# create minigame app
# Rock beats scissors.  Scissors beat paper.  Paper beats rock.
# user input rock, paper, or scissors and should warned if choose invalid option
# the user input should be case insensitive
# # computer randomly selects rock, paper, or scissors
# compare user and computer selections and determine winner
# display winner and ask if user wants to play again
# if user wants to play again, repeat the game
# if user does not want to play again, display goodbye message
# use functions to implement the game
# use random module to select computer choice
# use while loop to play multiple games
# use input() function to get user input
# use print() function to display messages to user
# use string formatting to display the winner
# use if, elif, else statements to compare user and computer choices
# use break statement to exit the loop
# use lower() string method to make user input case insensitive
# use time.sleep() function to slow down the game

import random
import time

def get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        if user_choice.lower() in ['rock', 'paper', 'scissors']:
            return user_choice.lower()
        else:
            print("Invalid choice.  Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chooses {computer_choice}.")
    time.sleep(1)
    print(determine_winner(user_choice, computer_choice))

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'no':
        print("Goodbye!")
        break
    print()

# Run the app
# python app.py
# Enter rock, paper, or scissors: rock
# Computer chooses scissors.
# You win!
# Do you want to play again? (yes/no): yes
# Enter rock, paper, or scissors: paper



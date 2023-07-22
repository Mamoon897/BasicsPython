import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Let's play Rock-Paper-Scissors!")
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = get_computer_choice()

if user_choice in ["rock", "paper", "scissors"]:
    print(f"Computer chooses {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))
else:
    print("Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")


import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    outcomes = {
        "rock": {"scissors": "win", "paper": "lose"},
        "paper": {"rock": "win", "scissors": "lose"},
        "scissors": {"paper": "win", "rock": "lose"}
    }
    if player == computer:
        return "tie"
    return outcomes[player][computer]

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    #print("Enter 'rock', 'paper', or 'scissors' to play or 'exit' to Quit the game.")

    while True:
        print("Enter 'rock', 'paper', or 'scissors' to play or 'exit' to Quit the game.")
        player_choice = input("Your choice: ").lower()

        if player_choice == "exit".lower():
            print("Thanks for playing! Goodbye!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")
        print()

play_game()

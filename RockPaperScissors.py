import random


def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 wins! Type 'rock', 'paper', or 'scissors'.\n")

    while user_score < 5 and computer_score < 5:
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")

    if user_score == 5:
        print("🎉 Congratulations! You're the champion!")
    else:
        print("Computer wins the game!")

    print("\nThanks for playing!")



rock_paper_scissors()
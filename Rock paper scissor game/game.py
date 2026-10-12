import random
item_list = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(item_list)

print(f"Your choice: {user_choice}, computer's choice: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

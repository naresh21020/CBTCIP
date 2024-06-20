import random

options = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, scissors): ").lower() 
computer_choice = random.choice(options)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice=="rock" and computer_choice=="scissor":
    print("you win")
elif user_choice=="paper" and computer_choice=="rock":
    print("you win")
elif user_choice=="scissors" and computer_choice=="paper":
    print("you win")
else:
    print("Computer wins!")

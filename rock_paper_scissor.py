import random

user_point = 0
computer_point = 0

print("Welcome to Rock_Paper_Scissors Game \n\n")

while True:
    print("Let's start")

    user_input = input ("Enter your choice (rock, paper, scissors) ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(possible_choices)

    print(f"you chose {user_input}, computer chose {computer_input} \n\n")

    if user_input == computer_input :
        print(f"Its a Draw as both selected {user_input} \n\n")
    elif user_input == "rock":
        if computer_input == "scissors":
            print("User wins, Rock will break the scissors \n\n")
            user_point +=1
        else :
         print("User lose, Paper will cover rock \n\n")
         computer_point +=1

    elif user_input == "paper":
        if computer_input == "rock":
            print("User wins, Paper will cover the rock \n\n")
            user_point +=1
        else :
            print("User lose, Scissors will cut the paper \n\n")
            computer_point +=1

    elif user_input == "scissors":
        if computer_input == "paper":
         print("User wins, Scissors will cut the paper \n\n")
         user_point +=1
        else :
            print("User lose, Rock will break the scissors \n\n")
            computer_point +=1

    play_again = input ("Wanna play again? (YES/NO): \n\n")
    if play_again.lower() != "YES":
     break

print(f"User's Score: {user_point}  Computer's Score: {computer_point} \n\n")
print("Game Over")
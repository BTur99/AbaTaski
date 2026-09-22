from random import choice
import os

ch = ["rock", "paper", "scissors"]
player_points = 0
pc_points = 0


while True:
    player_choice = input("rock/paper/scissors: ").lower()
    os.system("cls")
    pc_choice = choice(ch).lower()
    print(f"pc choice: {pc_choice}")
    if player_choice == pc_choice:
        print("Nichya")
    elif (player_choice == "rock" and pc_choice == "paper") or (player_choice == "paper" and pc_choice == "scissors") or (player_choice == "scissors" and pc_choice == "rock"):
        pc_points += 1
        print("PC win round")
    else:
        player_points += 1
        print("You win round")

    print(pc_points, '|', player_points)

    if pc_points == 3 or player_points == 3:
        restart = input("Want restart? y/n: ")
        if restart == "y":
            pc_points = 0
            player_points = 0
        else:
            break
    
if player_points > pc_points:
    print("you win", pc_points, '|', player_points)
elif player_points < pc_points:
    print("pc win", pc_points, '|', player_points)


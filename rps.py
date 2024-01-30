import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:


  
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper,\n3 for scissors:\n\n")

    player = int(playerchoice)

    if player < 1  or player > 3: 
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

   
    print("\nYou chose " + str(RPS(player)).replace('RPS.','' ) +".")
    print("python chose" + str(RPS(computer)).replace('RPS.','' ) +".\n")
    

    if player == 1 and computer == 3:
        print("you win!")
    elif player == 2 and computer == 1:
        print("you win!")
    elif player == 3 and computer == 2:
        print("you win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("python wins!")    

    playagain = input("\nPlay again? \nY for Yes or \nQ to quit\n\n")  
    if playagain.lower() == "y":
        continue
    else:
        print("\ncelebration") 

        print("Thank you for playing again!\n")

        playagain = False


sys.exit ("Bye!!!!!!!!!!!")    

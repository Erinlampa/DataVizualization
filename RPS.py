# Incorporate the random library
import random

# Initial variable to track game play
user_play = "n"

# While we are still playing...
while user_play == "y":

# Print Game 
print("Let's play a game of Rock, Paper, Scissors, Lizard, Spock!")


# Specify the three options
options = ["r", "p", "s", "l", "sp"]

# Computer Selection
computer_choice = random.choice(options)

#Ask for selection
user_choice = input("Do you choose Rock(r), Paper(p), Scissors(s), Lizard (l), or Spock(sp)?")

#Resuts for user choosing Paper
if(user_choice =="p" and computer_choice == "p"):
    print("Computer chose " + computer_choice + ", so -- You TIE!")
elif(user_choice=="p" and computer_choice =="s"):
    print("Computer chose " + computer_choice + " -- You LOSE!")
elif(user_choice=="p" and computer_choice =="r"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice=="p" and computer_choice =="l"):
    print("Computer chose " + computer_choice + " -- You LOSE!")
elif(user_choice=="p" and computer_choice =="sp"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 

#Resuts for user choosing Rock
elif(user_choice=="r" and computer_choice =="s"):
    print("Computer chose " + computer_choice + " -- You LOSE!")
elif(user_choice=="r" and computer_choice =="r"):
    print("The Computer chose " + computer_choice + ", so  -- You TIE!") 
elif(user_choice=="r" and computer_choice =="p"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice=="r" and computer_choice =="l"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice=="r" and computer_choice =="sp"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!") 

#Resuts for user choosing Scissors
elif(user_choice=="s" and computer_choice =="s"):
    print("Computer chose " + computer_choice + " -- You TIE")
elif(user_choice=="s" and computer_choice =="r"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!") 
elif(user_choice=="s" and computer_choice =="p"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice=="s" and computer_choice =="l"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice=="s" and computer_choice =="sp"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!") 

#Results for Choosing Lizard
elif(user_choice=="l" and computer_choice =="l"):
    print("Computer chose " + computer_choice + " -- You TIE")
elif(user_choice=="l" and computer_choice =="r"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!") 
elif(user_choice=="l" and computer_choice =="p"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice=="l" and computer_choice =="s"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!") 
elif(user_choice=="l" and computer_choice =="sp"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!")

#Resuts for user choosing Spock
elif(user_choice =="sp" and computer_choice =="sp"):
    print("Computer chose " + computer_choice + " -- You TIE!")
elif(user_choice =="sp" and computer_choice =="r"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice =="sp" and computer_choice =="p"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!") 
elif(user_choice =="sp" and computer_choice =="s"):
    print("The Computer chose " + computer_choice + ", so  -- You WIN!") 
elif(user_choice =="sp" and computer_choice =="l"):
    print("The Computer chose " + computer_choice + ", so  -- You LOSE!")

   # Once complete...
    user_play = input("Do you want to Continue: (y)es or (n)o? ")

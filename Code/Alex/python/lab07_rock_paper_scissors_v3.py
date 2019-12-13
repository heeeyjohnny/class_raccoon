'''
Lab 7: Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
Version 2 (optional)

After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

Version 3 (optional)

Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/
'''



#i imported the random module to enable the computer to play back using a random choice of the given strings
import random

#intro statement into rock paper scissors game
print("It's time to get down with some rock, paper, scissors, lizard, spock.")


#possible choices listed as seperate strings within a variable
move_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']

#for v2 i selected a variable for the user if they chose to play the game again. In order to start the while loop again.
play_again = "yes"
while play_again == "yes":

#I utilized the variable above to give the user choices to choose from and then input into the calculation.
    user_move_choice = input(f"\nChoose {move_list[0]}, {move_list[1]}, {move_list[2]}, {move_list[3]}, or {move_list[-1]} to continue. ")

#this is the computer's calculation for it's choice. Again I utilized the variable representing the valid choices in order to play.
    computer_move_choice = random.choice(move_list)

#the game begins with the computers response to the input from the user and lists the choices neatly to be evaluated.
    print(f"\nI used {computer_move_choice} and you used {user_move_choice}.\n")


    if computer_move_choice == move_list[0]: #computer chooses 'rock'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nIt's a tie!\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nYou've won this round..\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nHah! I'm better than you!\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nI crushed your lizard with a rock. I win.\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nWhat? Spock vaporized my rock! I guess you win..\n")

    elif computer_move_choice == move_list[1]: #computer chooses 'paper'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nSorry Charlie.\nI win.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nSo it's a tie..\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nAlright, i give up.. you win\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nYou've won. Your lizard ate my paper\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nPaper disproves Spock. \nYou loose.\n")

    elif computer_move_choice == move_list[2]: #computer chooses 'scissors'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nYou win.\nI loose.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nI win.\nYou loose.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nquit copying me.\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nI decapitated your lizard with my scissors.\nYou loose.\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nSpock smashes scissors. \nYou win.\n")

    elif computer_move_choice == move_list[3]: #computer chooses 'lizard'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nYour rock crushed my lizard.\nYou win.\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nMy lizard ate your paper.\nI win.\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nHow dare you decapitate my lizard!\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nWe've tied.\n But my lizard is cooler than yours.\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nLizard poisons Spock.. duh!\n You loose.\n")

    elif computer_move_choice == move_list[4]: #computer chooses 'spock'
        if user_move_choice == move_list[0]: #user chooses 'rock'
            print("\nSpock vaporizes rock.\n I win!\n")
        elif user_move_choice == move_list[1]: #user chooses 'paper'
            print("\nYou win. Paper disproves Spock\n")
        elif user_move_choice == move_list[2]: #user chooses 'scissors'
            print("\nSpock smashes scissors.\n You loose.\n")
        elif user_move_choice == move_list[3]: #user chooses 'lizard'
            print("\nYou win i guess\n")
        elif user_move_choice == move_list[4]: #user chooses 'spock'
            print("\nIt's a tie. Spock... meet Spock.\n")

#v2 addition. i used the user input to ask if they wanted to play again and then created a while loop incase of invalid entry
    play_again = input("Would you like to play again?\n").lower()

#I kept it inside the original while loop in order to give them the option of whether or not they wanted to leave the game.
    while play_again != "no" and play_again != "yes":
        print(f"\ninvalid input.")

        play_again = input("\nWould you like to play again?\n").lower()

        if play_again == "no":
            break

#ending while loop
else:
    print("\nokay bye\n╭∩╮(ツ)_/¯\n")#classraccoon
'''*not complete*
Lab 11: Guess the Number

Version 2

Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
'''


import random

print("\n\n\n\n\n\n\n\nLet's play 'Guess the Number'. The computer will guess a random int between 1 and 10. You can then try to guess the number, and the program will tell you whether you are right or wrong.\n\n")

computer_choice = random.randint(1,10)#might need to be 11


user_guess = input("Guess the number or type 'done' to cancel: ")

counter = 0

while user_guess != "done":

    counter += 1

    if int(user_guess) != computer_choice:
        print("\ntry again!\n\n")

    if int(user_guess) == computer_choice:
        print("\nYou guessed my number! Good job\n\n")
        print(f"It took you {counter} tries to guess my number.\n\n")
        if counter <= 3:
            print("Not bad\n\n\n")
        if counter > 3:
            print("I think you can do better..\n\n\n")

    user_guess = input("Guess the number or type 'done' to cancel: ")

#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 21, 2025
# This program creates a guessing game with number range 0-9.

# Imports the random module for random generators.
import random


def main():
    # Set the correct number to a random number between 0 and 9.
    correct_number = random.randint(0, 9)

    # Get the chosen number from the user.
    chosen_number = int(input("Guess a number between 0 and 9: "))

    # Check if the user chose the correct number.
    if chosen_number == correct_number:
        # Displays they got it correct.
        print("You guessed correct!")
    # Otherwise, check if the user did not choose the correct number.
    else:
        # Displays they got it wrong, and they must try again.
        print(f"You guessed wrong! The correct answer was {correct_number}.")


if __name__ == "__main__":
    main()

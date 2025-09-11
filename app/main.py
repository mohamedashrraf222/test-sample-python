# app/main.py

import random
import sys

def print_welcome_message():
    """Prints the initial welcome message and instructions."""
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'exit' to quit at any time.")

def get_user_guess():
    """Prompts the user for their guess and returns the input."""
    return input("Enter your guess: ")

def evaluate_guess(guess, secret_number):
    """
    Compares the user's guess to the secret number, provides feedback,
    and returns True if the guess is correct, otherwise False.
    """
    if guess < secret_number:
        print("Too low! Try again.")
        return False
    elif guess > secret_number:
        print("Too high! Try again.")
        return False
    else:
        return True

def game_loop():
    """Contains the main logic for a single round of the game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = get_user_guess()

        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break

        try:
            guess = int(user_input)
            attempts += 1
            if evaluate_guess(guess, secret_number):
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    """The main entry point for the application."""
    try:
        print_welcome_message()
        game_loop()
    except KeyboardInterrupt:
        print("\nThanks for playing!")
        sys.exit()

if __name__ == "__main__":
    main()
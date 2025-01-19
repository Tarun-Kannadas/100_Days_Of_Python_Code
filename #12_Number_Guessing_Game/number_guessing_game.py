from art import logo
from random import randint

LEVEL_EASY = 10
LEVEL_HARD = 5

def check_answer(user_guess,actual_answer, turns):
    """Check answers against the guess, returns the number of turns"""
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    elif user_guess == actual_answer:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    """Setting the difficulty for the player"""
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if mode == "easy":
        return LEVEL_EASY
    elif mode == "hard":
        return LEVEL_HARD

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out of guess, You lose!")
            return
        elif guess != answer:
            print("Guess Again.")

game()
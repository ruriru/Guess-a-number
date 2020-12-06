from random import randint
from art import logo


EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print("You got it! You guessed! :)")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print("""Welcome to the Guessing Game!
    I'm thinking of a number from 1 to 100""")
    answer = randint(1, 100)
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return 
        elif guess != answer:
            print("Guess again.")

game()
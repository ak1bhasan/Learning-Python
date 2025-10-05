from random import randint
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return -1


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(art.logo)
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses, you lose.")
            print(f"The real answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")
        elif turns == -1:
            return


game()
while input("Do you want to play again? Type 'y' or 'n': ").lower() == 'y':
    print("\n"*30)
    game()

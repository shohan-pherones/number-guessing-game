import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    target_number = random.randint(1,100)
    attempts = set_difficulty()
    return target_number, attempts

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def play_game():
    target_number, attempts = start_game()
    guessed = False

    while not guessed and attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if guess == target_number:
            print("You got it! The answer was", target_number)
            guessed = True
        elif guess < target_number:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1
        if attempts == 0 and not guessed:
            print("You've run out of attempts. You lose! The number was", target_number)

def main():
    while input("Do you want to play the Number Guessing Game? Type 'yes' or 'no': ").lower() == "yes":
        play_game()
    print("Thanks for playing!")

main()
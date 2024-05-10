import random

def generate_random_number():
    return random.randint(1, 10)


def play_guessing_game():

    while True:
        random_number = generate_random_number()
        guess = input("Guess number between 1 and 10 (enter 0 to quit): ")

        if guess == '0':
            print("Game over")
            break

        guess = int(guess)
        if guess == random_number:
            print("Congratulations! You've made it!")
        else:
            print(f"Sorry, the number was {random_number}. Try again.")


if __name__ == "__main__":
    play_guessing_game()
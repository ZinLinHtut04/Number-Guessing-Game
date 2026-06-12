import random

secret = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input("Enter your guess(1-100): "))
    guess_count += 1

    if guess == secret:
        print(f"\nCorrect!")
        print(f"The number was {secret}")
        print(f"It took you {guess_count} guesses.")
        break

    elif guess < secret:
        if guess >= secret - 10:
            print("Low!")
        else:
            print("Too low!")

    else:
        if guess <= secret + 10:
            print("High!")
        else:
            print("Too high!")
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randrange(1, 10)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Guess a number between 1 and 9. To end enter 'exit': ")

    if guess == "exit":
        print("Game Over")
        break

    guess = int(guess)
    count += 1
    if guess not in range(1, 10):
        print("Guess a number between 1 and 9!")
    elif guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        if count == 1:
            print("Great Job! You've got it first try!")
        elif count <= 3:
            print("Excellent! You've got it in just {} tries".format(count))
        elif count > 3:
            print("Finally! It took you {} tries!".format(count))
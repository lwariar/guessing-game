"""A number-guessing game."""

# Put your code here
from random import randint

count = 0
random_number = randint(1, 100)

print("What's your name?'")

name = input('<type in your name> ')

while True:
    guess = input('What is your guess? ')

    # convert the input string into an integer
    g = int(guess)

    # check if the input is a valid number
    """if int(guess) == ValueError:
        print("Not a valid number")
        continue
    """

    # check if the guess is between 1 and 100
    if g < 1 and g > 100:
        print('Please guess a number between 1 and 100')
        continue

    # increment the counter
    count += 1  

    if g < random_number:
        print('Your guess is too low.')

    elif g > random_number:
        print('Your guess is too high.')

    else:
        print(f'Yay, {name}!')
        print(f'You guessed the number in {count} tries!')
        break


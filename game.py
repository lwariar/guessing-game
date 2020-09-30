"""A number-guessing game."""

# Put your code here
from random import randint

count = 0
random_number = randint(1, 100)

print("What's your name?'")

name = input('<type in your name> ')

while True:
    guess = input('What is your guess? ')

    # check if the input is a valid number
    if ! int(guess):
        print("Not a valid number")
        continue
    """try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a valid number, try again.')
        continue
    """

    # check if the guess is between 1 and 100
    if guess < 1 and guess > 100:
        print('Please guess a number between 1 and 100')
        continue

    # increment the counter
    count += 1  

    if guess < random_number:
        print('Your guess is too low.')

    elif guess > randon_number:
        print('Your guess is too high.')

    else:
        print(f'Yay, {name}!')
        print(f'You guessed the number in {tries} tries!')
        break


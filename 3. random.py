import random

the_number = random.randint(0,100)
guess = -1

while guess != the_number:
    guess_text = input('Guess a number?')
    guess = int(guess_text)
    if guess < the_number:
        print('too low')
    elif guess > the_number:
        print('too high')
    else:
        print('you win!')
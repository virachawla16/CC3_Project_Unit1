import random

n = random.randint(1, 10)
count = 1   # this is used to tell the player how many times it took them to guess the correct number
introduction = ('Hi there', 'Welcome', 'Hey')
greeting = random.choice(introduction)

name = raw_input(greeting + ', What is your name?' + ":")
print()

print(greeting + " " + name + "! " + 'Welcome to Guess A Random Number.')
print()
print('In this game, I will generate a random number between 1-10 and you have to guess what number I chose. Enjoy!!')
print()
print('I am now choosing a number between 1-10.')
print()

while True:
    guesses = input('Go on, guess a number between 1-10!: ')
    guesses = int(guesses)  # this makes the player input into an integer as initally whatever the player inputs is a string

    if guesses == n:
        print('Good job! You guessed correctly!')
        break # this terminates the current loop

    elif guesses < n:
        print('Oops! You guessed too low. Try again!')
        count += 1

    else:
        print('Oops! You guessed too high. Try again!')
        count += 1

print('It took you' , count, 'tries! Not bad')

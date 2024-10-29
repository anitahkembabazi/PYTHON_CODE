import random

secretnumber= random.randint(1,20)

print('Welcome!')
print('I am thinking of number between 1 and 20')

guesses=0
guess=0
while guess != secretnumber:
    print('Take a guess.')
    guess =int(input())

    guesses+= 1
    if guess < secretnumber:
        print('Your guess is too low.')
    elif guess > secretnumber:
        print('Your guess is too high.')
    else:
        break

# Check if the guess is correct
if guess == secretnumber:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretnumber))
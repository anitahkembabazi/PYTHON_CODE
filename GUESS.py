import random
secretnumber=random.randint(1,30)
print('Welcome to the Gaming class')
print("I am thinking of a number between 1 and 30")
guesses=0
for guesses in range(1,6):
    print("take a guess")
    guess =int(input())
    if guess< secretnumber:
        print('Your guess is too low') 
    elif guess> secretnumber:
        print('Your guess is too high.')   
    else:
        break


if guess ==secretnumber:
 print("Good job ! You guessed my number in " + str(guessestaken) + 'guesses!')   
else:
   print('Nope! The number I was thinking of was ' + str(secretnumber) )




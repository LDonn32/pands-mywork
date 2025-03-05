# Extra: get the program to generate a random number 
# between 0 and 100 to guess

# Resource: 
# https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/


import random
a=random.randint(1,100)
print(a)

numberToGuess = a

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # It can't be equal or too low, so it must be too h
        print( "too high")
    guess = int(input("Please guess again:"))

print("Well Done! Yes the number was ", numberToGuess)
# modified guess1.py to tell the user if the guess
# is too high or too low
# each time they guess

#Author: Laura Donnelly

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # It can't be equal or too low, so it must be too high
        print( "too high")
    guess = int(input("Please guess again:"))

print("Well Done! Yes the number was ", numberToGuess)
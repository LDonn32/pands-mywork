# prompts user to guess a nummber
# program should keep prompting user to guess number
# until they get it right

# Author: Laura Donnelly

numberToGuess = 30

guess = int(input("Please guess the number:"))

while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was 30", numberToGuess)

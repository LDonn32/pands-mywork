# rounds a number 
# rounds to the nearest even number 
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# not to be used when accuracy is essential 
# Author: Laura Donnelly

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ('{} rounded is {}'.format(numberToRound,roundedNumber))
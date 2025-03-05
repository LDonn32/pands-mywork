# This program asks user to enter in a number
# Program will tell the user if the number is even or odd

# Author: Laura Donnelly

number = int(input("enter an integer"))

if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")
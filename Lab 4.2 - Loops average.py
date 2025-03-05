# program keeps reading numbers until user enters a 0
# Program should append each of them to a list
# Program should print out each of the numbers entered
# And average them

# use a list

# Author:Laura Donnelly

numbers = []

# first number then we check if it is a 0 in the while loop
number = int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))
                 
for value in numbers:
    print (value)

# I want avergae to be a float
average = float(sum(numbers)) / len(numbers)
print (f"The Average is {average}")
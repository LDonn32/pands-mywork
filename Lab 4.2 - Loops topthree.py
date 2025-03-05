# This program generates 10 random numbers
# prints them out, then
# prints out the top 3

# Use a list to store and manipulate the numbers

# Author: Laura Donnelly

import random
# programming the general case
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))
print (f"{howMany} random numbers\t {numbers}")

# keep the original list maybe dont need to 

topOnes = numbers.copy()

topOnes.sort(reverse = True)

print ("The Top {topHowMany} are \t\t {topOnes[0:topHowMany]}")
# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all letters to lower case.
# It then outputs the leghts of the original string
# and the normalised one

# Author: Laura Donnelly

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print(f"That string normalised is :{normalisedString}")
print(f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")
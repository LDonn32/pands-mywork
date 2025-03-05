# This program reads in 
# a students persentage
# and prints out the 
# corresponding grade

# Author: Laura Donnelly
percentage = float(input("Enter the percentage: "))
# print (percentage)

# be careful with ands and ors

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")

# Extra (I will not give the answer to these) 
# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction.  
# How would you modify the program in 1 to deal with this? 




# How would you use a while loop to modify 1 so that it keeps prompting the user for a number until the user enters -1
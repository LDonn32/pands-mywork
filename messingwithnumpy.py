# Messing with numpy
#Author: Laura Donnelly

# Numpy can only store one variable type at a time.
# If you add strings, or floats, 
# all the variables will be converted to the one variable type


import numpy as np

list_of_numbers= [1,2,3,5,"asdf"]

print(list_of_numbers)

numbers = np.array([1,2,3,4,])
numbers = numbers * [1,2,3,5]

print("array", numbers)

rando = np.random.randint(100,200,30)
print(rando)
normalrando = np.random.normal(loc= 50,scale= 20, size=100)
print(normalrando)
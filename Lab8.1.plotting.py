
import matplotlib.pyplot as plt
import numpy as np
# it is good practice to have your absolute variables
# at the beginning of the program
minSalary = 20000
maxSalary = 80000
numberOfEnteries = 10

np.random.seed(1) # this line is so the random numbers are the same each time. Easier to debug
salaries = np.random.randint(minSalary, maxSalary, numberOfEnteries)
'''
salariesPlus = salaries + 5000 # this will add 5000 to each value
print(salariesPlus)
'''
'''
# can also multiply
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)
# this is a float array, i convert it to an int array
newSalaries = salariesMult.astype(int)
print(newSalaries)
'''

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEnteries)

plt.hist(salaries)
plt.show()
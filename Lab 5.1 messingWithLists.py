# Messing with lists
# Author: Laura Donnelly

boats = ['Sigma', 23, [1,2,3], {} ]

for boat in boats:
    print(type(boat))
    
ages =[12,21,23,34]

sum = 0
for age in ages:
    sum += age
print(sum)

lenght_of_list = len(ages)
for i in range (0, lenght_of_list):
    sum += ages[i]
print(sum)

string = "1234567890"
print(string[6:])
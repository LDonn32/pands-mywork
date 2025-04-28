# Use person Module 
# Author: Laura Donnelly

from personmodule import *

person1 = {
    'firstname' : 'Laura',
    'lastname' : 'Donnelly',
    'dob' : dt.date(1995,1,2),
    'height' :  170,
    'width' : 900
}
displayperson(person1)
gethealthdata(person1)
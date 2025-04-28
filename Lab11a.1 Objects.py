# Demonstration of a module
# Author: Laura Donnelly

import datetime as dt


def gethealthdata(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)

if __name__ == "__main__":
    person1 = {
        'firstname' : 'Laura',
        'lastname' : 'Donnelly',
        'dob' : dt.date(1995,1,2),
        'height' :  170,
        'width' : 900
    }
    displayperson(person1)
    gethealthdata(person1)




def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("Enter the first Module name (blank to quit)").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName  # Corrected this line
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        
        moduleName = input("Enter next module name (blank to quit):").strip()

    return modules

def doView(students):
    if not students:
        print("No students to display.")
    else:
        for student in students:
            print(f"\nStudent Name: {student['name']}")
            print("Modules and Grades:")
            for module in student["modules"]:
                print(f"\tModule: {module['name']}, Grade: {module['grade']}")

# Main program
students = []

choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)  # Pass the students list to doAdd
    elif choice == 'v':
        doView(students)  # Pass the students list to doView
    elif choice != 'q':
        print("\n\nPlease select either a, v, or q.")
    choice = displayMenu()












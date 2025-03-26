# read in two number and multiple them 

def readNum(message = "enter a number"):
    num = False
    while (not num):
        try:
            num = int(input("enter a number: "))
        except ValueError:
            print("that was not a number ", ends="")
    return num

num1 = readNum()
num2 = readNum("enter num2:")


answer = num1 * num2

print(f"answer is {answer}")


# writing this code means it is reusable
# simpler code in long run as we can make changes easier 

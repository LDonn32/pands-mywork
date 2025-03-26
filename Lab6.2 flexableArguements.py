# messing with more functions
# flexible arguements

print(1,2,3, sep="", end="\t")
print("hi")

def fun1(*args):
    print(type(args))
    for val in args:
        print(val)
fun1("a", "b", "c")

# keyword arguements 
def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # for val in args:
    #print(val)

    fun2(name="joe", age=21, gender= "M")

# sample code
def ave(*values):
    number_of_values = len(values)
    sum = 0
    for value in values:
        sum+= value

    average = sum / number_of_values
    return average , sum

av1, sum_of_numbers = ave(1,2,3,4,5,6)
print(f"{av1} and sum is {sum_of_numbers}")


# Return Values 
# Return a variable but it can be:
# Of any type or 
# A tuple of variables

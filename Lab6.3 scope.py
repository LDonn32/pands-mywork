# messing with more functions
# variable scope

# dont do this 

x = 999

def fun():
    print(x)

def fun2(x2):
    print(f"in fun 2 x {x}")
    global x = 21
    print(f"in fun 2 x {x2}")

fun2(x)
print(f"after fun2 x is {x}")
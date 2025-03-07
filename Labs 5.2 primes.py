# generates primes
# Author: Laura Donnelly

primes = [] # instead of printing store in a list
upto = 100000

for candidate in range(2, upto): # checks all these numbers
    print(candidate)
    isPrime = True 
    # only need to check if dividable by prime
    for divisor in range(2, candidate):
        # if divisable by an int it is not a prime num
        if (candidate % divisor == 0):
            isPrime = False 
            # so there is no reason to keep checking
            break # break will jump out of the fall loop if nothing left to check 
        
    if isPrime:
        primes.append(candidate)

print(primes)
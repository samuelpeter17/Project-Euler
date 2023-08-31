import math
import timeit

#Largest prime factor
def largesPrimeFactor(num):
    #list of factors except one, starts with the number since every number is a factor of itself
    factors = [num]
    
    #Get all available other factors
    #Logic: Start searching from 2 for factors. If a factor(x) is found, add x and it counterpart(num/x).
    #       By searching if x or num/x already exists in the list of factors, we can identify when we have crossed
    #       the halfway point in a sorted list of factors for num. If one half is x, the other half would be num/x.
    #       Hence, by stopping once we see an overlap, we know we found all the factors and any result now would be redundant.
    x = 2
    while x<=(num/2):
        if (num%x) == 0:
            if int(x) not in factors:
                factors.append(int(x))
            else:
                break
            if int(num/x) not in factors:
                factors.append(int(num/x))
            else:
                break
        x = x + 1
    
    #Remove non prime factors    
    for a in range (len(factors)-1,-1,-1):
        if not isPrime(factors[a]):
            factors.pop(a)

    #print largest prime factor from list of available prime factors
    print(max(factors))

#Helper function to calculate whether a number is a prime or not    
def isPrime(num):
    if (num%2) == 0:
        return False
    else:
        sqroot = int(math.sqrt(num))
        x = 3
        while x<=sqroot:
            if (num%x) == 0:
                return False
            x = x + 2
        return True
    
#Function call
startTime = timeit.default_timer()
largesPrimeFactor(600851475143)
endTime = timeit.default_timer()

runTime = (endTime - startTime)*1000
print("Runtime : ", runTime, " ms.")        #Fastest runtime: 228.6353000017698  ms

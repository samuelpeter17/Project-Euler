import timeit

#10001st prime number
def calc(n):
  primes = [2]  #add 2 and check only odd numbers
  x = 3         #temporary variable
  k = 0         #flag to notify if a number is divisible by any prime
  while len(primes) < n:    #Check while length of list of primes is less than the desired number
    for i in primes:
      if (x%i) == 0:    #If x is divisible by i in primes
        k = 1           #Raise the flag and break
        break
    if k == 1:          #If flag is raised, lower it and move onto the next odd number
      x = x + 2
      k = 0
    else:               #Else, the number is a prime. Add x to the list of primes.
      primes.append(x)
  print(primes[n-1])
  
#Function call
startTime = timeit.default_timer()    
calc(10001)
endTime = timeit.default_timer()

runTime = (endTime - startTime)*1000
print("Runtime : ", runTime, " ms")        #Fastest runtime: 8780.195500003174  ms

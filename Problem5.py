import timeit

#Smallest multiple
def calc():
    # Start at 2520 as it could be smallest multiple of 1-20
    num = 2520
    factors = list(range(1,21))     #list of factors
    k = 0
    while (k == 0): #While the flag stays down
        #Go through the list of factors
        for i in factors:
            x = num % i         #Calculate the remainder from division
            if i == 20:         #If the factor is 20 
                #With no remainder, raise the flag.
                if x == 0:
                    k = 1
                    break
                else:           #Else, keep it down and break to the next number.
                    k = 0
                    break
            else:               #If there is a remainder with any other factor, break and move onto the next number.
                if x != 0:
                    k = 0
                    break
        
        #If out of for loop and flag is down, increment num.
        if k == 0:
            num = num + 1
        else:       #Else, the smallest multiple of 1-20 is found.
            break
    print(num, " is the answer.")
            
#Function call
startTime = timeit.default_timer()
print(startTime)
calc()
endTime = timeit.default_timer()

runTime = (endTime - startTime)
print("Runtime : ", runTime, " s")        # Fastest Runtime: 11 hrs 51 min 44 sec

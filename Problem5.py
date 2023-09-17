import timeit

#Smallest multiple
def calc():
    # Number should be a multiple of all the prime factors
    num = 2*3*5*7*11*13*17*19 + 10  #Add 10 to make the second last digit even. Last digit is already zero. Last two digits must be an even number and zero for num to be divisible by 20 and 10.
    factors = list(range(1,21))     #list of factors
    k = 0
    while (k == 0): #While the flag stays down
        print(num)
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
            num = num + 20    # Number is even since even numbers can't be factors of odd numbers, but odd numbers can be factors of both odd and even numbers.
            #We add 20 because the final number must end in a multiple of 20.
        else:       #Else, the smallest multiple of 1-20 is found.
            break
    print(num, " is the answer.")
            
#Function call
startTime = timeit.default_timer()
calc()
endTime = timeit.default_timer()

runTime = (endTime - startTime)
print("Runtime : ", runTime, " s")        # Fastest Runtime: 1443.5525731319995 s

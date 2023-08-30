import timeit

#Even fibonacci numbers
def fibsum():
    #Starting values
    a = 1
    b = 2
    
    #Sum of even numbers
    sum = 2
    
    #Temporary sum of a and b
    x = 3
    while(x < 4000000):
        #while x < 4 million, check to make sure both a and b are both odd or both even to add up to an even sum
        if ((a%2 == 0) and (b%2 == 0)) or ((a%2 != 0) and (b%2 != 0)):
            x = a + b
            sum = sum + x
            a = b
            b = x
        else:
            #If not, continue finding fibonacci terms
            x = a + b
            a = b
            b = x
    print(sum)

startTime = timeit.default_timer()    
fibsum()
endTime = timeit.default_timer()

runTime = (endTime - startTime)*1000
print("Runtime : ", runTime, " ms.")        #Fastest runtime: 0.2691999834496528  ms

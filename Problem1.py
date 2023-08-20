import timeit

def adder():
    x = 3
    y = 5
    sum = 0
    
    #add all multiples of 3 under 1000
    while x < 1000:
        sum = sum + x
        x = x + 3
    
    #add all multiples of 5 under 1000 that are not also multiples of 3
    while y < 1000:
        if (y%3) != 0:
            sum = sum + y
        y = y + 5
    
    print(sum)

startTime = timeit.default_timer()
adder()
endTime = timeit.default_timer()

runTime = (endTime - startTime)*1000
print("Runtime : ", runTime, " ms.")        #Fastest runtime: 0.34849997 ms

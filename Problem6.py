import timeit

#Sum Square Difference
def calc():
    #Formulas/Mathematical Thought Process
    #   (a+b+c...+n)^2 = a^2 + b^2 + c^2 + ...... + n^2 + 2(ab+ac+....+an+bc+....+bn+c....+cn+....+(n-1)n) = x
    #   a^2 + b^2 + c^2 + .... + n^2 = y
    # We want x-y, so we end up finding 2(ab+ac+....+an+bc+....+bn+c....+cn+....+(n-1)n)
    
    #Use two loops to find the sum of all the products
    sum = 0
    for i in range(1,100):
        for j in range(i+1,101):
            sum = sum + i*j

    #Finally we multiply by two to get the final answer
    print(2*sum)

#Function call
startTime = timeit.default_timer()    
calc()
endTime = timeit.default_timer()

runTime = (endTime - startTime)*1000
print("Runtime : ", runTime, " ms")        #Fastest runtime: 0.39790000300854445  ms

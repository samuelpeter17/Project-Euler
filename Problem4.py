import timeit

#Largest Palindrome Product
def palindromer():
    #start with the two largest 3 digit numbers
    a = 999
    b = 999
    pals = []           #list to store palindrome products
    while len(str(a)) == 3:
        #start by multiplying a and b
        p1 = a * b
        p2 = reverse(p1)
        #if the product is a palindrome add it to the list
        if p1 == p2:
            pals.append(p1)
        #if not decrement by and find the next palindrome product
        b = b - 1
        #If b becomes a two digit number, decrement a and reset b to 999, hence while loops runs till a becomes 99
        if b == 99:
            a = a - 1 
            b = 999
    print(max(pals))

#Function to return the reverse of a given number    
def reverse(num):
    st = str(num)
    x = ""
    for i in st:
        x = i + x
    return int(x)

#Function call
startTime = timeit.default_timer()
palindromer()
endTime = timeit.default_timer()

runTime = (endTime - startTime)*1000
print("Runtime : ", runTime, " ms")        #Fastest runtime: 908.5469999990892  ms

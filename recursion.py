def openRussianDoll(doll):
    if doll==1:
        print("All dolls are opened")
    else:
        print(doll)
        openRussianDoll(doll-1)

openRussianDoll(6) 
print('--------------')
def recursiveMethod(n):
    # for n in recursiveMethod:
    #  n==6
    if n<1:
        print("n is less than 1")
    else:
        # n = 6
        recursiveMethod(n-1)
        print(n)

recursiveMethod(3)
print('--------------')

###-Recursion Methhod-###
def recursiveMethod(n):  
    if n < 1:            
        print("n is less than 1")
    else:    
        print(n)      
        recursiveMethod(n-1)   
recursiveMethod(6)         
print('--------------')

def factorial(n):
    if n == 0:
        # print("Factorial of 0 is 1")
        return 1
    else:
        return n * factorial(n-1)
print(factorial(0))
print('--------------')



####-Recursive Method-####
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2
print(powerOfTwo(3))

print('--------------')

####-Iterative Method-####
def powerOfTwo(n):
 i = 0
 power = 1
 while i < n:
     power = power * 2
     i = i + 1  
 return power
print(powerOfTwo(6)) 
print('--------------')

###-Fibonacci-###
def fibonacci(n):
    assert n >= 0 or int(n) == n , 'fibonacci number cannot be negative or non-integer number'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(16))
print('--------------')

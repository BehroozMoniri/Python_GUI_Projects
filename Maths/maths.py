# import math
factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

def factorial(num):
    if num < 0:
        print("Incorrect input")
    if num==0:
        return 1
    else: 
        return num * factorial (num-1)
    #return res

#res = factorial(10)
#print(res)


def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

res = Fibonacci(7)
print ("Fib 6" , res)
sum_of, fibs= [], []
for i in range(1,1000):
    fib = Fibonacci(i)
    fibs.append(fib)
    if fib > 4_000_000: 
        break
    if (fib %2 ==0):
        sum_of.append(fib)
print(fibs)
print(sum_of)
print(sum(sum_of))
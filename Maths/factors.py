import math , os
from time import process_time

from maths import factorial
def find_factors(n):
    if n<=0:
        print("Provide a positive number") 
    else:
        factors = set()
        #print(round(math.sqrt(n))+1)
        #print(n%3)
        for i in range(1,round(math.sqrt(n))+1,1):
            if (n%(i)==0) and (i!=0):
                factors.add(int(i))
                other_factor = int(n/i)
                factors.add(other_factor)

    return factors



def number_of_factors(num):
    return len(find_factors(num))

#print("number_of_factors(36): ",number_of_factors(36))


def primeFactors(n):
    prime_factors = set()
    # Print the number of two's that divide n
    while n % 2 == 0:
        prime_factors.add(2)
        n = n // 2
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i ad divide n
        while n % i== 0:
            prime_factors.add(i)
            n = n // i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        prime_factors.add(n)
    return prime_factors
# Driver Program to test above function
print("max factor: ",max(primeFactors(600851475143)))
n = 946
#print(primeFactors(n))
def primeFactorsBelow(num):
    primes =  set()
    for i in range(2,num):
        primes = primes.union(primeFactors(i))
    return primes

def sum_of_digits(num):
    sumOfDigits = 0
    done = True
    while(done) :
        sumOfDigits += num % 10 
        num -= num % 10 
        num  /= 10
        if num < 1:
            done =False
    return sumOfDigits
# print(factorial(10))
# print(sum_of_digits(factorial(100)))
#print(primeFactorsBelow(10))
#print(primeFactorsBelow(2000000))
#print(sum(primeFactorsBelow(2000000)))

start = process_time()
#print(primeFactorsBelow(20))
end = process_time()
time_taken = end - start
#print("Time it took in seconds: ", time_taken)

def generate_triangular_number(num):
    return sum([i for i in range(num+1)])

#print("generate_triangular_number(7)",generate_triangular_number(7))

def triangular_num_factors(  max_divisors):
    num = 10^100000
    for i in range(1, num):
        tran = generate_triangular_number(i)
        num_div = number_of_factors(tran)
        if num_div > max_divisors:
            return tran

#print("triangular_num_factors(500)", triangular_num_factors( 500))
one_up = os.path.dirname(__file__)
two_up = os.path.dirname(os.path.dirname(__file__))
# print(one_up)
#print("../os.getcwd()", "../" + os.getcwd() )

def read_file( file_name ="/numbers.txt"): 
    with open( one_up + file_name ,"r") as f:
        total , num_of_lines = 0, 0
        for line in f.readlines():
            total += (int(line) %  10000000000)
            num_of_lines+= 1
        print("total: ",total)
        res = total %  10000000000
        print("res: ",res)
        print("lines: ",num_of_lines)

# print("2^15: " , pow(2,15) )
# print("sum_of_digits(2^10): " ,sum_of_digits( pow(2,15)))

#print("2^1000: " , pow(2,1000) )
#print("sum_of_digits(2^1000): " ,sum_of_digits( pow(2,1000)))

# print("40! /(20! * 20!): ",factorial(40) / (factorial(20) *factorial(20)))

conversion = { 1: 3,  # one
              2: 3,     #two
              3:5,   #three
              4:4,  #four
              5:4,  #five
              6:3, #six
              7: 5, #seven
              8: 5 , #eight
              9: 4  #nine        
              }

print(conversion[9])

# def read_file_and_add_highest( file_name ="/trangle.txt"): 
#     with open( one_up + file_name ) as f:
#         total , num_of_line = 0, 0
#         for line in f.readlines():
#             line = list(line.rstrip("\n").split(" "))
#             arg_max, maximum = max(list(enumerate(line)), key=lambda x: x[1])
#             nextlinemax = max()
#             num_of_line += 1
#             print("line: ",line)
        #print("lines: ",num_of_line)
# read_file_and_add_highest("/trangle.txt")

# print("sum_of_digits(factorial(10)) ",sum_of_digits(factorial(10)))
# print("factorial(100) ", factorial(100))
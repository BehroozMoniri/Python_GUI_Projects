
from isPrime import IsPrime

def findRemainder( base, power, mod):
    if IsPrime(mod):
        if base > mod:
            base %= mod
            if base !=0:

                power %= (mod-1)
                res = pow(base, power) % mod
                #print(res)
                return res
            else:
                print("You must provide a base that is not a multiple of mod number")
                return
    print("You must provide a prime number as arg for modulus")

#print(findRemainder(128, 129, 17))


print(findRemainder(9565446989, 45646468987987, 11))

#print( pow(9565446989, 45646468987987)%11)
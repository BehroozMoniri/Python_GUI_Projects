

from math import sqrt

def Prime(number,itr):  #prime function to check given number prime or not
  #itr = int(sqrt(num)+1)
  
  if itr == 1:   #base condition
    return True
  if number % itr == 0:  #if given number divided by itr or not
    return False
  if Prime(number,itr-1) == False:   #Recursive function Call
    return False 
    
  return True
 
#num = 23

#itr = int(sqrt(num)+1)

#print(Prime(num,itr))

def IsPrime(num):
  itr = int(sqrt(num)+1)
  return  Prime(num,itr)

#print(IsPrime(num ))
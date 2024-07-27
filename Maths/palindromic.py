


def isPalindromic(num):
    order = list()
    while (num >=1):
        dig = num %10
        order.append(dig)
        num = num //10
    isTrue = []
    #print("order",order)
    for i, digit in enumerate(order):
        # print("i, digit", i, digit)
        # print("len(order)-i:", len(order)-(1+i))
        if (digit== order[len(order)-(1+i)]):
            isTrue.append(True)
        else:
            isTrue.append(False)
    if all(isTrue):
        return True
    else:
        return False
# function to reverse bits of a number
def reverseBits(n):
    rev = 0
  # traversing bits of 'n' from the right
    while (n > 0):
        # bitwise left shift 'rev' by 1
        rev = rev << 1
        # if current bit is '1'
        if (n & 1 == 1) :
            rev = rev ^ 1
        # bitwise right shift 'n' by 1
        n = n >> 1
        # required number
    #print("rev",rev)
    return rev
     
# function to check whether binary
# representation of a number is
# palindrome or not
def isPalindrome(n) :
    # get the number by reversing 
    # bits in the binary
    # representation of 'n'
    rev = reverseBits(n)
    return (n == rev)
 
 
# Driver program to test above
n = 9
if (isPalindrome(n)) :
    print("Yes")
else :
    print("No")
#print(isPalindromic(bin(10355301)))
def converttoBinary(num):
    print(int(str(bin(num))[2:-1]))
    return int(str(bin(num))[2:-1])

#print("converttoBinary(120)",  converttoBinary(256))
print(isPalindrome(585) )
print(isPalindromic(585))

list_of_paln =[]
for i in range(1,1000_000):

    if (isPalindrome(i) and isPalindromic(i)):
        list_of_paln.append(i)
print(list_of_paln)
print("sum: ",sum(list_of_paln))
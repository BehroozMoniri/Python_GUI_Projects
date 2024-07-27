def divide(a, b):
  '''Returns the decimal representation of the fraction a / b in three parts:
  integer part, non-recurring fractional part, and recurring part.'''
  assert b > 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder = remainder % b
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return (integer, digits[:where], digits[where:])
    else:
      seen[remainder] = len(digits)

# Some examples.
# for a, b in [(5,4), (1,6), (17,7), (22,11), (100,17)]:
#   (i, f, r) = divide(a, b)
#   print("%d/%d = %d.%s(%s)" % (a, b, i, ''.join(map(str, f)),
#                                ''.join(map(str,r))))
# Output:
# 5/4 = 1.25(0)
# 1/6 = 0.1(6)
# 17/7 = 2.(428571)
# 22/11 = 2.(0)
# 100/17 = 5.(8823529411764705)
longest = 0
num = 0
for j in range(1,1000):
    (i, f, r) = divide(1, j)
    rec = ''.join(map(str,r))
    if len(rec) > longest:
      longest = len(rec)
      num =  "%d/%d = %d.%s(%s)" % (1, j, i, ''.join(map(str, f)), ''.join(map(str,r)))
#print(num)
  
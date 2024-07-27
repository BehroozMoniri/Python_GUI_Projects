def f1(x=5,m= 3 ,d=2):
    d1, d2 = set(), set()
    for i in range(1, x+1):
        n = 1
        d1.add( n )
        n+=4*(i)
        d1.add(n)
        # do the same again
        n+=4*(i)
        d1.add(n)

        
        m+=d
        d2.add(m)
        d+=2
        m+=d
        d2.add(m)
        d+=2
        d3 = d1.union(d2)
        d3.add(n+x-1)
    print(d1)
    print(d2)
    print(d3)

def d2(x=5):
    d2 = set()
    sum1 = 1
    for i in range(1, (x*2) -1):
        sum1  += 2*i
        d2.add(sum1)
    return d2

#print("d2", d2(x=4))

def d1(x=5):
    sum1= 1
    d1 = set()
    d1.add(1)
    for i in range(1, x):
        sum1 += 4*i
        d1.add(sum1)
        sum1 += 4*i
        d1.add(sum1)
    return d1
#print("d1", d1(x=4))

def SquareSpiral(x = 3):
    x = (x//2) +1
    print("x: ",x)
    set1 = d1(x)
    set2 = d2(x)
    combined = sorted(set1.union(set2) )
    print(combined)
    #print("sum",sum(combined))
SquareSpiral(x = 10)



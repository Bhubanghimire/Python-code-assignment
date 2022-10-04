from fractions import *

def kempner(n):
    sum = Fraction(1,1)
    print(sum)
    for i in range(2,n+1):
        sum = sum+Fraction(1,i)
        sum=sum.limit_denominator(max_denominator=1000)
    
    result = Fraction(sum)
    return result

n=1000
result = kempner(n)
print(result)
    
    
import math

def sum_of_two_squares(n):
    status = False
    while (n>0):
        square = int(math.sqrt(n))

        remain=n-square**2
        print(remain)
        remain_square = int(math.sqrt(remain))
        if n==(square**2+remain_square**2):
            return (square, remain)
        else:
            n-=1

    
    
n=48
result = sum_of_two_squares(n)
print(result)
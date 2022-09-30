def pyramid_blocks(n, m, h):
    sum = 0
    for i in range(h):
        sum += (n+i)*(m+i)
    return sum

n=100
m=100
h=100
result = pyramid_blocks(n, m, h)
print(result)
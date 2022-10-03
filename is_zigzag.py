def is_zigzag(n):
    status = True
    n=str(n)
    if len(n)==1:
        return status
    previous = int(n[0])
    next_item = int(n[1])

    if (next_item-previous)>0:
        increase = True
    else:
        increase = False
    previous = next_item
    for idx in range(2,len(n)):
        current = int(n[idx])
        test = current-previous
        if increase:
            if test>=0:
                status = False
                break
        else:
            if test<=0:
                status = False
                break

    return status

n=49573912009
result = is_zigzag(n)
print(result)
from re import I
from unittest import result


def josephus(ls, skip):
    ls = [i+1 for i in range(n)]
    final_list = []
    skip -= 1 # pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        final_list.append(ls.pop(idx))
        idx = (idx + skip) % len(ls)
    print('survivor: ', ls[0])
    final_list.append(ls[0])

    return final_list

n=4
k=1

result = josephus(n,k)
print(result)
# [7, 6, 8, 2, 5, 1, 3, 4]
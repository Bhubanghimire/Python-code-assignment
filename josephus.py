from re import I
from unittest import result


def josephus(n, k):
    initial_list = [x+1 for x in range(n)]
    final_list = []
    index = 1
    while (len(initial_list)>=k):
        print(initial_list)
        for index,item in enumerate(initial_list):
            print(index, item)
            if (index+1)%k==0:
                final_list.append(item)
                initial_list.remove(item)

        print("ok")
    final_list.extend(initial_list)
    return final_list


n=4
k=1
result = josephus(n,k)
print(result)
from unittest import result


def josephus(n, k):
    final_list = []
    for i in range(n):
        final_list.append(i+1)

    return final_list


n=4
k=1

result = josephus(n,k)

print(result)
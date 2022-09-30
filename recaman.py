def recaman(n):
    final_list = []
    previous = 0
    for n in range(1,n+1):
        current = previous-n
        if current>0 and current not in final_list: 
            final_list.append(current)
        else:
            current = previous+n
            final_list.append(current)
        previous = current
    return final_list


n=100
result = recaman(n)
print(result)
[1, 3, 6, 2, 7, 13, 20, 12, 21, 11]
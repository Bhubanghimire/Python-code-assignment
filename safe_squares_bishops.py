def safe_squares_bishops(n, bishops):
    possible_list = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            tup = (i,j)
            possible_list.append(tup)
    for item in bishops:
        for tup in possible_list:
            x1=item[0]
            y1=item[1]
            x2=tup[0]
            y2=tup[1]
            if abs(x1-x2)==abs(y1-y2):
                possible_list.remove(tup)
    return len(list(set(possible_list)))        

n=100
bishops = [(row, (row*row) % 100) for row in range(100)]
result = safe_squares_bishops(n, bishops)
print(result)
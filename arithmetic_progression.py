from collections import Counter

def arithmetic_progression(items):
    difference = []
    for idx in range(len(items)-1):
        diff = items[idx+1]-items[idx]
        difference.append(diff)
    c = Counter(difference)
    print(c.most_common(1)[0])

    stride = c.most_common(1)[0][0]
    start = items[idx]
    for idx in range(len(items)-1):
        diff = items[idx+1]-items[idx]
        if diff ==stride:
            start = items[idx]
        break


    final_result = (start,c.most_common(1)[0][0],c.most_common(1)[0][1]+1)
    return final_result


items = range(10)
result = arithmetic_progression(items)
print(result)
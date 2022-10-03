def find_min(num1,num2,num3):
    if (num1 < num2) and (num1 < num3):
        largest = num1
    elif (num2 < num1) and (num2 < num3):
        largest = num2
    else:
        largest = num3
    return largest

def nearest_smaller(items):
    final_list = []
    length = len(items)
    previous = 100000000000

    for i in range(length-1):
        print(items[i])
        current = items[i]
        next_item = items[i+1]

        minimum = find_min(previous, current, next_item)
        final_list.append(minimum)
        previous = current
    
    if previous<items[length-1]:
        final_list.append(previous)
    else:
        final_list.append(items[length-1])

    return final_list



items = [6, 9, 3, 2,11,19,22]
result = nearest_smaller(items)
print(result)
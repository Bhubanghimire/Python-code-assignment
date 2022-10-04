def eliminate_neighbours(items):
    maxmimum = max(items)
    print(maxmimum)
    count = 1
    while True:
        
        minimum = min(items)
        position = items.index(minimum)

        if len(items)==2:
            return count
            
        if position==0:
            previous_item = 0
            next_item = items[position+1]
        elif position == len(items):
            previous_item=items[position-1]
            next_item = 0
        else:
            previous_item=items[position-1]
            next_item = items[position+1]
        
        if previous_item<next_item:
            items.remove(items[position])
            items.remove(next_item)
        else:
            items.remove(items[position])
            items.remove(previous_item)
        
        if maxmimum not in items:
            return count
        else:
            count +=1
    return count

items =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = eliminate_neighbours(items)
print(result)
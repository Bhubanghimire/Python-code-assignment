def tukeys_ninthers(items):
    result = None
    new_items=[]
    while(len(items)>3):
        total_break = len(items)//3
        for idx in range(2,len(items)+2,3):
            temp_list = [items[idx-2],items[idx-1],items[idx]]
            temp_list.sort()
            new_items.append(temp_list[1])
        
        items=[]
        items = new_items
        new_items = []
    if len(items)==3:
        items.sort()
        result = items[1]
    else:
        result = items[0]
    return result


items = [99, 42, 17, 7, 1, 9, 12, 77, 15]
# items.sort()
result = tukeys_ninthers(items)
print(result)
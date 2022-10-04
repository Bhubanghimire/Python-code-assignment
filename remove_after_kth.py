def remove_after_kth(items, k=1):
    final_list = []
    if k==0:
        return []
    test = [item for (index , item) in enumerate(items) if item == 1]
    for item in items:
        count = final_list.count(item)
        if count<k:
            final_list.append(item)
        
    return final_list

items = ['tom', 42, 'bob', 'bob', 99,'bob', 'tom', 'tom', 99]
k=2
result = remove_after_kth(items,k)
print(result)
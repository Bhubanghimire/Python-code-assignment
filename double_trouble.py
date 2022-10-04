def double_trouble(items, n):
    item = ""
    count=0
    
    for i in range(1,n+1):
        item = items[0]
        items.remove(items[0])
        items.append(item)
        items.append(item)
    item = items[0]
    return item
    
n=10**20
items =[17, 42, 99]
result = double_trouble(items, n)
print(result)
        

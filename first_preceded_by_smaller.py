def first_preceded_by_smaller(items, k=1):
    minimum=min(items)
    index = items.index(minimum)
    length = len(items)

    if index+k+1>length:
        return None
    else:
        return items[index+k]

items = [42, 99, 16, 55, 7, 32, 17, 18, 73]
k=8
result = first_preceded_by_smaller(items,k)
print(result)
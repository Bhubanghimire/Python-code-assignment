def collapse_intervals(items):
    intervals = ""
    if len(items)<1:
        return intervals
    elif len(items)==1:
        intervals += str(items[0])
    start_item = items[0]
    previous = items[0]
    length = len(items[1:])-1
    for idx,item in enumerate(items[1:]):
        if idx==length:
            string = f"{start_item}-{item},"
            intervals += string

        if item==previous+1:
            previous = item
        
        else:
            if start_item != previous:
                string = f"{start_item}-{previous},"
            else:
                string = f"{start_item},"
            intervals += string
            start_item = item
            previous = item
        
    return intervals

    
# items =[3, 5, 6, 7, 9, 11, 12, 13]
items = range(1, 101)
result = collapse_intervals(items)
print(result)
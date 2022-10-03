def count_distinct_sums_and_products(items):
    final_list = []
    for i in range(len(items)):
        for item in items:
            # print("ok")
            final_list.append(item+item)
            final_list.append(item*item)
            final_list.append(item+items[i])
            final_list.append(item*items[i])
    
    final_list = list(set(final_list))
    return len(final_list)



items = [x*x for x in range(1, 101)]
result = count_distinct_sums_and_products(items)
print(result)
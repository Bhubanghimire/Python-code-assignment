def expand_intervals(intervals):
    final_list = []
    initial_list = intervals.split(",")
    


    for item in initial_list:
        if item == '':
            return final_list
        item = item.split("-")
        if len(item)==1:
            final_list.append(int(item[0]))

        else:
            start = int(item[0])
            end = int(item[1])
            for itm in range(start,end+1):
                final_list.append(itm)

    return final_list

    
intervals ='1,3-9,12-14,9999'
result = expand_intervals(intervals)
print(result)
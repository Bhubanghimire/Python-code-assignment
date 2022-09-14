"""
Given a list of ​ items that are all guaranteed to be integers, create and return a new list whose first
two elements are the same as they were in original ​ items​ , after which each element equals the
median of the three elements in the original list ending in that position. (If two out of these three
elements are equal, then that element is the median of those three.)
"""

from typing import final


def running_median_of_three(items):
    final_list = []

    for index,item in enumerate(items):
        if index==0 or index==1:
            final_list.append(item)
        else:
            new_list = [items[index-2], items[index-1], items[index]]
            new_list.sort()
            final_list.append(new_list[1])
            print(new_list)

    return final_list


items = [5, 2, 9, 1, 7, 4, 6, 3, 8]
result = running_median_of_three(items)
print(result)
# [5, 2, 5, 2, 7, 4, 6, 4, 6]
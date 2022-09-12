"""
An element of ​ items is said to be a dominator if ​ every element to its right (and not just the one that
is immediate to its right) is strictly smaller than it. This function should count how many elements
in ​ items are dominators, and return that count. By this definition, the last item of the list is
automatically a dominator. For example, dominators of ​ [42, 7, 12, 9, 13, 5] would be the
elements 42, 13 and 5.
"""


def count_dominators(lst):
    if not lst:
        return 0
    lst.reverse()
    max_i = lst[0]
    n = 1
    for x in lst:
        if x > max_i:
            max_i = x
            n += 1
    return n


items = [1, 42, 55, 12, 19, 2, 1]
result = count_dominators(items)
print("length:", result)

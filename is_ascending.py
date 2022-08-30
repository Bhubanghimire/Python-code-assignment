"""
Determine whether the sequence of ​ item is ​ strictly ascending so that each element is ​ strictly
larger (not just merely equal to) than the element that precedes it. Return ​ True if the list of ​ item
is strictly ascending, and return ​ False otherwise. Note that the empty sequence is ascending, as is
also every one-element sequence, so be careful that your function returns the correct answers in
these seemingly insignificant ​ edge cases of this problem. (If these sequences were not ascending,
pray tell, what would be the two elements that violate the requirement and make that particular
sequence not be ascending?)
"""


def is_ascending(item):
    if len(item) == 0 or len(item) == 1:
        return True
    prev = item[0]
    status = True
    for item in item[1:]:
        if item <= prev:
            status = False
            break

    return status


items = [-5, 10, 99, 123456]
result = is_ascending(items)
print("result: ", result)

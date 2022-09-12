"""
A non-negative integer is said to be a ​ cyclops number if it consists of an ​ odd number of digits so
that the middle (more poetically, the "eye") digit is a zero, and all other digits of that number are
nonzero. This function should determine whether its parameter integer ​ n is a cyclops number, and
return either ​ True​ or ​ False​ accordingly.
"""


def is_cyclops(n):
    status = True
    length = int(len(str(n)))
    mid = int(length / 2)

    while length > 0:
        if (length-1) == mid:
            n = n // 10
            length -= 1

        else:
            item = n % 10
            if item == 0:
                status = False
                break
            n = n // 10
            length -= 1

    return status


input = 675409821
result = is_cyclops(input)
print(result)

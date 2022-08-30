def only_odd_digits(n):
    status = True
    length = len(str(n))
    while length >= 0:
        item = n % 10

        if item % 2 == 0:
            status = False
            break
        n = n // 10
        length -= 1

    return status


n = int("0")
result = only_odd_digits(n)
print(result)

"""
Given a list of ​ items whose length is guaranteed to be even (notice here that "oddly" enough, zero
is an even number), create and return a list produced by performing a perfect ​ riffle to the ​ items by
interleaving the items of the two halves of the list in an alternating fashion.
When performing a perfect riffle, also known as the ​ Faro shuffle​ , the list of ​ items is split in two
equal sized halves, either conceptually or in actuality. The first two elements of the result are then
the first elements of those halves. The next two elements of the result are the second elements of
those halves, followed by the third elements of those halves, and so on up to the last elements of
those halves. The parameter ​ out determines whether this function performs an ​ out shuffle or an ​ in
shuffle​ that determines which half of the deck the alternating card is first taken from.
"""


def riffle(item, out=True):
    final_list = []
    mid = int(len(item) / 2)
    first = item[0:mid]
    last = item[mid:]
    for i in range(mid):
        if out:
            final_list.append(first[i])
            final_list.append(last[i])
        else:
            final_list.append(last[i])
            final_list.append(first[i])
    return final_list


item = ['bob', 'jack']
item = [1, 2, 3, 4, 5, 6, 7, 8]
result = riffle(item)
print(result)
result = riffle(item, out=False)
print(result)

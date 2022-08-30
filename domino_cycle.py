"""
A single ​ domino tile is represented as a two-tuple of its ​ pip values​ , such as ​ (2, 5) or ​ (6, 6)​ .
This function should determine whether the given list of ​ tiles forms a ​ cycle so that each tile in the
list ends with the exact same pip value that its successor tile starts with, the successor of the last tile
being the first tile of the list since this is supposed to be a cycle instead of a chain. Return ​ True if the
given list of domino tiles form such a cycle, and ​ False​ otherwise.
"""


def domino_cycle(tiles):
    status = True
    length = len(tiles)

    if tiles[0][0] != tiles[length - 1][1] and length != 0:
        return False

    for item in range(length-1):
        if tiles[item][1] != tiles[item+1][0]:
            status=False
            break

    return status


# titles = [(3, 5), (5, 2), (2, 3)]
titles = [(4, 3), (3, 1)]
result = domino_cycle(titles)
print(result)

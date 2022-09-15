"""
This function creates ​ a list of lists that represents a two-dimensional ​ grid with the given number
of ​ rows and ​ cols​ . This grid should contain the integers counting the ​ rows * cols numbers from
start in ascending order. However, similar to the way an ox slowly plows a field somewhere back
in ancient Greece, the elements of every odd-numbered row
"""

def create_zigzag(rows, cols, start=1):
    l = []
    for i in range(rows):

        print(list(range(1,3)))
        # print(list(range(cols+start-1, start-1, -1)))
        l.append(list(range(cols+start-1, start-1, -1)) if i % 2 else list(range(start, cols+start)))
        start += cols
    return l


rows = 4
cols = 2

result = create_zigzag(rows, cols)
print(result)
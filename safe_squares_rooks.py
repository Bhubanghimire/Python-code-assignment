"""
On a generalized n - by-n chessboard, there are some number of rooks, each one represented as a
two-tuple(row, column) of the row and the column of the square that the rook is in. Since we are
again computer programmers instead of chess players and other normal folks, these rows and
columns are numbered from 0 to n - 1. A chess rook covers all squares that are in the same row or
in the same column as that rook. Given the board size n and the list of rooks on that board, count
the number of empty squares that are safe, that is, are not covered by any rook.
"""
def generate_tupple(r,c):
    tupple_list = []
    print(r,c)
    for i in range(r):
        for j in range(r):
            print(i)
            # tupple_list.append((i,j))
    return tupple_list
    
def safe_squares_rooks(n, rooks):
    final_list = []
    for i in range(n):
        for j in range(n):
            final_list.append((i,j))
    
    for rook in rooks:
        row = rook[0]
        col = rook[1]
        row_list = []
        col_list = []

        for i in range(n):
            row_list.append((row,i))
            col_list.append((i,col))
        
        _ = [final_list.remove(item) for item in row_list if item in final_list]
        _ = [final_list.remove(item) for item in col_list if item in final_list]

    
    return len(final_list)

n=6
rooks = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
result = safe_squares_rooks(n, rooks)
print(result)
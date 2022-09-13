"""
A Manhattan taxicab starts at the origin point(0, 0) of the two-dimensional grid of integers,
initially heading north. It then executes the given sequence of moves, given as a string made up of
the characters'L' for turning 90 degrees left (while standing in place),'R' for turning 90 degrees
right (ditto), and 'F' for moving one step forward towards its present heading. This function should
return the final position of the taxicab in the integer grid coordinates of Manhattan.
"""


def taxi_zum_zum(moves):
    x_pos = 0
    y_pos = 0
    dir = "N"
    
    for item in moves:
        if dir=="N":
            if item == "R":
                dir = "E"
            elif item == "L":
                dir = "W"

            else:
                y_pos +=1


        elif dir=="E":
            if item == "R":
                dir = "S"
            elif item == "L":
                dir = "N"

            else:
                x_pos +=1

        elif dir=="S":
            if item == "R":
                dir = "W"
            elif item == "L":
                dir = "E"

            else:
                y_pos -=1

        else:
            if item == "R":
                dir = "N"
            elif item == "L":
                dir = "S"

            else:
                x_pos -=1

    return x_pos, y_pos


moves = 'FRLFRL'
x,y = taxi_zum_zum(moves)
print(x,y)

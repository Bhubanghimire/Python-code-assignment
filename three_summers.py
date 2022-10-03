def three_summers(items, goal):
    print(items)
    if goal == 0 or goal < 1:
        return False
    elif len(items) == 0:
        return False
    else:
        if items[0] == goal:
            return [items[0]]
        else:
            with_v = three_summers(items[1:],(goal - items[0])) 
            if with_v:
                return True
            else:
                return three_summers(items[1:],goal)

    return status


items = [1,2,3]
goal = 5

result = three_summers(items, goal)
print(result)
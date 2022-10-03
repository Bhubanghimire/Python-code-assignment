
def backwards(items):
        items=items[::-1]
        return items

def reverse_reversed(items):
    print(items)
    final_list = []
    if isinstance(items, list):
        
        for a in backwards(items):
            final_list.append(reverse_reversed(a))
        return final_list
    return items
items = [42, [99, [17, [33, ['boo!']]]]]
result = reverse_reversed(items)
print(result)